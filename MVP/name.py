name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#пример1
fist_name = "Ada"
last_name = "lovelace"
age = 30+1
full_name = f"{fist_name} {last_name} {age}"
message = f"Hello,{full_name.title()}!"
print(message)

#пример2 с переходом строки
fist_name = "Ada"
last_name = "lovelace"
age = 30+1
full_name = f"{fist_name} \n{last_name} {age}"  #где \n указывает на переход сл строки
message = f"Hello,{full_name.title()}!"
print(message)

fist_name = input("Как твоё имя?")
last_name = input("Какая твоя фамилия")
age = int(input("Сколько тебе лет?"))
full_name = f"{fist_name} {last_name}, тебе {age}"
message = f"Привет, {full_name}!"
print(message)




