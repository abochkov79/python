distance = float(input("Введите дистанцию пробежки в км в первый день: "))
while distance <= 0:
    print()
    distance = float(input("Значение должно быть больше 0.\nВведите дистанцию пробежки в км в первый день: "))

target = float(input("Введите цель в км: "))
while target <= distance:
    print()
    target = float(input("Значение должно быть положительным числом и превышать дистанцию пробежки в первый день.\nВведите цель в км: "))

day = 2

while True:
    distance = distance * 1.1
    if distance >= target:
        break
    else:
        day += 1

print("На {}-й день спортсмен достиг результата.".format(day))

