class Date:
    def __init__(self, date_str):
        self.date_str = date_str

    def __str__(self):
        Date.valid_date(Date.extract_date(myDate))
        return self.date_str

    @classmethod
    def extract_date(cls, param):
        new_date = param.date_str.split("-")
        my_day = int(new_date[0])
        my_month = int(new_date[1])
        my_year = int(new_date[2])
        return my_day, my_month, my_year

    @staticmethod
    def valid_date(date_int):
        start_year = 2010
        end_year = 2020
        num_days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        try:
            if date_int[1] == 2 and date_int[2] % 4 == 0:
                if date_int[0] not in range(1, num_days[1] + 1):
                    print(f"День должен быть от 1 до {num_days[1] + 1}!!!")
            else:
                if date_int[0] not in range(1, num_days[date_int[1] - 1]):
                    print(f"День должен быть от 1 до {num_days[date_int[1] - 1]}!!!")
        except IndexError:
            print(f"День должен быть от 1 до 31!!!")
        if date_int[1] not in range(1, 13):
            print("Месяц должен быть от 1 до 12!!!")
        if date_int[2] not in range(2010, 2021):
            print("Год должен быть от 2010 до 2020!!!")

myDate = Date("30-02-2024")
print(myDate)
