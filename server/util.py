import json
import numpy as np
import pandas as pd
import xgboost as xgb
from static_vars import  MODEL_FILE_PATH, UNIQUE_CATEGORICAL_VALUES_FILE_PATH

__model = None
__categorical_values = None

def load_saved_artifacts():
    global __model
    global __categorical_values
    print("Loading Artifacts...")
    __model = xgb.XGBRegressor()
    __model.load_model(MODEL_FILE_PATH)
    print('Model is',__model)
    
    __categorical_values = get_categorical_values()
    print("Loading Artifacts completed.")

def get_categorical_values():
    with open(UNIQUE_CATEGORICAL_VALUES_FILE_PATH, 'r') as fp:
        categorical_values = json.load(fp)
    return categorical_values


def get_estimated_price(brand_name, num_cores,
                        ram_capacity, internal_memory,
                        battery_capacity, fast_charging_available,
                        primary_camera_rear, primary_camera_front):
    response = None
    sample={'brand_name': brand_name,
        'num_cores': num_cores,
        'ram_capacity': ram_capacity,
        'internal_memory': internal_memory,
        'battery_capacity': battery_capacity,
        'fast_charging_available': fast_charging_available,
        'primary_camera_rear': primary_camera_rear,
        'primary_camera_front': primary_camera_front
        }

    sample= pd.Series(sample)


    sample_array = pd.DataFrame([sample], columns=sample.index )
    sample_array['brand_name'] = sample_array['brand_name'].astype('category')
    sample_array

    global __model
    if __model:
        response = round(__model.predict(sample_array)[0],2)
    return response


if __name__ == '__main__':
    load_saved_artifacts()
    price = get_estimated_price(brand_name='apple', num_cores=2,
                                 ram_capacity=2, internal_memory=128,
                                 battery_capacity=4000, fast_charging_available=False,
                                 primary_camera_rear=50,primary_camera_front=10)
    print(price)