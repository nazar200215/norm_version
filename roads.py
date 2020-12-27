#import sys

# sys.path.append("ka-8226\\src\\constants\\roads_constants.py")
from char_of_roads import *


class Road():
    _name = None

    def __init__(self):
        self._line_numbers = LINE_NUMBERS[self._name]
        # self._line_width = LINE_WIDTH[self._name]
        self._bus_line = False
        # self._roadway_width = _line_numbers
        self._max_traffic = MAX_TRAFFIC[self._name]
        self._fence = False
        self._max_speed = MAX_SPEED[self._name]

    # возможно переделаю на осевую нагрузку
    def max_weight(self):
        return 0

    def get_max_traffic(self):
        return self._max_traffic

    def get_max_speed(self):
        return self._max_speed


class DirtRoad(Road):
    def __init__(self):
        self._name = "DirtRoad"
        super().__init__()

    def get_stack(self, transport):
        return transport.get_weight > self.max_weight()


class SimpleCityRoad(Road):
    def __init__(self):
        self._name = "SimpleCityRoad"
        super().__init__()
        self._central_separate_line = True
        self._bus_line = True


class CityExpressRoad(Road):
    def __init__(self):
        self._name = "CityExpressRoad"
        # Две 4 полосы
        super().__init__()


class Highway(Road):
    def __init__(self):
        self._name = "Highway"
        super().__init__()


class Freeway(Road):
    def __init__(self):
        self._name = "Freeway"
        super().__init__()