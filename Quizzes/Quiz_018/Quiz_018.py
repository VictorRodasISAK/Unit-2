def get_truth() -> str:
    message = "A | B | C\n"
    input = [0, 1]
    for x in input:
        for y in input:
            for z in input:
                message += f"{x} | {y} | {z}\n"
    return message

print(get_truth())
