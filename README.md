# Binance Data Collector

This application collects data from the Binance API for a specified interval and symbol, and saves the data in both CSV and a relational database (SQLite).

# Flask Candlestick Chart App

This Flask application displays a candlestick chart using data from a CSV file. The app utilizes the Plotly library to generate dynamic candlestick charts.


First run the script then flask app

## Requirements

- Python 3.x
- pandas
- requests
- sqlite3
- Flask

## Installation

1. Clone the repository:
2. Activate virtual enviroment:

For windows:

    - create a virtual environment
    - python -m venv venv

    - Activate the virtual environment
        venv\Scripts\activate

For Ubuntu:

    - create a virtual environment
    - python3 -m venv venv

    - Activate the virtual environment
        source venv/bin/activate

3. Install the requirements with this command in enviroment
    -  `pip3 install -r requirements.txt`

## Usage of script

1. Open the `app.py` file and modify the `interval` and `symbol` variables according to your desired values.

2. Run the script:


## Usage of Flask

1. Ensure that the data file `BTCUSDT_1d_data.csv` exists in the root directory of the project. This file should contain the necessary candlestick data.

2. Run the Flask application:

3. Open a web browser and navigate to `http://localhost:5000` to view the candlestick chart.
