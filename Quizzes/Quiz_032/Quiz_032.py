from matplotlib.gridspec import GridSpec

from Quiz_032_Library import get_sensor
import matplotlib.pyplot as plt
import matplotlib

plt.style.use('ggplot')
matplotlib.use('MacOSX')

sensors = []
for s in [4, 5]:
    data = get_sensor(id=s)
    sensors.append(data)

print(sensors[0])

num_samples = len(sensors[1])
average = []
for i in range(num_samples):
    total = 0
    for n in sensors:
        total += n[i]
    average.append(-total/len(sensors))

fig = plt.figure(figsize=(10, 5))
grid = GridSpec(3, 4, figure=fig)

box1 = fig.add_subplot(grid[0:3, 1:3])
plt.plot(average, color='red')
plt.title("Sensor#4 - Sensor#5")

box2 = fig.add_subplot(grid[1, 0])
plt.ylim(0, 100)
plt.xlim(0, 800)
plt.subplots_adjust(hspace=0.5)
plt.plot(sensors[0], color="black")
plt.title("Sensor id = 4")

box3 = fig.add_subplot(grid[1, 3])
plt.ylim(0, 100)
plt.xlim(0, 800)
plt.subplots_adjust(hspace=0.5)
plt.plot(sensors[1], color="green")
plt.title("Sensor id = 5")
plt.show()