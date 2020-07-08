class EnteredString(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
is_digit = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "-")
while True:
    try:
        my_str = input("Введите число для добавления в список: ")
        if my_str == "stop":
            break
        for s in my_str:
            if s not in is_digit:
                raise (EnteredString("Вы ввели строку!!! Необходимо вводить числа."))
        if my_str.count(".") > 1 or my_str.count("-") > 1 or (my_str.find("-") != 0 and my_str.find("-") != -1):
            raise (EnteredString("Вы ввели строку!!! Необходимо вводить числа."))

    except EnteredString as err:
        print(err)
    else:
        my_list.append(float(my_str))

print(my_list)
