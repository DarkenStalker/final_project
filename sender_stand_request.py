import configuration
import requests
import data

def post_new_order(track_number):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=track_number)
response = post_new_order(data.order_body);
print(response.status_code)
print(response.json())
track_number = str(response.json())
track_number = track_number[10:16]
print(track_number)

def get_order():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + str(track_number))
response = get_order();
print(response.status_code)
