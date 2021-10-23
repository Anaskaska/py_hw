from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothes):
    def __init__(self, size):
        self.size = float(size)
    @property
    def consumption(self):
        return self.size / 6.5 + 0.5
    def sum_consumption(self, list_of_suit):
        s = 0
        for elem in list_of_suit:
            s += elem.consumption
        return s


class Suit(Clothes):
    def __init__(self, length):
        self.length = float(length)
    @property
    def consumption(self):
        return self.length * 2 + 0.3
    def sum_consumption(self, list_of_suit):
        s = 0
        for elem in list_of_suit:
            s += elem.consumption
        return s



my_coat_1 = Coat(1.76)
my_coat_2 = Coat(1.65)
print(f"Consumption for a coat: size {my_coat_1.size}  -  {my_coat_1.consumption:.2f} ")
print(f"Consumption for a coat: size {my_coat_2.size}  -  {my_coat_2.consumption:.2f} ")
list_of_coat = [my_coat_1, my_coat_2]
print(f"Total consumption for coat: {my_coat_2.sum_consumption(list_of_coat):.2f}")
my_suit_1 = Suit(1.72)
my_suit_3 = Suit(1.62)
my_suit_2 = Suit(1.80)
print(f"Consumption  a suit: high {my_suit_1.length}  -  {my_suit_1.consumption:.2f} ")
print(f"Consumption  a suit: high {my_suit_3.length}  -  {my_suit_3.consumption:.2f} ")
print(f"Consumption  a suit: high {my_suit_2.length}  -  {my_suit_2.consumption:.2f} ")

list_of_suit = [my_suit_1, my_suit_2, my_suit_3]
print(f"Total consumption for suit: {my_suit_1.sum_consumption(list_of_suit):.2f}")
print(f"Total consumption for all clothes: {my_suit_1.sum_consumption(list_of_suit + list_of_coat):.2f}")
