import configuration
import requests


def create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                         json=body)


def get_track(params):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS_PATH,
                        params=params)


# Хохлов Кирилл, 8а когорта — Финальный проект. Инженер по тестированию плюс