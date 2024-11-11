import matplotlib.pyplot as plt

para1 = [(x/100+2)**2 for x in range(-600, 0, 4)]
para2 = [(x/100-2)**2 for x in range(0, 600, 4)]
ypara1 = [x/100 for x in range(-600, 0, 4)]
ypara2 = [x/100 for x in range(0, 600, 4)]
para3 = [-i for i in para1]
para4 = [-i for i in para2]

plt.plot(ypara1, para1, "red")
plt.plot(ypara2, para2, "blue")
plt.plot(ypara1, para3, "green")
plt.plot(ypara2, para4, "yellow")
plt.legend(['$x^2$-2','$x^2$+2','-$x^2$-2','-$x^2$+2'])
plt.xlim(-15, 15)
plt.show()