def int_func(my_word):
    result_str = None
    for i in my_word:
        if ord(i) < ord("a") or ord(i) > ord("z"):
            result_str = "Слово должно состоять только из маленьких латинских букв!!!"
    if result_str == None:
        result_str = my_word.capitalize()
    return result_str

a = input("Введите слово, состоящее из маленьких латинских букв: ")
print(int_func(a))