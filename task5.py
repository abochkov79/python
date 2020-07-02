class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки инструментом "{self.title}".')
        print("Рисовать ручкой нужно осторожно!!!")


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки инструментом "{self.title}".')
        print("Не забудьте наточить карандаш как следует!!!")

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки инструментом "{self.title}".')
        print("Рисовать маркером - одно удовольствие!!!")

myStationery = Stationery("канцелярская принадлежность")
myStationery.draw()
print()

myPen = Pen("ручка")
myPen.draw()
print()

myPencil = Pencil("карандаш")
myPencil.draw()
print()

myHandle = Handle("маркер")
myHandle.draw()