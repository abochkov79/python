my_list = [9, 7, 4, 4, 3, 2]

number = float(input("Введите элемент рейтинга: "))

for i in range(len(my_list)):
    if number > my_list[i]:
        my_list.insert(i, number)
        break

if number not in my_list or number == my_list[len(my_list) - 1]:
    my_list.append(number)

print(my_list)
