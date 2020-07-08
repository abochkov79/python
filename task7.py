class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return(f"{self.a}+{self.b}i")

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)

myNumber1 = ComplexNumber(2, 15)
myNumber2 = ComplexNumber(10, 3)
print(f"{myNumber1} + {myNumber2} = {myNumber1 + myNumber2}")
print(f"{myNumber1} * {myNumber2} = {myNumber1 * myNumber2}")

