def my_func(number_1, number_2, number_3):
    my_sum = number_1 + number_2 + number_3
    my_sum = my_sum - min(number_1, number_2, number_3)
    return my_sum


print(f"Сумма двух наибольших чисел: {my_func(3, 7, 2)}")