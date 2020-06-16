my_list = [10, "Bird", 89.3, (5, "Elephant", False), {'Name': 'Mike', 'Age': '31'}, set("Moscow"),
           frozenset("Computer"), b'Future', bytearray(b"Tomorrow"), None, True, [4, "Monkey"]]

print("%-9s%-63s%-20s" % ("Индекс", "Значение элемента", "Тип элемента"))
for my_element in my_list:
    print(f"{my_list.index(my_element):<8} {str(my_element):<60}   {str(type(my_element)):<20}")
