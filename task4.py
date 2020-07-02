class Car:


    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала!")

    def stop(self):
        print("Машина остановилась!")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорость автомобиля: {self.speed} км/ч")

class TownCar(Car):
    def show_speed(self):
        print(f"Текущая скорость автомобиля: {self.speed} км/ч")
        speed_limit = 60
        if self.speed > speed_limit:
            print(f"Скорость превышена на {self.speed - speed_limit} км/ч, максимальная скорость - {speed_limit} км/ч!!!")


class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print(f"Текущая скорость автомобиля: {self.speed} км/ч")
        speed_limit = 40
        if self.speed > speed_limit:
            print(f"Скорость превышена на {self.speed - speed_limit} км/ч, максимальная скорость - {speed_limit} км/ч!!!")

class PoliceCar(Car):
    pass


myTownCar = TownCar(90, "Black", "Ford", False)
print(f"Городской автомобиль: название - {myTownCar.name}, цвет - {myTownCar.color}, скорость - {myTownCar.speed}, "
      f"полицейский автомобиль - {myTownCar.is_police}")
myTownCar.go()
myTownCar.show_speed()
myTownCar.turn("налево")
myTownCar.stop()
print()

mySportCar = SportCar(50, "Black", "Ford", False)
print(f"Спортивный автомобиль: название - {mySportCar.name}, цвет - {mySportCar.color}, скорость - {mySportCar.speed}, "
      f"полицейский автомобиль - {mySportCar.is_police}")
mySportCar.go()
mySportCar.show_speed()
mySportCar.turn("налево")
mySportCar.stop()
print()

myWorkCar = WorkCar(50, "Black", "Ford", False)
print(f"Рабочий автомобиль: название - {myWorkCar.name}, цвет - {myWorkCar.color}, скорость - {myWorkCar.speed}, "
      f"полицейский автомобиль - {myWorkCar.is_police}")
myWorkCar.go()
myWorkCar.show_speed()
myWorkCar.turn("налево")
myWorkCar.stop()
print()

myPoliceCar = PoliceCar(50, "Black", "Ford", True)
print(f"Городской автомобиль: название - {myPoliceCar.name}, цвет - {myPoliceCar.color}, скорость - {myPoliceCar.speed}, "
      f"полицейский автомобиль - {myPoliceCar.is_police}")
myPoliceCar.go()
myPoliceCar.show_speed()
myPoliceCar.turn("налево")
myPoliceCar.stop()
print()
