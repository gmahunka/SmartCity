import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from entsoe import EntsoePandasClient
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import json
load_dotenv()

app = Flask(__name__)
CORS(app)

API_KEY = os.environ.get("ENTSOE_API_KEY")
# default ENTSO-E code (Hungary) – used when no country is specified or lookup fails
DEFAULT_COUNTRY_CODE = "10YHU-MAVIR----U"

# Comprehensive mapping of ISO3 country codes to ENTSO-E bidding zone identifiers
# Source: ENTSO-E official bidding zone data (45 countries, primary zones)
COUNTRY_CODES = {
    # Southeastern Europe
    "ALB": "10YAL-KESH-----5",  # Albania
    "BIH": "10YBA-JPCC-----D",  # Bosnia and Herzegovina
    "BGR": "10YCA-BULGARIA-R",  # Bulgaria
    "HRV": "10YHR-HEP------M",  # Croatia
    "CYP": "10YCY-1001A0003J",  # Cyprus
    "GRC": "10YGR-HTSO-----Y",  # Greece
    "HUN": "10YHU-MAVIR----U",  # Hungary
    "MKD": "10YMK-MEPSO----8",  # North Macedonia
    "MNE": "10YCS-CG-TSO---S",  # Montenegro
    "ROU": "10YRO-TEL------P",  # Romania
    "SRB": "10YCS-SERBIATSOV",  # Serbia
    "SVN": "10YSI-ELES-----O",  # Slovenia
    "XKX": "10Y1001C--00100H",  # Kosovo

    # Central Europe
    "AUT": "10YAT-APG------L",  # Austria
    "CZE": "10YCZ-CEPS-----N",  # Czech Republic
    "DEU": "10Y1001A1001A83F",  # Germany
    "LUX": "10YLU-CEGEDEL-NQ",  # Luxembourg
    "POL": "10YPL-AREA-----S",  # Poland
    "SVK": "10YSK-SEPS-----K",  # Slovakia

    # Western Europe
    "BEL": "10YBE----------2",  # Belgium
    "FRA": "10YFR-RTE------C",  # France
    "NLD": "10YNL----------L",  # Netherlands
    "CHE": "10YCH-SWISSGRIDZ",  # Switzerland

    # Northern Europe
    "DNK": "10Y1001A1001A65H",  # Denmark
    "EST": "10Y1001A1001A39I",  # Estonia
    "FIN": "10YFI-1--------U",  # Finland
    "ISL": "IS",                 # Iceland (special case)
    "IRL": "10YIE-1001A00010",  # Ireland
    "LVA": "10YLV-1001A00074",  # Latvia
    "LTU": "10YLT-1001A0008Q",  # Lithuania
    "NOR": "10YNO-0--------C",  # Norway
    "SWE": "10YSE-1--------K",  # Sweden
    "GBR": "10YGB----------A",  # United Kingdom

    # Southern Europe
    "ESP": "10YES-REE------0",  # Spain
    "ITA": "10YIT-GRTN-----B",  # Italy
    "MLT": "10Y1001A1001A93C",  # Malta
    "PRT": "10YPT-REN------W",  # Portugal

    # Eastern Europe
    "BLR": "10Y1001A1001A51S",  # Belarus
    "MDA": "10Y1001A1001A990",  # Moldova
    "RUS": "10Y1001A1001A49F",  # Russia
    "UKR": "10Y1001C--00003F",  # Ukraine
    "GEO": "10Y1001A1001B012",  # Georgia
    "TUR": "10YTR-TEIAS----W",  # Turkey
}

