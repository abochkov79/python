def my_division(dividend, denominator):
    return dividend / denominator

number_1 = float(input("Введите делимое: "))
number_2 = float(input("Введите делитель: "))

try:
    result = my_division(number_1, number_2)
    print(f"Результат деления: {result:.2f}")
except ZeroDivisionError:
    print("Ошибка! Произошло деление на ноль.")


