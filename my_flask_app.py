from flask import Flask, render_template, request
import requests

app = Flask(__name__)


def get_exchange_rate(base, target):
    url = f"https://api.exchangerate-api.com/v4/latest/{base}"
    response = requests.get(url)
    data = response.json()
    return data['rates'][target]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    base_currency = request.form['base_currency']
    target_currency = request.form['target_currency']
    amount = float(request.form['amount'])

    exchange_rate = get_exchange_rate(base_currency, target_currency)
    converted_amount = amount * exchange_rate

    return render_template('index.html',
                           result=f"{amount} {base_currency} равно {converted_amount} {target_currency}")


if __name__ == '__main__':
    app.run(debug=True)