# Quiz 019
## Using the function that produces the table of Truth for 3 inputs, add a column for the boolean equation
### Python Code
```.py
def get_truth() -> str:
    message = "X | Y | Z | XY + (Not Y) + (Not (YZ))\n"
    val = [0, 1]
    for x in val:
        for y in val:
            for z in val:
                res = (x and y or (not y) or not (y and z))
                message += f"{x} | {y} | {z} | {str(int(res)).center(26)}\n"
    return message

print(get_truth())
```

### Proof
![Quiz_019_Proof_Image.png](Quiz_019_Proof_Image.png)

**Fig.1:** Proof of the Quiz 019

### Flow Chart
![Quiz_019_Flow_Chart.png](Quiz_019_Flow_Chart.png)

**Fig.2:** Flow Chart of the Quiz 019

### Work on paper
![Quiz_019_Work_Paper.jpeg](Quiz_019_Work_Paper.jpeg)

**Fig.3:** Work on paper of the Quiz 019

### Part B
![Quiz_019_Part_B.jpeg](Quiz_019_Part_B.jpeg)

**Fig.4:** Part B of the Quiz 019