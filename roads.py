from char_of_roads import *


class Road():
    _name = None

    def __init__(self):
        self._line_numbers = LINE_NUMBERS[self._name]
        self._bus_line = False
        self._max_traffic = MAX_TRAFFIC[self._name]
        self._fence = False
        self._max_speed = MAX_SPEED[self._name]

    def get_max_traffic(self):
        return self._max_traffic

    def get_max_speed(self):
        return self._max_speed


class DirtRoad(Road):
    def __init__(self):
        self._name = "DirtRoad"
        super().__init__()


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