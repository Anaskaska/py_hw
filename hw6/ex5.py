
class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Drawing ")

class Pen(Stationery):
    def draw(self):
         print(f"Drawing Pen {self.title}")
class Pencil(Stationery):
    def draw(self):
        print(f"Drawing Pencil {self.title}")
class Handle(Stationery):
    def draw(self):
        print(f"Drawing Handle {self.title}")

my_pen = Pen("A")
my_pen.draw()
my_pencil = Pencil("B")
my_pencil.draw()
my_handle = Handle("C")
my_handle.draw()


