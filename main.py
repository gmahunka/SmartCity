import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from entsoe import EntsoePandasClient
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

# load variables from .env (optional; install python-dotenv)
load_dotenv()


app = Flask(__name__)
CORS(app)


API_KEY = os.environ.get("ENTSOE_API_KEY")
COUNTRY_CODE = "10YHU-MAVIR----U"  # Magyarország (HUPX) kódja

if not API_KEY:
    raise RuntimeError("ENTSOE_API_KEY environment variable is required")

def get_eur_huf_rate(date_str):
    try:
        url = f"https://api.frankfurter.app/{date_str}?from=EUR&to=HUF"
        r = requests.get(url, timeout=5)
        return r.json()['rates']['HUF']
    except:
        return 410.0
    
@app.route('/api/prices')
def get_prices():
    # A frontendtől érkező paraméterek (pl: ?start=2024-02-01&end=2024-02-05)
    start_str = request.args.get('start')
    end_str = request.args.get('end')

    if not start_str or not end_str:
        return jsonify({"error": "Hiányzó dátumok"}), 400

    try:
        client = EntsoePandasClient(api_key=API_KEY)
        
        # Dátumok konvertálása az ENTSO-E formátumára
        start = pd.Timestamp(start_str, tz='Europe/Budapest')
        end = pd.Timestamp(end_str, tz='Europe/Budapest') + pd.Timedelta(days=1)

        # API hívás
        ts = client.query_day_ahead_prices(COUNTRY_CODE, start=start, end=end)
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

# def get_multi_day_prices(days_back):
#     client = EntsoePandasClient(api_key=API_KEY)
    
#     now = pd.Timestamp.now(tz='Europe/Budapest')
#     start = (now - pd.Timedelta(days=days_back)).replace(hour=0, minute=0, second=0)
#     end = now

#     try:
#         # 1. Áramárak lekérése (EUR-ban jön meg)
#         ts = client.query_day_ahead_prices(COUNTRY_CODE, start=start, end=end)
#         df = pd.DataFrame(ts, columns=['EUR_MWh'])
        
#         # 2. Árfolyam hozzárendelése minden egyes órához külön-külön
#         def apply_rate(index):
#             # Kiszedjük a dátumot az időbélyegből (pl. 2024-05-20)
#             day_str = index.strftime('%Y-%m-%d')
#             return get_eur_huf_rate(day_str)

#         # Új oszlop az árfolyamnak (napi szinten változik)
#         df['Exchange_Rate'] = df.index.map(apply_rate)
        
#         # 3. Kiszámoljuk a HUF árat a soronkénti árfolyammal
#         df['HUF_kWh'] = (df['EUR_MWh'] * df['Exchange_Rate']) / 1000
        
#         print(f"--- Lekért időszak: {start.date()} - {end.date()} ---")
#         print(f"{'Időpont':<16} | {'EUR/MWh':<10} | {'Árfolyam':<8} | {'HUF/kWh':<10}")
#         print("-" * 55)

#         for index, row in df.tail(10).iterrows():
#             print(f"{index.strftime('%m-%d %H:%M'):<16} | {row['EUR_MWh']:>10.2f} | {row['Exchange_Rate']:>8.2f} | {row['HUF_kWh']:>8.2f} Ft")
        
#         df.reset_index().to_json("energy_data.json", orient="records", date_format="iso")

#     except Exception as e:
#         print(f"Hiba: {e}")

# if __name__ == "__main__":
#     get_multi_day_prices(2)