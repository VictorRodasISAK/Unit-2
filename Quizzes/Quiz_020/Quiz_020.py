import random

random.seed(1234)


def produce(n: int, m: int, s: int):
    message = "| x  |  y(x)  |\n"
    for num in range(n):
        x = random.randint(0, 100)
        res = round(x ** ((1/2) * ((m / s) ** 2)), 2)
        message += f"| {str(x).center(2)} | {str(res).center(6)} |\n"
    return message

print(produce(n=5, m=3, s=2))
