from random import random

my_numbers = []

with open("text_5.txt", "w", encoding="utf-8") as my_file:
    for i in range(10):
        my_file.write(f"{random()*100:.2f} ")


with open("text_5.txt", "r", encoding="utf-8") as num_file:
    my_sum = 0
    my_numbers = num_file.readline().split()
    for n in my_numbers:
        my_sum += float(n)
    print(f"Сумма чисел в файле: {my_sum:.2f}")