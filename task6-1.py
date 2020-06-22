from itertools import count

start_number = 50
stop_number = 100

for el in count(start_number):
    if el > stop_number:
        break
    else:
        print(el)

