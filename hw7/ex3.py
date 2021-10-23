


class Cell:
    def __init__(self, cell):
        self.cell = int(cell)

    def __add__(self, other):
        return Cell(self.cell+other.cell)

    def __sub__(self, other):
        if self.cell-other.cell > 0:
            return Cell(self.cell-other.cell)
        else:
            print("Subtraction is impossible")

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell//self.cell)

    def make_order(self, num_in_line):
        s = ""
        for i in range(self.cell//num_in_line):
            s += "*" * num_in_line + "\n"
        s += "*" * (self.cell % num_in_line) + "\n"
        return s

    def __str__(self):
        return f"{self.cell}"

a = Cell(5)
b = Cell(7)
print(f" cell a  {a}  cell b {b}")
print(f" a + b = {a + b}")
print(f" a - b = {a - b}")
print(f" b - a = {b - a}")
print(f" a * b = {a * b}")
print(f" a / b = {a / b}")
print(f" b / a = {b / a}")
c = Cell(12)
print(c.make_order(5))