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

# Comprehensive mapping of ISO2 country codes to ENTSO-E bidding zone identifiers
# Source: ENTSO-E official bidding zone data (45 countries, primary zones)
COUNTRY_CODES = {
    # Southeastern Europe
    "AL": "10YAL-KESH-----5",  # Albania
    "BA": "10YBA-JPCC-----D",  # Bosnia and Herzegovina
    "BG": "10YCA-BULGARIA-R",  # Bulgaria
    "HR": "10YHR-HEP------M",  # Croatia
    "CY": "10YCY-1001A0003J",  # Cyprus
    "GR": "10YGR-HTSO-----Y",  # Greece
    "HU": "10YHU-MAVIR----U",  # Hungary
    "MK": "10YMK-MEPSO----8",  # North Macedonia
    "ME": "10YCS-CG-TSO---S",  # Montenegro
    "RO": "10YRO-TEL------P",  # Romania
    "RS": "10YCS-SERBIATSOV",  # Serbia
    "SI": "10YSI-ELES-----O",  # Slovenia
    "XK": "10Y1001C--00100H",  # Kosovo

    # Central Europe
    "AT": "10YAT-APG------L",  # Austria
    "CZ": "10YCZ-CEPS-----N",  # Czech Republic
    "DE": "10Y1001A1001A83F",  # Germany
    "LU": "10YLU-CEGEDEL-NQ",  # Luxembourg
    "PL": "10YPL-AREA-----S",  # Poland
    "SK": "10YSK-SEPS-----K",  # Slovakia

    # Western Europe
    "BE": "10YBE----------2",  # Belgium
    "FR": "10YFR-RTE------C",  # France
    "NL": "10YNL----------L",  # Netherlands
    "CH": "10YCH-SWISSGRIDZ",  # Switzerland

    # Northern Europe
    "DK": "10Y1001A1001A65H",  # Denmark
    "EE": "10Y1001A1001A39I",  # Estonia
    "FI": "10YFI-1--------U",  # Finland
    "IS": "IS",                 # Iceland (special case)
    "IE": "10YIE-1001A00010",  # Ireland
    "LV": "10YLV-1001A00074",  # Latvia
    "LT": "10YLT-1001A0008Q",  # Lithuania
    "NO": "10YNO-0--------C",  # Norway
    "SE": "10YSE-1--------K",  # Sweden
    "GB": "10YGB----------A",  # United Kingdom

    # Southern Europe
    "ES": "10YES-REE------0",  # Spain
    "IT": "10YIT-GRTN-----B",  # Italy
    "MT": "10Y1001A1001A93C",  # Malta
    "PT": "10YPT-REN------W",  # Portugal

    # Eastern Europe
    "BY": "10Y1001A1001A51S",  # Belarus
    "MD": "10Y1001A1001A990",  # Moldova
    "RU": "10Y1001A1001A49F",  # Russia
    "UA": "10Y1001C--00003F",  # Ukraine
    "GE": "10Y1001A1001B012",  # Georgia
    "TR": "10YTR-TEIAS----W",  # Turkey
}

ISO3_TO_ISO2 = {
    "ALB": "AL", "AND": "AD", "ARM": "AM", "AUT": "AT", "AZE": "AZ", "BLR": "BY", "BEL": "BE", "BIH": "BA",
    "BGR": "BG", "HRV": "HR", "CYP": "CY", "CZE": "CZ", "DNK": "DK", "EST": "EE", "FIN": "FI", "FRA": "FR",
    "GEO": "GE", "DEU": "DE", "GRC": "GR", "HUN": "HU", "ISL": "IS", "IRL": "IE", "ITA": "IT", "XKX": "XK",
    "LVA": "LV", "LIE": "LI", "LTU": "LT", "LUX": "LU", "MKD": "MK", "MLT": "MT", "MDA": "MD", "MCO": "MC",
    "MNE": "ME", "NLD": "NL", "NOR": "NO", "POL": "PL", "PRT": "PT", "ROU": "RO", "RUS": "RU", "SMR": "SM",
    "SRB": "RS", "SVK": "SK", "SVN": "SI", "ESP": "ES", "SWE": "SE", "CHE": "CH", "UKR": "UA", "GBR": "GB"
}

def normalize_country_iso2(country_code):
    if not country_code:
        return None
    country_code = country_code.upper()
    if len(country_code) == 2:
        return country_code
    if len(country_code) == 3:
        return ISO3_TO_ISO2.get(country_code)
    return None

