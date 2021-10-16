
class Road:

    def  __init__(self, length, width):
        Road._length = length
        Road._width = width

    def Method(self, mas_1_m2, thickness_sm):
        mass = self._length * self._width * mas_1_m2 * thickness_sm / 1000
        return mass

my_length = 5000
my_width = 20
my_mas_1m2 = 25
my_thickness_sm = 5
my_road = Road(my_length, my_width)
print(my_road.Method(my_mas_1m2, my_thickness_sm))