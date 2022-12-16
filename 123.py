login = input('Введи логин')

message = f"Привет, {login}!"
f = open("name.txt", "r")

with open("name.txt", "rt") as file:
    print("GOOD" if f"{login}" in file.read() else "BAD")
