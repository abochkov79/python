months_list = ["зима", "зима", "весна", "весна", "весна", "лето", "лето", "лето", "осень", "осень", "осень", "зима"]
months_dic = {1: "зима", 2: "зима", 3: "весна", 4: "весна", 5: "весна", 6: "лето", 7: "лето", 8: "лето", 9: "осень", 10: "осень", 11: "осень", 12: "зима"}

month_number = int(input("Введите номер месяца: "))

while month_number < 1 or month_number > 12:
    print()
    print("Номер месяца должен быть от 1 до 12")
    month_number = int(input("Введите номер месяца: "))


# Проверка через list
print("Проверяем по списку. Этот месяц относится ко времени года:", months_list[month_number-1])

# Проверка через dict
print("Проверяем по словарю. Этот месяц относится ко времени года:", months_dic[month_number])