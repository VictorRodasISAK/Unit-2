def get_let(msg: str) -> str:
    message = ""
    let_change = {
        "a": "4",
        "e": "3",
        "i": "1",
        "o": "0",
        " ": "_"
    }
    for letter in msg:
        if letter.lower() in let_change:
            message += let_change[letter.lower()]
        else:
            message += letter

    return message

print(get_let("Hello World"))