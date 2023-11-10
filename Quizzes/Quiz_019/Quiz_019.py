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