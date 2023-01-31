message = f"Привет, {full_name}!"
f = open("name.txt", "r") #подгружаем файл с именами

with open("name.txt", "rt") as file: #проверка сперва по фамилии , потом по возрасту
    print(f"Отлично, вы: {full_name}, доступ разрешен!" if f"{last_name}" in file.read() and f"{now1}" >= "30"
          else "В доступе отказано!!!")
