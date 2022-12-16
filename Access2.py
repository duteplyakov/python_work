#Делаю доступ по фамилии и возрасту, возраст боьше или равно 30 лет
#возраст определяется: текущий год - дата рождения
#фамилии в файле name.txt


first_name = input("Как твоё имя?")
last_name = input("Какая твоя фамилия")
age = int(input("Введи свой год рождения?"))

#текущий год
import datetime
now = datetime.datetime.now()
now1 = now.year - age

#определения возраста
full_name = f"{first_name} {last_name}, твой возраст {now1}"

#итог

message = f"Привет, {full_name}!"
f = open("name.txt", "r") #подгружаем файл с именами

with open("name.txt", "rt") as file: #проверка сперва по фамилии , потом по возрасту
    print(f"Отлично, вы: {full_name}, доступ разрешен!" if f"{last_name}" in file.read() and f"{now1}" >= "30"
          else "В доступе отказано!")



