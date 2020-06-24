my_dict = {}

with open("text_6.txt", "r", encoding="utf-8") as my_file:
    my_data = my_file.readlines()

for my_str in my_data:
    my_record = my_str.split()
    num_lessons = 0
    for j in range(1,len(my_record)):
        if my_record[j] != "-":
            num_lessons += int(my_record[j][0:my_record[j].find("(")])
    my_dict[my_record[0]] = num_lessons


print(my_dict)
