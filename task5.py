revenue = int(input("Введите выручку фирмы: "))
cost = int(input("Введите издержки фирмы: "))
print()

profit = revenue - cost

if profit > 0:
    print("Фирма получила прибыль в размере:", profit)
    print("Рентабельность выручки составила: {:.2f}".format(profit / revenue))
    print()
    staff = int(input("Введите численность сотрудников фирмы: "))
    print("Прибыль фирмы в расчете на одного сотрудника: {:.1f}".format(profit / staff))
elif profit < 0:
    print("Фирма получила убыток в размере:", profit)
else:
    print('Фирма отработала "в ноль".')