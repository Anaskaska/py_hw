
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position (Worker):

    def get_full_name(self):
#        print(f" {self.name}  {self.surname} ")
        full_name = f"{self.name} {self.surname}"
        return full_name
    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

worker_1 = Position("Petr", "Ivanov","Director",5000,3000)
print(worker_1.name)
print(worker_1.surname)
print(worker_1._income)
print(worker_1.get_full_name())
print(worker_1.get_total_income())

