import requests
import pandas as pd
import time
from openpyxl import Workbook
import threading

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": False
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def write_to_excel(data, file_name="Live_Crypto_Data.xlsx"):
    try:
        workbook = Workbook()
        sheet = workbook.active
        sheet.append([
            "Cryptocurrency", "Symbol", "Price (USD)", "Market Cap (USD)",
            "24h Volume (USD)", "24h Change (%)"
        ])
        
        for crypto in data:
            sheet.append([
                crypto.get('name', 'N/A'),
                crypto.get('symbol', 'N/A'),
                crypto.get('current_price', 'N/A'),
                crypto.get('market_cap', 'N/A'),
                crypto.get('total_volume', 'N/A'),
                crypto.get('price_change_percentage_24h', 'N/A')
            ])
        
        workbook.save(file_name)
        print(f"Data written to {file_name}")
    except Exception as e:
        print(f"Error writing data to Excel: {e}")

def analyze_data(data):
    try:
        df = pd.DataFrame(data)
        
        top_5 = df.nlargest(5, "market_cap")[["name", "market_cap"]]
        print("\nTop 5 Cryptocurrencies by Market Cap:")
        print(top_5)
        
        avg_price = df["current_price"].mean()
        print(f"\nAverage Price of Top 50 Cryptocurrencies: ${avg_price:.2f}")
        
        highest_change = df.nlargest(1, "price_change_percentage_24h")[["name", "price_change_percentage_24h"]]
        lowest_change = df.nsmallest(1, "price_change_percentage_24h")[["name", "price_change_percentage_24h"]]
        print("\nHighest 24h Change:")
        print(highest_change)
        print("\nLowest 24h Change:")
        print(lowest_change)
    except Exception as e:
        print(f"Error during data analysis: {e}")

def update_crypto_data():
    while True:
        try:
            print("\nFetching live data...")
            data = fetch_crypto_data()
            if data:
                write_to_excel(data)
                analyze_data(data)
            else:
                print("Failed to fetch data.")
        except Exception as e:
            print(f"Error in update loop: {e}")
        time.sleep(300)

def main():
    print("Starting the live update process...")
    thread = threading.Thread(target=update_crypto_data)
    thread.daemon = True
    thread.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping the live update process.")

if __name__ == "__main__":
    main()
