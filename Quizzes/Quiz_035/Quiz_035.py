import matplotlib.pyplot as plt

temp = 0
x = []
y = []
para = []
for _ in range(50):
    x.append(temp)
    y.append(temp)
    temp += 0.02

tempo = 0
for _ in range(-2, 3):
    para.append(-tempo**2 + 2)
    tempo += 0.02

x_neg = [-i for i in x]
plt.plot(x, y, "red")
plt.plot(x_neg, y, "green")
plt.plot(x, para, "black")
plt.show()