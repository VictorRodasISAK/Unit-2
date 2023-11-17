student = {
    "name": "bob", 18: True, "music": ['rock', 'classic'],
    "email": {"home": "bob@home", "work": "work@home"}
}

for key, value in student.items():
    print(f"The key is {key} with value {value}")

print(student["email"]["work"])

if "address" in student:
    print(student["address"])
else:
    student["address"] = ""
