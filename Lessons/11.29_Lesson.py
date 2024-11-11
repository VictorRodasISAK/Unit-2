from matplotlib.gridspec import GridSpec

from Lesson_Library import get_sensor
import matplotlib.pyplot as plt
import matplotlib

plt.style.use('ggplot')
matplotlib.use('MacOSX')

#Step 1 get sensors
sensors = []
for s in [0, 1, 2, 3]:
    data = get_sensor(id=s)
    sensors.append(data)
    print(f"Sensors {s} with {len(data)}")

num_samples = len(sensors[1])
average = []
for i in range(num_samples):
    total = 0
    for n in sensors:
        total += n[i]
    average.append(total/len(sensors))

fig = plt.figure(figsize=(10, 8))
grid = GridSpec(3, 3, figure=fig)

box1 = fig.add_subplot(grid[0:2, 0:2])
plt.plot(average, color='red')
plt.title("Average of all sensors")

box2 = fig.add_subplot(grid[0, 2])
plt.subplots_adjust(hspace=0.5)
plt.plot(sensors[0], color="black")
plt.title("Sensor id = 1")

box3 = fig.add_subplot(grid[1, 2])
plt.subplots_adjust(hspace=0.5)
plt.plot(sensors[1], color="green")
plt.title("Sensor id = 2")

box4 = fig.add_subplot(grid[2, 0])
plt.subplots_adjust(hspace=0.5)
plt.plot(sensors[2], color="purple")
plt.title("Sensor id = 3")

box5 = fig.add_subplot(grid[2, 1])
plt.subplots_adjust(hspace=0.5)
plt.plot(sensors[3], color="yellow")
plt.title("Sensor id = 4")
plt.show()