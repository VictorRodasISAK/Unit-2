# Quiz 022
## Create a program shows the graph of the parabola for 100 values of x in the interval -10 < x < 10  
### Python Code
```.pycon
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
```

### Proof
![Quiz_022_Proof_Image.png](Quiz_022_Proof_Image.png)

**Fig.1:** Proof of the Quiz 022

### Flow Chart
![Quiz_022_Flow_Chart.png](Quiz_022_Flow_Chart.png)

**Fig.2:** Flow Chart of the Quiz 022

### Work on paper
![Quiz_022_Work_Paper.jpeg](Quiz_022_Work_Paper.jpeg)

**Fig.3:** Work on paper of the Quiz 022

### Part B
![Quiz_022_Part_B.jpeg](Quiz_022_Part_B.jpeg)

**Fig.4:** Part B of the Quiz 022