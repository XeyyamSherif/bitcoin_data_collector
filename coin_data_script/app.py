import requests
import pandas as pd
import sqlite3

class BinanceDataCollector:
    def __init__(self, interval, symbol):
        self.interval = interval
        self.symbol = symbol

    def collect_data(self):
        url = f"https://api.binance.com/api/v3/klines?symbol={self.symbol}&interval={self.interval}"
        print(url)
        response = requests.get(url)
        data = response.json()

        df = self._format_data(data)

        # Save data to CSV
        csv_filename = f"{self.symbol}_{self.interval}_data.csv"
        df.to_csv(csv_filename, index=False)

        # Save data to relational database (SQLite in this example)
        self._save_to_database(df)

    def _format_data(self, data):
        df = pd.DataFrame(data, columns=['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time',
                                         'Quote Asset Volume', 'Number of Trades', 'Taker Buy Base Asset Volume',
                                         'Taker Buy Quote Asset Volume', 'Ignore'])
        df['Open Time'] = pd.to_datetime(df['Open Time'], unit='ms')
        return df

    def _save_to_database(self, df):
        conn = sqlite3.connect('crypto_data.db')
        table_name = f"{self.symbol}_{self.interval}_data"
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()

# Example usage
collector = BinanceDataCollector('1d', 'BTCUSDT')
collector.collect_data()

