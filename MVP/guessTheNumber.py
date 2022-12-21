# Игра в угадывание чисел

import random

secretNumber = random.randint(1, 20)
print('Я загадал число от 1 до 20')

# Игроку дается 6 попыток

for guessesTaken in range(1, 7):
    print('Угадайте число.')
    guess = int(input())

    if guess < secretNumber:
        print('Я загадал большее число.')
    elif guess > secretNumber:
        print("Я загадал меньшее число.")
    else:
        break       # Число угадано

if guess == secretNumber:
    print('Отлично! Вы угадали! Количество попыток: ' + str (guessesTaken) + '.')
else:
    print('Вам не повезло. Я загадал другое число ' + str (secretNumber))
