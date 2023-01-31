print("Простой калькулято!"
      "\nДелить на ноль нельзя")
while True:
    w = input("Введите знак операции (+,-,*,/): ")
    if w == '0':
        break
    if w in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if w == '+':
            print("%.f" % (x+y))
        elif w == '-':
            print("%.f" % (x-y))
        elif w == '*':
            print("%.f" % (x*y))
        elif w == '/':
            if y != 0:
                print("%.f" % (x/y))
            else:
                print("Деление на ноль ЗАПРЕЩЕНО!")
    else:
        print("Неверный знак операции!")