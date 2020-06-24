with open("text.txt", "w", encoding="utf-8") as my_file:
    while True:
        new_string = input("Введите строку для записи в файл, для окончания записи введите пустую строку: ")
        if new_string == "":
            break
        else:
            my_file.write(new_string + "\n")
