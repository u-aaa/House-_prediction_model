import pickle
import json
import numpy as np
from flask import Flask, request, jsonify


app = Flask(__name__)


with open('models/regressor.pkl', 'rb') as f:
    model = pickle.load(f)


def __process_input(posted_data) -> np.array:
    try:
        data_str = json.loads(posted_data)
        data_list = data_str['features']
        data_item = np.array(data_list)
        dimensions = data_item.ndim
        if dimensions > 2:
            return None
        if len(data_item.shape) == 1: #checks if array is 1D
            data_item = data_item.reshape(1, -1)
        arr_len = data_item.shape[-1]
        if arr_len == 13:
            return data_item
        return None
    except (KeyError, json.JSONDecodeError, AssertionError):
        return None


@app.route('/')
def index() -> str:
    return 'Welcome to the house prediction interface', 200


@app.route('/predict', methods=['POST'])
def predict() -> (str, int):
    try:
        data_str = request.data
        predict_params = __process_input(data_str)
        if predict_params is not None:
            prediction = model.predict(predict_params)
            return json.dumps({'predicted house price(s) (in dollars)': prediction.tolist()}), 200
        return json.dumps({'Error': 'Invalid input'}), 400
    except (KeyError, json.JSONDecodeError, AssertionError):
        return json.dumps({'Error': 'Unable to predict'}), 500


if __name__ == '__main__':
    app.run()
