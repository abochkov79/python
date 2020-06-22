original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [el for i, el in enumerate(original_list) if i > 0 and el > original_list[i - 1]]

print(original_list)
print(new_list)