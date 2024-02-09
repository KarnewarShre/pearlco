import pandas as pd
from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/calculate_returns', methods=['GET'])
def calculate_returns():
    file_path = request.args.get('file_path')

    if file_path is None:
        return jsonify({'error': 'Please provide a valid file path'})
    try:
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip()
        df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y')


        df = df.sort_values('Date')
        df['Daily Return'] = df['Close'].pct_change()
        df['Daily Return'] = df['Daily Return'].round(4)

        length_data = len(df)
        annualized_volatility = df['Close'].pct_change().std() * np.sqrt(length_data)
        annualized_volatility = round(annualized_volatility, 3)

        result = {
            'file_path': file_path,
            'daily_returns': df['Daily Return'].tolist(),
            'annualized_volatility': annualized_volatility
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
