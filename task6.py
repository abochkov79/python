my_list = []
my_dict = {}
new_element = []

i = 1
while True:
    good = input("Введите название товара: ")
    price = int(input("Введите цену товара: "))
    while price < 0:
        price = int(input("Цена товара должна быть положительной величиной: "))
    quantity = int(input("Введите количество товара: "))
    while quantity < 0:
        quantity = int(input("Количество товара должно быть положительной целой величиной: "))
    measure = input("Введите единицы измерения товара: ")
    my_list.append(tuple([i, dict(название=good, цена=price, количество=quantity, ед=measure)]))

    answer = input("Вы хотите добавить еще один товар (да/нет)? ")
    if answer != "да":
        break
    else:
        i = i + 1

print("\nСтруктура данных:\n")
print(my_list)

my_keys = list(my_list[0][1].keys())

for i in range(len(my_keys)):
    new_list = []
    for j in range(len(my_list)):
        new_element = my_list[j][1].get(my_keys[i])
        if new_element not in new_list: new_list.append(new_element)
    my_dict[my_keys[i]] = new_list

print("\nАналитика о товарах:\n")
print(my_dict)
