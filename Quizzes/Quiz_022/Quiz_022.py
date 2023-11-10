import matplotlib.pyplot as plt
def produce():
    x_out = []
    y_out = []
    for n in range(-10,11):
        x_out.append(n)
        res = 2*((n+5)**2)
        y_out.append(res)
    return y_out, x_out

plt.style.use('ggplot')
y, x = produce()
plt.plot(x, y, color='r')
plt.xlabel("Interval", fontsize=20)
plt.ylabel("$f(x) = 2(x + 5)^{2}$", fontsize = 20)
plt.show()
