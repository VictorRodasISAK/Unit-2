def count_letters(dictionary: dict, msg: str):
    for letter in msg:
        if letter in dictionary:
            dictionary[letter] += 1
    return dictionary


dictionary = {
    'w': 0,
    'l': 0,
    'o': 0
}

print(count_letters(dictionary=dictionary, msg='hello world'))
