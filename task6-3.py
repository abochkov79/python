from itertools import count, cycle

original_list = ["A", "B", "C", 66, True, -23.4, "CAT"]
start_number = 50
number_iterations = 20

my_set = count(start_number)
my_cycle = cycle(original_list)

for i in range(number_iterations):
    print(next(my_set))

for i in range(number_iterations):
    print(next(my_cycle))
