import json
from app import __process_input


def test_home(app, client):
    response = client.get('/')
    assert response.status_code == 200
    expected = 'Welcome to the house prediction interface'
    assert expected == response.get_data(as_text=True)

def test_process_input():
    data = json.dumps(
        {"features": [3.67822, 0.0, 18.10, 0.0, 0.770, 5.362, 96.2, 2.1036, 24.0, 666.0, 20.2, 380.79, 10.19]})
    result = __process_input(data)
    assert hasattr(result, '__array__')

def test_predict(app, client):
    data = json.dumps(
        {"features": [3.67822, 0.0, 18.10, 0.0, 0.770, 5.362, 96.2, 2.1036, 24.0, 666.0, 20.2, 380.79, 10.19]})
    response = client.post('/predict', data=data)
    assert response.status_code == 200
    expected = {"predicted house price(s) (in dollars)": [20.43914910916915]}
    assert expected == json.loads(response.get_data())

def test_predict2(app, client):
    data = json.dumps(
        {"features":
            [[3.67822, 0.0, 18.10, 0.0, 0.770, 5.362, 96.2, 2.1036, 24.0, 666.0, 20.2, 380.79, 10.19],
             [1.27346, 0.0, 19.58, 1.0, 0.605, 6.250, 92.6, 1.7984, 5.0, 403.0, 14.7, 338.92, 5.50]]})
    response = client.post('/predict', data=data)
    assert response.status_code == 200
    expected = {"predicted house price(s) (in dollars)": [20.43914910916915, 25.663303706451064]}
    assert expected == json.loads(response.get_data())


