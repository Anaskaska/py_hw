from time import sleep

class TrafficLight:
    colors = ('red', 'yellow', 'green')
    time_light = (7, 2, 5)
    def __init__(self):
        self.__color = "red"

    def running(self ):
        while True:
            for color_light in self.colors:
                self.__color = color_light
                print(self.__color)
                sleep(self.time_light[self.colors.index(self.__color)])

traffic_light = TrafficLight()
traffic_light.running()
