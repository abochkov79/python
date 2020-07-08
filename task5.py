class Warehouse:
    def __init__(self, name):
        self.name = name

        # Здесь храним информацию о наличии оргтехники на складе
        self.stock = {"printers": [], "scanners": [], "xeroxes": []}

        # Здесь храним информацию об оргтехнике, переданной в каждое подразделение
        self.recepients = {"Бухгалтерия": {"printers": [], "scanners": [], "xeroxes": []},
                           "Департамент маркетинга": {"printers": [], "scanners": [], "xeroxes": []},
                           "Департамент разработки": {"printers": [], "scanners": [], "xeroxes": []},
                           }

    def __str__(self):
        return f'На складе "{self.name}" находится: принтеров - {len(self.stock["printers"])}, сканеров - {len(self.stock["scanners"])}, ксероксов - {len(self.stock["xeroxes"])}.'

    # Метод, отвечающий за прием оргтехники на склад
    def get_equipment(self, equipment, number):
        if type(equipment) == Printer:
            for i in range(number):
                self.stock["printers"].append(equipment)
        elif type(equipment) == Scanner:
            for i in range(number):
                self.stock["scanners"].append(equipment)
        elif type(equipment) == Xerox:
            for i in range(number):
                self.stock["xeroxes"].append(equipment)
        print(
            f'На склад "{self.name}" принято {number} {"принтеров" if type(equipment) == Printer else "сканеров" if type(equipment) == Scanner else "ксероксов"}.')

    # Метод, отвечающий за передачу оргтехники в подразделение (recepient)
    def dispatch_equipment(self, recepient, equipment, number):
        if type(equipment) == Printer:
            for i in range(number):
                self.recepients[recepient]["printers"].append(self.stock["printers"].pop())
        elif type(equipment) == Scanner:
            for i in range(number):
                self.recepients[recepient]["scanners"].append(self.stock["scanners"].pop())
        elif type(equipment) == Xerox:
            for i in range(number):
                self.recepients[recepient]["xeroxes"].append(self.stock["xeroxes"].pop())
        print(
            f'Со склада "{self.name}" в подразделение "{recepient}" передано {number} {"принтеров" if type(equipment) == Printer else "сканеров" if type(equipment) == Scanner else "ксероксов"}.')


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
print(f"Ксерокс: {myXerox.brand}, вес: {myXerox.weight} кг, максимальный формат печати: {myXerox.max_format}.\n")

myWarehouse = Warehouse("Основной склад")

myWarehouse.get_equipment(myPrinter, 10)
myWarehouse.get_equipment(myScanner, 15)
myWarehouse.get_equipment(myXerox, 5)
print()
print(myWarehouse)

myWarehouse.get_equipment(myPrinter, 2)
myWarehouse.get_equipment(myScanner, 7)
myWarehouse.get_equipment(myXerox, 4)
print()
print(myWarehouse, "\n")

myWarehouse.dispatch_equipment("Бухгалтерия", myPrinter, 1)
myWarehouse.dispatch_equipment("Департамент маркетинга", myScanner, 2)
myWarehouse.dispatch_equipment("Департамент разработки", myXerox, 6)
print()
print(myWarehouse, "\n")


for i in myWarehouse.recepients:
    print(
        f'В подразделение "{i}" передано всего: {len(myWarehouse.recepients[i]["printers"])} принтеров, {len(myWarehouse.recepients[i]["scanners"])} сканеров, {len(myWarehouse.recepients[i]["xeroxes"])} ксероксов.')

