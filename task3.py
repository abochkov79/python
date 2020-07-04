class Cell:
    def __init__(self, num_cells):
        self.num_cells = num_cells

    def __str__(self):
        return "*" * self.num_cells

    def __add__(self, other):
        return (Cell(self.num_cells + other.num_cells))

    def __sub__(self, other):
        if self.num_cells != other.num_cells:
            return Cell(self.num_cells - other.num_cells if self.num_cells > other.num_cells else other.num_cells - self.num_cells)
        else:
            return "Количество ячеек в клетках равно!!!"

    def __mul__(self, other):
        return (Cell(self.num_cells * other.num_cells))

    def __truediv__(self, other):
        return (Cell(self.num_cells // other.num_cells))

    def make_order(self, n_row):
        my_st = ""
        for i in range(self.num_cells // n_row):
            my_st += "*" * n_row + "\n"
        my_st += "*" * (self.num_cells % n_row)
        return my_st



myCell_1 = Cell(10)
print(f"Клетка №1 из {myCell_1.num_cells} ячеек: {myCell_1}")
myCell_2 = Cell(3)
print(f"Клетка №2 из {myCell_2.num_cells} ячеек: {myCell_2}")
print(f"Сумма клетки №1 и клетки №2: {myCell_1 + myCell_2}")
print(f"Разность клетки №1 и клетки №2: {myCell_1 - myCell_2}")
print(f"Произведение клетки №1 и клетки №2: {myCell_1 * myCell_2}")
print(f"Частное от деления клетки №1 и клетки №2: {myCell_1 / myCell_2}")

r1 = 4
r2 = 2

print()
print(f"Клетка №1, организованная в ряды по {r1} ячеек:")
print(myCell_1.make_order(r1))
print()
print(f"Клетка №2, организованная в ряды по {r2} ячеек:")
print(myCell_2.make_order(r2))
