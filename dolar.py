from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_usd_value')
def get_usd_value():
    response = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
    data = response.json()
    usd_brl_value = "{:.4f}".format(float(data['USDBRL']['ask']))
    var_bid = data['USDBRL']['varBid']
    pct_change = data['USDBRL']['pctChange'] + '%'
    return jsonify({'usd_brl_value': usd_brl_value, 'var_bid': var_bid, 'pct_change': pct_change})

@app.route('/get_server_time')
def get_server_time():
    import datetime
    server_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return jsonify({'server_time': server_time})

if __name__ == '__main__':
    app.run(debug=True)
