# Quiz 018
## Create a function that produces the table of Truth for 3 inputs:
### Python code
```.py
def get_truth() -> str:
    message = "A | B | C\n"
    input = [0, 1]
    for x in input:
        for y in input:
            for z in input:
                message += f"{x} | {y} | {z}\n"
    return message

print(get_truth())
```

### Proof
![Quiz_018_Proof_Image.png](Quiz_018_Proof_Image.png)

**Fig.1:** Proof of the Quiz 018

### Flow Chart
![Quiz_018_Flow_Chart.png](Quiz_018_Flow_Chart.png)

**Fig.2:** Flow Chart of the Quiz 018

### Work on paper
![Quiz_018_Work_Paper.jpeg](Quiz_018_Work_Paper.jpeg)

**Fig.3:** Work on paper of the Quiz 018

### Part B
![Quiz_018_Part_B.jpeg](Quiz_018_Part_B.jpeg)

**Fig.4:** Part B of the Quiz 018