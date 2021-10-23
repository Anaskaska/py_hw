from random import randint

class Matrix:

    def __init__(self, matr):
        self.matrix = matr

    def __str__(self):
        s = ""
        for string_m in self.matrix:
            for elem in string_m:
                s += f"{elem:02} "
            s += "\n"
        return s


    def __add__(self, other):
        if (len(self.matrix) is not len(other.matrix)) or (len(self.matrix[0]) is not len(other.matrix[0])):
            return "Is not possible to sum such matrix..."
        else:
            matrix = [
                [self.matrix[i][j]+other.matrix[i][j]for j in range(len(self.matrix[i]))]
                    for i in range(len(self.matrix))]
        return Matrix(matrix)


matr_A = Matrix([[randint(0,10) for _ in range(3)] for _ in range(3)])
matr_B = Matrix([[randint(0,10) for _ in range(4)] for _ in range(3)])
print(matr_A)
print(matr_B)
print(matr_A + matr_B)

