# House Prediction Flask Application
## Description
This project was carried out to deploy a gradient boost regression model trained on the Boston housing data.
The model was deployed on heroku using a flask application. The purpose of the model is to predict prices for houses in Boston.

## Getting Started
The app api can be found here - [House Prediction API](https://b-house-predic.herokuapp.com/).
To predict house prices using the app, send a post request [here]( https://b-house-predic.herokuapp.com/predict).
The predict endpoint takes only POST requests and request made to the endpoint should come with ```features```
as part of the request data. The endpoint can predict up to 2 prices per request.

## Usage
Post request should e made using a list with 13 numbers. 2 lists can also be passed into the request.

```python
import json

url = "https://b-house-predic.herokuapp.com/predict"
data = {"features": [3.67822, 0.0, 18.10, 0.0, 0.770, 5.362, 96.2, 2.1036, 24.0, 666.0, 20.2, 380.79, 10.19]}

post_data = json.dumps(data)
resp = requests.post(url, data=post_data)
print(resp.status_code, resp.content)
```
```python
import json

url = "https://b-house-predic.herokuapp.com/predict"
data = {"features": [[3.67822, 0.0, 18.10, 0.0, 0.770, 5.362, 96.2, 2.1036, 24.0, 666.0, 20.2, 380.79, 10.19],[1.27346, 0.0, 19.58, 1.0, 0.605, 6.250, 92.6, 1.7984, 5.0, 403.0, 14.7, 338.92, 5.50]]}

post_data = json.dumps(data)
resp = requests.post(url, data=post_data)
print(resp.status_code, resp.content)
```

## License
The MIT License - Copyright (c) 2021 - Blessing Ehizojie-Philips