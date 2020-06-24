with open("text_3.txt", "r", encoding="utf-8") as my_file:
    my_list = my_file.readlines()
    salary_limit = 20000
    salary_total = 0
    for i in my_list:
        salary = float(i.split()[1])
        salary_total += salary
        if salary < salary_limit:
            print(i.split()[0])
    print(f"Средняя величина дохода сотрудников: {salary_total/len(my_list):.2f}")