def my_func(x, y):
    return x ** y

def my_func2(x, y):
    my_result = 1
    while y < 0:
        my_result = my_result / x
        y += 1
    return my_result


number_1 = float(input("Введите действительное положительное число (x): "))
while number_1 <= 0:
    number_1 = float(input("Число должно быть действительным положительным. Введите повторно: "))

"""Обработка исключения - число не целое"""
try:
    number_2 = int(input("Введите целое отрицательное число (y): "))
    while number_2 >= 0:
        number_2 = int(input("Число должно быть целое отрицательное. Введите повторно: "))
except ValueError:
        number_2 = int(input("Число должно быть ЦЕЛОЕ отрицательное. Введите повторно: "))

print(f"Вариант решения через '**'. Результат возведения числа x в степень y = {my_func(number_1, number_2):.3f}")
print(f"Вариант решения через функцию. Результат возведения числа x в степень y = {my_func2(number_1, number_2):.3f}")