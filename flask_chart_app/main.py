from flask import Flask, render_template, jsonify
import pandas as pd
import json
import os

app = Flask(__name__)


@app.route('/')
def index():
    try:
        # Check if the file exists
        file_path = 'BTCUSDT_1d_data.csv'
        if not os.path.isfile(file_path):
            raise FileNotFoundError
        
        df = pd.read_csv(file_path)

        # Prepare data for chart
        candlestick_data = {
            'x': df['Open Time'].tolist(),
            'open': df['Open'].tolist(),
            'high': df['High'].tolist(),
            'low': df['Low'].tolist(),
            'close': df['Close'].tolist()
        }

        return render_template('index.html', candlestick_data=json.dumps(candlestick_data))

    except FileNotFoundError:
        error_message = "Data file not found."
        print('salam')
        return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)