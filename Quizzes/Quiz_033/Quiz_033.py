import matplotlib.pyplot as plt

temp = -2
x = []
y = []
for _ in range(100):
    x.append(temp)
    y.append(temp**2)
    temp += 0.04
y_neg = [-i for i in y]
plt.plot(x, y, "red")
plt.plot(x, y_neg,"plum")
plt.plot(y, x, "blue")
plt.plot(y_neg, x, "green")
plt.show()