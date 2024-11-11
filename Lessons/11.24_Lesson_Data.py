from Lesson_Library import get_sensor, smoothing
import matplotlib.pyplot as plt

sensor1 = get_sensor()
x,y = smoothing(x=sensor1)
plt.subplot(2,1,1)
plt.plot(sensor1)
plt.subplot(2,1,2)
plt.plot(x,y, color='r')
plt.show()