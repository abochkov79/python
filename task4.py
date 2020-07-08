class Warehouse:
    pass

class OfficeEquipment:
    def __init__(self, brand, weight):
        self.brand = brand
        self.weight = weight

class Printer(OfficeEquipment):
    def __init__(self, brand, weight, printing_speed):
        super().__init__(brand, weight)
        self.printing_speed = printing_speed

class Scanner(OfficeEquipment):
    def __init__(self, brand, weight, dpi):
        super().__init__(brand, weight)
        self.dpi = dpi

class Xerox(OfficeEquipment):
    def __init__(self, brand, weight, max_format):
        super().__init__(brand, weight)
        self.max_format = max_format


myPrinter = Printer("Citizen", 4.5, 10)
myScanner = Scanner("Mustek", 2.3, "1200x1200")
myXerox = Xerox("Kyocera", 14.6, "A3")

print(f"Принтер: {myPrinter.brand}, вес: {myPrinter.weight} кг, скорость печати: {myPrinter.printing_speed} стр./мин.")
print(f"Сканер: {myScanner.brand}, вес: {myScanner.weight} кг, разрешение сканирования: {myScanner.dpi} точек/дюйм.")
print(f"Ксерокс: {myXerox.brand}, вес: {myXerox.weight} кг, максимальный формат печати: {myXerox.max_format}.")