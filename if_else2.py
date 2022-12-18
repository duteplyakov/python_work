#Задание: Есть список пользователь, если введут admin,
# то приветствие для Админа, для остальных пользователей
# по списку свое приветствие, для тех кто не в списке другое.
usersAccess = ['admin', 'ivan', 'petr', 'viktor']
user = input('Enter user name:')

if "admin" in user:
    print("Привет Админ!")
elif user in usersAccess:
    print("Привет пользователь")
else:
    print("Привет странник")