# Countries with multiple bidding zones – mapping ISO2 to list of (zone_name, eic_code) tuples
COUNTRY_ZONES = {
    "DE": [
        ("Germany (main)", "10YCB-GERMANY--8 "),
        ("Germany (50Hertz)", "10YDE-VE-------2"),
        ("Germany (Amprion)", "10YDE-RWENET---I"),
        ("Germany (TenneT)", "10YDE-EON------1"),
        ("Germany (TransnetBW)", "10YDE-ENBW-----N"),
    ],
    "DK": [
        ("Denmark DK1", "10YDK-1--------W"),
        ("Denmark DK2", "10YDK-2--------M"),
    ],
    "NO": [
        ("Norway NO1", "10YNO-1--------2"),
        ("Norway NO2", "10YNO-2--------T"),
        ("Norway NO3", "10YNO-3--------J"),
        ("Norway NO4", "10YNO-4--------9"),
        ("Norway NO5", "10Y1001A1001A48H"),
    ],
    "SE": [
        ("Sweden SE1", "10Y1001A1001A44P"),
        ("Sweden SE2", "10Y1001A1001A45N"),
        ("Sweden SE3", "10Y1001A1001A46L"),
        ("Sweden SE4", "10Y1001A1001A47J"),
    ],
    "IT": [
        ("Italy North", "10Y1001A1001A73I"),
        ("Italy Centre-North", "10Y1001A1001A70O"),
        ("Italy Centre-South", "10Y1001A1001A71M"),
        ("Italy South", "10Y1001A1001A788"),
        ("Italy Sicily", "10Y1001A1001A75E"),
        ("Italy Sardinia", "10Y1001A1001A74G"),
    ],
    "UA": [
        ("Ukraine (main)", "10Y1001C--00003F"),
        ("Ukraine DobTPP", "10Y1001A1001A869"),
        ("Ukraine BEI", "10YUA-WEPS-----0"),
        ("Ukraine IPS", "10Y1001C--000182"),
    ],
    "IE": [
        ("NIR", "10Y1001A1001A59C"),
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

@app.route('/api/zones/<country_code>')
def get_zones(country_code):
    """Return available zones for a country if it has multiple zones."""
    country_iso2 = normalize_country_iso2(country_code)
    print(f"Zones lookup: input={country_code} normalized={country_iso2}")
    
    if not country_iso2 or country_iso2 not in COUNTRY_ZONES:
        return jsonify({"error": f"Ország nincs a több zonás listán: {country_code}"}), 404
    
    zones = COUNTRY_ZONES[country_iso2]
    return jsonify({
        "country": country_iso2,
        "zones": [
            {"name": name, "code": code}
            for name, code in zones
        ]
    })
    
@app.route('/api/prices')
def get_prices():
    start_str = request.args.get('start')
    end_str = request.args.get('end')
    country_param = request.args.get('country')
    zone_code = request.args.get('zone')  # Optional specific zone code

    if not start_str or not end_str:
        return jsonify({"error": "Hiányzó dátumok"}), 400

    # resolve ENTSO-E bidding zone identifier
    country_code = None
    country_iso2 = normalize_country_iso2(country_param) if country_param else None
    if zone_code:
        # Use the explicit zone code provided
        country_code = zone_code
    elif country_param:
        if not country_iso2:
            return jsonify({"error": f"Ismeretlen országkód: {country_param}"}), 400
        country_code = COUNTRY_CODES.get(country_iso2)
        if not country_code:
            return jsonify({"error": f"Ismeretlen országkód: {country_param}"}), 400
    else:
        country_code = DEFAULT_COUNTRY_CODE

    try:
        client = EntsoePandasClient(api_key=API_KEY)
        
        # Dátumok konvertálása az ENTSO-E formátumára
        start = pd.Timestamp(start_str, tz='Europe/Budapest')
        end = pd.Timestamp(end_str, tz='Europe/Budapest') + pd.Timedelta(days=1)

        # API hívás
        selected_zone_name = None
        if zone_code and country_iso2 in COUNTRY_ZONES:
            for name, code in COUNTRY_ZONES[country_iso2]:
                if code == zone_code:
                    selected_zone_name = name
                    break

        print(
            f"Debug: country_param={country_param} normalized_iso2={country_iso2} "
            f"zone_code={zone_code} zone_name={selected_zone_name}"
        )
        #print(f"Lekérdezés: {country_code} ----- {country_iso2}")
        if selected_zone_name == None:
            print("SIMA")
            ts = client.query_day_ahead_prices(country_iso2, start=start, end=end)
        else:
            ts = client.query_day_ahead_prices(zone_code, start=start, end=end)

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