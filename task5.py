def sum_str(my_str):
    my_sum = 0
    my_list = my_str.split()
    for i in my_list:
        my_sum += float(i)
    return my_sum

special_symbol = "&"
final_sum = 0


while True:
    a = input("Введите строку чисел: ")
    if a == special_symbol:
        break
    elif special_symbol in a:
        final_sum += sum_str(a[:a.find(special_symbol)])
        print(final_sum)
        break
    else:
        final_sum += sum_str(a)
        print(final_sum)
