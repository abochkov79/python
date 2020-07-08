class MyDivisionError(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt


while True:
    try:
        a = float(input("Введите делимое: "))
        b = float(input("Введите делитель: "))
    except ValueError:
        print("Необходимо вводить числа!!!")
    else:
        try:
            if b == 0:
                raise MyDivisionError("Делитель не может равняться нулю!!!")
        except MyDivisionError as err:
            print(err)
        else:
            print(f"Результат деления {a} на {b}: {a/b:.2f}")
            break
