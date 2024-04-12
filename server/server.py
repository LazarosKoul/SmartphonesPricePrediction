from flask import Flask, request, jsonify
import util
from numpy import nan
app= Flask(__name__)

def parsingBooleanValue(string_value):
    string_value = string_value.lower()
    if string_value in ['true', 'yes']:
        return True
    if string_value in ['false', 'no']:
        return False
    return nan

@app.route('/get_categorical_values')
def get_categorical_values():
    response = jsonify( util.__categorical_values )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_estimated_price', methods=['POST'])
def get_estimated_price():
    print("[POST] For get_estimated_price...")
    try:
        brand_name = request.form['brand_name'] if  ('brand_name' in request.form) else None
        num_cores = int(request.form['num_cores'])
        ram_capacity = float(request.form['ram_capacity'])
        internal_memory = float(request.form['internal_memory'])
        battery_capacity = float(request.form['battery_capacity'])
        fast_charging_available = parsingBooleanValue(request.form['fast_charging_available'])
        primary_camera_rear = float(request.form['primary_camera_rear'])
        primary_camera_front = float(request.form['primary_camera_front'])
    except:
        print("Something went wrong with the parsing of POST's body.")

    try:
        estimated_price = util.get_estimated_price(brand_name, num_cores,
                                                    ram_capacity, internal_memory,
                                                    battery_capacity, fast_charging_available,
                                                    primary_camera_rear, primary_camera_front)
    except:
        estimated_price = -40
        print("Something went wrong with the estimator's prediction.")

    response = jsonify({ 'estimated_price': str(estimated_price)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server for Phone Price Regression...")
    util.load_saved_artifacts()
    app.run()