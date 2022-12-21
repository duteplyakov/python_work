#Делаю доступ по возрасту, возраст боьше или равно 30 лет
#возраст определяется: текущий год - дата рождения


fist_name = input("Как твоё имя?")
last_name = input("Какая твоя фамилия")
age = int(input("Введи свой год рождения?"))

#текущий год
import datetime
now = datetime.datetime.now()
now1 = now.year - age

#определения возраста
full_name = f"{fist_name} {last_name}, твой возраст {now1}"

#итог

message = f"Привет, {full_name}!"
f = open("out.txt", "a") #открываю и создаю файл для записи вывода

if (now1 >= 30) :
    print(f"Привет {full_name} лет, \n Доступ разрешен!")

else:
    print(f"Привет {full_name} лет, \n Доступ запрещен!", file=f) #добавлен file=f для вывода в файл out.txt


f.close()
