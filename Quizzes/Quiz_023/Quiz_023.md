# Quiz 023
## Create a program shows the graph of the function below for 100 values of x in the interval -10 < x < 10
### Python Code
```.py
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
plt.ylabel("$f(x) = |x|$", fontsize=20)
plt.show()
```

### Proof
![Quiz_023_Proof_Image.png](Quiz_023_Proof_Image.png)

**Fig.1:** Proof of the Quiz 023

### Flow Chart
![Quiz_023_Flow_Chart.png](Quiz_023_Flow_Chart.png)

**Fig.2:** Flow Chart of the Quiz 023

### Part B
![Quiz_023_Part_B.jpeg](Quiz_023_Part_B.jpeg)

**Fig.3:** Part B of the Quiz 023