def user_info(user_name, user_phone, user_surname,  user_email, user_city, user_year):
    """Возвращает данные о пользователе одной строкой

    Именованные параметры:
    user_name:      имя пользователя
    user_surname:   фамилия
    user_year:      год рождения
    user_city:      город проживания
    user_email:     email
    user_phone:     номер телефона

    """
    user_record = f"Имя: {user_name}, фамилия: {user_surname}, год рождения: {user_year}, город проживания: {user_city}, email: {user_email}, телефон: {user_phone}."
    return user_record

my_name = input("Введите имя: ")
my_surname = input("Введите фамилию: ")
my_year = input("Введите год рождения: ")
my_city = input("Введите город проживания: ")
my_email = input("Введите email: ")
my_phone = input("Введите номер телефона: ")

print()
print(user_info(user_email = my_email, user_name = my_name, user_year = my_year, user_phone = my_phone, user_surname = my_surname, user_city = my_city))
