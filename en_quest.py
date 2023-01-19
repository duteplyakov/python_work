# Приветвуем пользователя

print('Привет! Предлагаю проверить свои знания английского!'
      'Расскажи как тебя зовут!')
name = input('Введи своё имя: ')
print(f'Привет, {name}, начинаем тренировку!')

# Счетчик ответов
correct_answers = 0

# Начинаем задавать вопросы
# Первый вопрос

first_question = f'My name ____ {name}\n'
first_answer = 'is'
user_answer = input(first_question)
if user_answer == first_answer:
    print('Ответ верный!\nВы получаете 10 баллов!')
    correct_answers += 1
else:
    print(f'Неправильно. Правильный ответ {first_answer}')

# Второй вопрос

second_question = 'I ____a schoolboy!\n'
second_answer = 'am'
user_answer = input(second_question)
if user_answer == second_answer:
    print('Ответ верный!\nВы получаете 10 баллов!')
    correct_answers += 1
else:
    print(f'Неправильно. Правильный ответ {second_answer}')

# Третий вопрос

third_question = 'I live ____Bataysk!\n'
third_answer = 'in'
user_answer = input(third_question)
if user_answer == third_answer:
    print('Ответ верный!\nВы получаете 10 баллов!\n')
    correct_answers += 1
else:
    print(f'Неправильно. Правильный ответ {third_answer}\n')

# Колличество баллов пользователя
user_score = correct_answers *10
# Колличество процентов
user_percentage = round((correct_answers / 3) * 100)
print(

    f'Вот и всё, {name}!\n'
    f'Вы ответили на {correct_answers} вопрос из 3 верно.\n'
    f'Вы заработали  {user_score} баллов.\n'
    f'Это {user_percentage} процентов.'
)


# for num in range (10):
#     result = 2 ** num
#     print(f'{result}')