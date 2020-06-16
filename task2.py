my_list = []

while True:
    my_list.append(input("Введите значение списка: "))
    if input("Добавите еще один элемент в список (да/нет)? ") != "да":
        break

for i in range(len(my_list)):
    if i % 2 == 0:
        new_list = my_list[i:i + 2]
        new_list.reverse()
        my_list[i:i + 2] = new_list

print(my_list)
