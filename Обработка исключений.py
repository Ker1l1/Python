try:
    number = int(input("Введите число: "))
    age = int(input("Введите число: "))
    result = number / age
except ValueError:
    print("Ошибка: введено не число!")
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")
else:
    print(f"Результат: {result}")
finally:
    print("Программа завершена")