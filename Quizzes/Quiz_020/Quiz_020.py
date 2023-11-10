import random

random.seed(1234)


def produce(n: int, m: int, s: int):
    message = "| x  |  y(x)  |\n"
    for num in range(n):
        x = random.randint(0, 100)
        res = (1/2) * ((m / s) ** 2)
        resf = x ** res
        res_fi = str(round(resf, 2)).center(6)
        message += f"| {str(x).center(2)} | {res_fi} |\n"
    return message

print(produce(n=5, m=3, s=2))
