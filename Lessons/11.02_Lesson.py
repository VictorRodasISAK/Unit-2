"""def from_decimal(num: int, base: int):
    result = ""
    while num > base:
        result = str(num % base) + result
        num = num // base
    result = str(num) + result
    return result


print(from_decimal(15, 3))"""

# Timer
import time

timer = int(input("Enter your time in seconds: "))
for x in range(timer, 0, -1):
    seconds = x % 60
    minutes = int((x / 60)) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
