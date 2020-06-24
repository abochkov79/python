with open("text.txt", "r", encoding="utf-8") as my_file:
    my_list = my_file.readlines()
    print("Всего строк в файле: ", len(my_list))
    for i, s in enumerate(my_list):
        print(f"В строке {i+1} количество слов: {len(s.split())}")