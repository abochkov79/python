from functools import reduce

def my_func(prev_el, el):
    return prev_el * el

my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(my_func, my_list))