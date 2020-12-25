from char_or_transport import*


class Transport:
    """
    basic transport class
    """
    _name = None
    _pathway = None

    def __init__(self):
        self._fuel_type = FUEL_TYPES[0]
        self._fuel = BASE_MOUNT_OF_FUEL[self._name]
        self._max_speed = MAX_SPEED[self._name]
        self._wheels_type = WHEELS_TYPE["Ordinary"]
        self._weight = WEIGHT[self._name]
        self._x = None
        self._y = None
        self._on_road = False
        self.xy_pathway = []
        self.pathway_point = 1
        self.drove_the_way = False
        self.px = None
        self.py = None

    def on_road(self, bool):
        self._on_road = bool

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def set_pathway(self, pathway):
        self._pathway = pathway

    def get_pathway(self):
        return self._pathway

    def set_fuel(self, fuel):
        self._fuel = fuel

    def get_fuel(self):
        return self._fuel

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def get_fuel_type(self):
        return self._fuel_type

    def get_max_speed(self):
        return self._max_speed

    def get_weight(self):
        return self._weight

    def move_to_gas_station(self):
        pass


class MotorCycle(Transport):
    def __init__(self):
        self._name = "MotorCycle"
        super().__init__()
        self._wheels_type = WHEELS_TYPE[self._name]


class DumpTruck(Transport):
    def __init__(self):
        self._name = "DumpTruck"
        super().__init__()
        self._wheels_type = WHEELS_TYPE["SpecialCar"]
        self._fuel_type = FUEL_TYPES[1]
        self._goods = False


class PickupTruck(Transport):
    def __init__(self):
        self._name = "PickupTruck"
        super().__init__()
        self._wheels_type = WHEELS_TYPE["SpecialCar"]
        self._fuel_type = FUEL_TYPES[1]
        self._goods = False
        self._passengers = False


class PassengerCar(Transport):
    def __init__(self):
        super().__init__()
        self._passenger_number = 0

    def take_passenger(self):
        if self._passenger_number != MAX_PASSENGER_NUMBER(self._name):
            self._passenger_number += 1
            self._weight += PASSANGER_WEIGHT

    def drop_off_passenger(self):
        self._passenger_number -= 1
        self._weight -= PASSANGER_WEIGHT


class Bus(PassengerCar):
    def __init__(self):
        self._name = "Bus"
        super().__init__()
        self._wheels_type = WHEELS_TYPE["SpecialCar"]


class CityGasolinCar(PassengerCar):
    def __init__(self):
        self._name = "CityGasolinCar"
        super().__init__()
        self._fuel_type = FUEL_TYPES[0]


class CityElectricCar(PassengerCar):
    def __init__(self):
        self._name = "CityElectricCar"
        super().__init__()
        self._fuel_type = FUEL_TYPES[2]


class CityBioFuelCar(PassengerCar):
    def __init__(self):
        self._name = "CityBioFuelCar"
        super().__init__()
        self._fuel_type = FUEL_TYPES[3]
