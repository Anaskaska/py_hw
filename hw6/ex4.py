
class Car:
    def __init__(self,speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Auto is running")
    def stop(self):
        print("Auto is stopped")
    def turn(self,direction):
        print(f"Auto is turning to {direction}")
    def show_speed(self):
        print(f"Your Speed is {self.speed}")

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Attention! Your speed more than 60!")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Attention! Your speed more than 40!")

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

my_town = TownCar(90, 'blue','Town')
my_sport = SportCar(120, 'red','Sport')
my_work = WorkCar(50, 'Yellow','Work')
my_police = PoliceCar(100, 'blue','Police')
my_town.show_speed()
my_work.show_speed()
my_work.speed = 30
my_work.show_speed()
my_police.turn('right')
