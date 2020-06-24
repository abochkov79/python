my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("text_4.txt", "r", encoding="utf-8") as my_file:
    with open("text_4_translate.txt", "w", encoding="utf-8") as new_file:
        for line in my_file:
            new_file.write(my_dict.get(line[:line.find(" ")])+line[line.find(" "):])



