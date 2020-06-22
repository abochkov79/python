def fact(n):
    for el in range(n):
        yield el + 1

n = 6


my_list = [el for el in fact(n)]
my_fact = 1

for i in my_list:
    my_fact *= i
    print(f"{i}! = {my_fact}")




