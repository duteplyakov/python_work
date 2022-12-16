


#Делаю доступ по возрасту, возраст боьше или расно 30 лет

fist_name = input("Как твоё имя?")
last_name = input("Какая твоя фамилия")
age = int(input("Сколько тебе лет?"))
full_name = f"{fist_name} {last_name}, твой возраст {age}"
message = f"Привет, {full_name}!"
if (age >= 30) :
    print(f"Привет {full_name} лет, \n Доступ разрешен!")
else:
    print(f"Привет {full_name} лет, \n Доступ запрещен!!!")
