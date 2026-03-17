try:
    num_1 = float(input("Введите число: "))
    num_2 = float(input("Введите число: "))
    op = input("Введите операцию (+, -, /, *): ")
    if   op == "+":
        result = num_1 + num_2
    elif op == "-":
        result = num_1 - num_2
    elif op == "/":
        result = num_1 / num_2
    elif op == "*":
        result = num_1 * num_2
    else:
        print("Ошибка")
        result = None
    print(f"Результат:  {result}")
except ValueError:
    print("Ошибка: введено не число!")
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")
finally:
    print("Подсчет заверешен")
