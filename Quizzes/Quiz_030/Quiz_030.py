import requests, numpy as np
from matplotlib import pyplot as plt


def get_sensor(id: int = 2, ip: str = "192.168.6.153"):
    request = requests.get(f'http://{ip}/readings')
    data = request.json()
    sensors = data['readings'][0]
    sensor = []
    for s in sensors:
        if s['sensor_id'] == id:
            sensor.append(s['value'])
    return sensor


def smoothing(x: list[int], size_window: int = 5):
    smooth_x = []
    t = []
    for i in range(0, len(x), size_window):
        points = sum(x[i:i + size_window]) / size_window
        smooth_x.append(points)
        t.append(i)

    return t, smooth_x

def quadratic(x, a, b, c):
    return a*x**2 + b*x + c

sensor1 = get_sensor()
x, y = smoothing(x=sensor1)
a, b, c = np.polyfit(x[40:80], y[40:80], 2)
y_quadratic = quadratic(np.array(x[40:80]), a, b, c)
print(f"{a:.4f}x^2 + {b:.4f}x + {c:.4f}")

plt.plot(x[40:80], y[40:80], color='r')
plt.plot(x[40:80], y_quadratic, linestyle='--', color='black')
plt.title(f'{a:.4f}x$^2$ + {b:.4f}x + {c:.4f}')
plt.show()