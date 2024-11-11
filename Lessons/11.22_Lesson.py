#api_part1

import requests, matplotlib.pyplot as plt

ip_server = "192.168.6.153"

data = requests.get(f'http://{ip_server}/readings')
data = data.json()

x = data['readings'][0]

my_sensors = {
    1: [],
    2: []
}

for record in x:
    id_sensor = record['sensor_id']
    if id_sensor in my_sensors:
        value = record['value']
        my_sensors[id_sensor].append(value)

print(my_sensors)

fig = plt.Figure(figsize=(10, 8))
plt.subplots_adjust(hspace=0.5)
plt.subplot(2, 1, 1) #rows, columns, id
plt.plot(my_sensors[1], color='red')
plt.title("Sensor Outside")
plt.subplot(2, 1, 2)
plt.plot(my_sensors[2], color='black')
plt.title("Sensor Inside")

plt.show()
