from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def material_spend(self):
        pass

class Coat(Clothes):
    def __init__(self, name, V):
        self.name = name
        self.V = V

    @property
    def material_spend(self):
        return self.V / 6.5 + 0.5

class Suit(Clothes):
    def __init__(self, name, H):
        self.name = name
        self.H = H

    @property
    def material_spend(self):
        return 2 * self.H + 0.3

myCoat = Coat("пальто", 10)
print(f"Расход ткани для {myCoat.name}: {myCoat.material_spend:.2f} м")
mySuit = Suit("костюм", 1.7)
print(f"Расход ткани для {mySuit.name}: {mySuit.material_spend:.2f} м")