user_time = int(input("Введите время в секундах: "))

seconds = user_time % 60
hours = (user_time - seconds) // (60 * 60)
minutes = int((user_time - seconds - hours * 60 * 60) / 60)

print("Время в формате чч:мм:сс - {:0>2d}:{:0>2d}:{:0>2d}".format(hours, minutes, seconds))


