from sys import argv

def compensation(time, rate, bonus):
    try:
        return(float(time) * float(rate) + float(bonus))
    except:
        return("Выработка в часах, ставка в час и премия должны быть указаны в виде положительных чисел.")

script_name, working_time, rate_per_hour, bonus = argv
print(f"Выработка в часах: {working_time}")
print(f"Ставка в час: {rate_per_hour}")
print(f"Премия: {bonus}")

print(f"Заработная плата сотрудника: {compensation(working_time, rate_per_hour, bonus)}")