from Quiz_029_Library import get_sensor, smoothing
import matplotlib.pyplot as plt

sensor1 = get_sensor(id=2)
x, y = smoothing(x=sensor1, overlap=0.5)
plt.subplot(2, 1, 1)
plt.plot(sensor1)
plt.subplot(2, 1, 2)
plt.plot(x, y, color='r')
plt.show()