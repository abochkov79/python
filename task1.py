host_name = "Александр"
host_age = 20
period = 30

print("Привет, меня зовут %s." %(host_name))
print("Мне %d лет." %(host_age))
print("Через {} лет мне будет {}.".format(period, host_age + period))
print()

user_name = input("Введите свое имя: ")
user_age = int(input("Введите возраст: "))

print(f"{user_name}, через {period} лет тебе будет {user_age + period}.")