# Countries with multiple bidding zones – mapping ISO3 to list of (zone_name, eic_code) tuples
COUNTRY_ZONES = {
    "DEU": [
        ("Germany (main)", "10Y1001A1001A83F"),
        ("Germany (50Hertz)", "10YDE-VE-------2"),
        ("Germany (Amprion)", "10YDE-RWENET---I"),
        ("Germany (TenneT)", "10YDE-EON------1"),
        ("Germany (TransnetBW)", "10YDE-ENBW-----N"),
    ],
    "DNK": [
        ("Denmark (main)", "10Y1001A1001A65H"),
        ("Denmark DK1", "10YDK-1--------W"),
        ("Denmark DK2", "10YDK-2--------M"),
    ],
    "NOR": [
        ("Norway (main)", "10YNO-0--------C"),
        ("Norway NO1", "10YNO-1--------2"),
        ("Norway NO2", "10YNO-2--------T"),
        ("Norway NO3", "10YNO-3--------J"),
        ("Norway NO4", "10YNO-4--------9"),
        ("Norway NO5", "10Y1001A1001A48H"),
    ],
    "SWE": [
        ("Sweden (main)", "10YSE-1--------K"),
        ("Sweden SE1", "10Y1001A1001A44P"),
        ("Sweden SE2", "10Y1001A1001A45N"),
        ("Sweden SE3", "10Y1001A1001A46L"),
        ("Sweden SE4", "10Y1001A1001A47J"),
    ],
    "ITA": [
        ("Italy (main)", "10YIT-GRTN-----B"),
        ("Italy North", "10Y1001A1001A73I"),
        ("Italy Centre-North", "10Y1001A1001A70O"),
        ("Italy Centre-South", "10Y1001A1001A71M"),
        ("Italy South", "10Y1001A1001A788"),
        ("Italy Sicily", "10Y1001A1001A75E"),
        ("Italy Sardinia", "10Y1001A1001A74G"),
    ],
    "UKR": [
        ("Ukraine (main)", "10Y1001C--00003F"),
        ("Ukraine DobTPP", "10Y1001A1001A869"),
        ("Ukraine BEI", "10YUA-WEPS-----0"),
        ("Ukraine IPS", "10Y1001C--000182"),
    ],
    "GBR": [
        ("United Kingdom", "10YGB----------A"),
        ("UK IFA", "10Y1001C--00098F"),
        ("UK IFA2", "17Y0000009369493"),
        ("UK ElecLink", "11Y0-0000-0265-K"),
    ],
    "IRL": [
        ("Ireland (main)", "10YIE-1001A00010"),
        ("Ireland SEM", "10Y1001A1001A59C"),
    ],
}

if not API_KEY:
    raise RuntimeError("ENTSOE_API_KEY environment variable is required")

def get_eur_huf_rate(date_str):
    try:
        url = f"https://api.frankfurter.app/{date_str}?from=EUR&to=HUF"
        r = requests.get(url, timeout=5)
        return r.json()['rates']['HUF']
    except:
        return 410.0

@app.route('/api/zones/<country_iso3>')
def get_zones(country_iso3):
    """Return available zones for a country if it has multiple zones."""
    country_iso3 = country_iso3.upper()
    
    if country_iso3 not in COUNTRY_ZONES:
        return jsonify({"error": f"Ország nincs a több zonás listán: {country_iso3}"}), 404
    
    zones = COUNTRY_ZONES[country_iso3]
    return jsonify({
        "country": country_iso3,
        "zones": [
            {"name": name, "code": code}
            for name, code in zones
        ]
    })
    
@app.route('/api/prices')
def get_prices():
    start_str = request.args.get('start')
    end_str = request.args.get('end')
    country_iso3 = request.args.get('country')  # ISO3 code coming from the frontend
    zone_code = request.args.get('zone')  # Optional specific zone code

    if not start_str or not end_str:
        return jsonify({"error": "Hiányzó dátumok"}), 400

    # resolve ENTSO-E bidding zone identifier
    country_code = None
    if zone_code:
        # Use the explicit zone code provided
        country_code = zone_code
    elif country_iso3:
        country_iso3 = country_iso3.upper()
        country_code = COUNTRY_CODES.get(country_iso3)
        if not country_code:
            return jsonify({"error": f"Ismeretlen országkód: {country_iso3}"}), 400
    else:
        country_code = DEFAULT_COUNTRY_CODE

    try:
        client = EntsoePandasClient(api_key=API_KEY)
        
        # Dátumok konvertálása az ENTSO-E formátumára
        start = pd.Timestamp(start_str, tz='Europe/Budapest')
        end = pd.Timestamp(end_str, tz='Europe/Budapest') + pd.Timedelta(days=1)

        # API hívás
        ts = client.query_day_ahead_prices(country_code, start=start, end=end)
        df = pd.DataFrame(ts, columns=['EUR_MWh'])
        
        # Árfolyam lekérés (a választott időszak első napjára, egyszerűsítve)
        huf_rate = get_eur_huf_rate(start_str)
        df['HUF_kWh'] = (df['EUR_MWh'] * huf_rate) / 1000
        
        # JSON formátumra alakítás a frontendnek
        result = df.reset_index()
        result.columns = ['time', 'EUR_MWh', 'HUF_kWh']
        return result.to_json(orient='records', date_format='iso')

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)