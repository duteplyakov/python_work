alien_color = ['green', 'yellow', 'red']

if 'green' in alien_color:
    print ("Ты заработал 5 очков")

# другой вариант
alien_color = ['green', 'yellow', 'red']
color = 'green'
if color not in alien_color:
    print (f"{color.title()}, Ты заработал 5 очков" )

#условие выполняется True

alien_color = ['green', 'yellow', 'red']

if 'black' in alien_color:
    print()


# с переменной if и else

alien_color = ['green', 'yellow', 'red']
color = "green"
if "green" in color:
    print("Ты заработал 5 очков")
elif "yellow" in color:
    print("Ты заработал 10 очков")
elif "red" in color:
    print("Ты заработал 15 очков")
else:
    print("Ты заработал 20 очков")

#
alien_color = ['green', 'yellow', 'red']
color = "yellow"
if "green" in color:
    print("Ты заработал 5 очков")
elif "yellow" in color:
    print("Ты заработал 10 очков")
elif "red" in color:
    print("Ты заработал 15 очков")
else:
    print("Ты заработал 20 очков")

#
alien_color = ['green', 'yellow', 'red']
color = "red"
if "green" in color:
    print("Ты заработал 5 очков")
elif "yellow" in color:
    print("Ты заработал 10 очков")
elif "red" in color:
    print("Ты заработал 15 очков")
else:
    print("Ты заработал 20 очков")

#
alien_color = ['green', 'yellow', 'red']
color = "black"
if "green" in color:
    print("Ты заработал 5 очков")
elif "yellow" in color:
    print("Ты заработал 10 очков")
elif "red" in color:
    print("Ты заработал 15 очков")
else:
    print("Ты заработал 20 очков")

#
alien_color = ['green', 'yellow', 'red']
color = input("Введи цвет:")
if "green" in color:
    print("Ты заработал 5 очков")
elif "yellow" in color:
    print("Ты заработал 10 очков")
elif "red" in color:
    print("Ты заработал 15 очков")
else:
    print("Ты заработал 20 очков")