import requests

user = {
    'username': 'daniel',
    'password': '12345'
}

ip = "192.168.6.153"

answer = requests.post(f'http://{ip}/register', json=user)
print(answer.json())

answer = requests.post(f'http://{ip}/login', json=user)
print(answer.json())
cookie = answer.json()['access_token']

sensor_a = {
    'type': 'Temperature',
    'location': 'Asama 25',
    'name': 'daniel_temp_1',
    'unit': 'C'
}
header = {
    'Authorization':f'Bearer {cookie}'
}
answer = requests.post(f'http://{ip}/sensor/new', json=sensor_a, headers=header)

print(answer.json())

record = {
    'sensor_id': 20,
    'value': 30
}
answer = requests.post(f'http://{ip}/reading/new', json=record, headers=header)

print(answer.json())

answer = requests.get(f'http://{ip}/sensors', headers=header)
print(answer.json())