from time import sleep


class TrafficLight:

    def running(self):
        while True:
            self.__color = "Red"
            print(self.__color)
            sleep(7)
            self.__color = "Yellow"
            print(self.__color)
            sleep(2)
            self.__color = "Green"
            print(self.__color)
            sleep(7)
            self.__color = "Yellow"
            print(self.__color)
            sleep(2)

myTF = TrafficLight()
myTF.running()