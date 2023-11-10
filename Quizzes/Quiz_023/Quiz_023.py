import matplotlib.pyplot as plt
def produce():
    x_out = []
    y_out = []
    for n in range(-10,11):
        x_out.append(n)
        y_out.append(abs(n))
    return y_out, x_out

plt.style.use('ggplot')
y, x = produce()
plt.plot(x, y, color='r')
plt.xlabel("Interval", fontsize=20)
plt.ylabel("$f(x) = |x|$", fontsize = 20)
plt.show()