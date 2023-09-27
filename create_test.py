import configuration
import requests
import data
import sender_stand_request
# Мария Иванова, 1-я когорта — Финальный проект. Инженер по тестированию плюс

def positive_assert(track):
    request = sender_stand_request.create_new_order(data.order_body)
    track_number = request.json()['track']
    print(track_number)
    params = data.get_track.copy()
    params['t'] = track
    request = sender_stand_request.get_track(params)
    assert request.status_code == 200

request = sender_stand_request.create_new_order(data.order_body)
track_number = request.json()['track']
print(track_number)


def test_status_code():
    positive_assert(track_number)