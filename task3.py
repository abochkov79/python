class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {}
        self._income["wage"] = wage
        self._income["bonus"] = bonus


class Position(Worker):

    def get_full_name(self):
        print(f"Полное имя сотрудника: {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Доход сотрудника с учетом премии: {self._income['wage'] + self._income['bonus']}")


Worker1 = Position("Alex", "Smirnoff", "engineer", 200000, 50000)
Worker1.get_full_name()
Worker1.get_total_income()
print()

Worker2 = Position("Vladimir", "Ivanoff", "analyst", 220000, 40000)
Worker2.get_full_name()
Worker2.get_total_income()
