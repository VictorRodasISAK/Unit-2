import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

heart_rate = []
with open("11.15_Lesson_Data.csv", "r") as f:
    header = f.readline()
    data = f.readlines()
print(header)

time = []
t = 0
for d in data:
    s1, s2, s3 = d.strip().split(',')
    heart_rate.append([int(s1), int(s2), int(s3)])
    time.append(t)
    t += 1

mean = []
std = []
min_hr = []
max_hr = []
for v in heart_rate:
    mean.append(np.mean(v))
    std.append(np.std(v))
    min_hr.append(np.min(v))
    max_hr.append(np.max(v))

plt.errorbar(time, mean, std, fmt="o", color="#023047")
plt.xlabel("Time(hours)")
plt.ylabel("Heart Rate(Pulses per minute)")
plt.fill_between(time, max_hr, min_hr, alpha=0.5, linewidth=0, color="#8ecae6")
plt.show()