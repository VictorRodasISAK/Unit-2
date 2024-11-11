def sort_dict(in_dict:dict):
    x = []
    y = []
    for key, values in in_dict.items():
        x.append(values)
        y.append(key)
    return {x, y}