import json

my_list = []
profit_list = {}
average_profit = {}
total_profit = 0
profitable = 0

with open("text_7.txt", "r", encoding="utf-8") as my_file:
    for line in my_file:
        my_record = line.split()
        profit = float(my_record[2]) - float(my_record[3])
        if profit >= 0:
            total_profit += profit
            profitable += 1
        profit_list[my_record[0]] = profit

average_profit["average_profit"] = total_profit / profitable

my_list.append(profit_list)
my_list.append(average_profit)

with open("text_7(mine).json", "w", encoding="utf-8") as my_json:
    json.dump(my_list, my_json, indent=4, ensure_ascii=False)