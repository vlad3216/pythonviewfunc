from unittest import result
from flask import Flask, request
from func import get_filtered_customers, get_count_of_firstname, get_all_profit

app = Flask(__name__)


@app.route("/customers", methods=['GET'])
def get_customers():
    city = request.args.get('city')
    state = request.args.get('state')
    result = get_filtered_customers(city, state)
    return result


@app.route("/firstname", methods=['GET'])
def get_count_firstname():
    return get_count_of_firstname()


@app.route("/profit", methods=['GET'])
def get_profit():
    profit = round(get_all_profit()[0][0], 2)
    result = f'orders sum - {profit}'
    return result