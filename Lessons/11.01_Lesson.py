def base2dec(base,num):
    index = 0
    sum = 0
    while num > 0:
        d = num % 10
        b = base ** index
        sum += d * b
        num = num // 10
        index += 1
    return sum

print(base2dec(4,2023))