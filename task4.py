number = int(input("Введите целое положительное число: "))

max_number = number % 10

while number > 0:
    if max_number == 9:
        break
    elif max_number < number % 10:
        max_number = number % 10
    number = number // 10

print("Самая большая цифра в введенном числе:", max_number)
