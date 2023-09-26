import requests

import configutation

import data

def post_new_user(body):
    return requests.post(configutation.URL_SERVICE+configutation.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())


def get_users_table():
    return requests.get(configutation.URL_SERVICE + configutation.USERS_TABLE_PATH)


response = get_users_table()
print(response.status_code)
