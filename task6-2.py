from itertools import cycle

original_list = ["A", "B", "C", 66, True, -23.4, "CAT"]

i = 0
for el in cycle(original_list):
    if i > 20:
        break
    print(el)
    i += 1
