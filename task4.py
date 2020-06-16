my_string = input("Введите несколько слов, разделенных пробелами: ")

my_list = my_string.split()

for ind, el in enumerate(my_list):
     print(ind + 1, el[:10])