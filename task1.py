class Matrix:
    def __init__(self, mtr):
        self.mtr = mtr

    def __str__(self):
        my_str = ""
        for r in range(len(self.mtr)):
            for c in range(len(self.mtr[r])):
                my_str += f"{self.mtr[r][c]:<5}"
            if r != len(self.mtr) - 1:
                my_str += "\n"
        return my_str

    def __add__(self, other):
        new_mtr = []
        for r in range(len(self.mtr)):
            new_col = []
            for c in range(len(self.mtr[r])):
                try:
                    new_col.append(self.mtr[r][c] + other.mtr[r][c])
                except IndexError:
                    return "Ошибка. Матрицы должны быть одинакового размера!!!"
            new_mtr.append(new_col)
        return Matrix(new_mtr)

matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

print(matrix_1)
print(f"{'+':^12}")
print(matrix_2)
print(f"{'=':^12}")
print(matrix_1 + matrix_2)