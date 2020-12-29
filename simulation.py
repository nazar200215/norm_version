import pygame
import os
from transport import *
from graph import *
from graph import adress
from math import sqrt, acos, degrees

white = (143, 54, 255)
select_car_action = ("MotorCycle", "PickupTruck",
                     "CityBioFuelCar", "CityElectricCar", "CityGasolinCar", "DumpTruck", "Bus")

motorcycle = MotorCycle()
pickup = PickupTruck()
city_gasolin = CityGasolinCar()
city_bio = CityBioFuelCar()
city_electric = CityElectricCar()
dump_track = DumpTruck()
bus = Bus()

transport = (motorcycle, pickup, city_bio, city_electric, city_gasolin, dump_track, bus)
transport_list = ["motorcycle", "pickup", "city_bio", "city_electric", "city_gasolin", "dump_track", "bus"]
car_path = []

for i in range(len(transport_list)):
    print("Input the path for", transport_list[i], ":")
    i1, i2 = input(), input()
    car_path.append(dijkstra(graph, i1, i2))
    print(dijkstra(graph, i1, i2))


class Simulation:
    def __init__(self, win):
        self.width = 1150
        self.height = 700
        self.win = win

        self.size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.size)
        self.background_image = pygame.image.load("img\\background.png").convert_alpha()
        self.motorcycle = pygame.image.load("img\\motorsycle 1.png").convert_alpha()
        self.pickup = pygame.image.load("img\\pickup 1.png").convert_alpha()
        self.city_gasolin = pygame.image.load("img\\city-gasolin 1.png").convert_alpha()
        self.city_electric = pygame.image.load("img\\city-electric 1.png").convert_alpha()
        self.city_bio = pygame.image.load("img\\city-bio 1.png").convert_alpha()
        self.dump_track = pygame.image.load("img\\dump 1.png").convert_alpha()
        self.bus = pygame.image.load("img\\bus 1.png").convert_alpha()
        self.info_box = pygame.image.load("img\\information.png").convert_alpha()

        self.temp_name = ""
        self.transport_objects = []

        self.buttons = (self.motorcycle, self.pickup, self.city_bio, self.city_electric,
                        self.city_gasolin, self.dump_track, self.bus)

        self.buttons_coord_x = (995, 975, 980, 980, 980, 935, 890, 425, 314)
        self.buttons_coord_y = (90, 150, 235, 330, 420, 500, 600, 600, 664)

        self.buttons_width = (42, 80, 70, 70, 70, 159, 249, 25, 123)
        self.buttons_height = (17, 33, 31, 35, 50, 60, 65, 25, 25)

        pygame.display.set_caption("У НАС Є МРІЯ, 60 З КУРСОВОЇ РОБОТИ")

    def run(self):
        run = True

        clock = pygame.time.Clock()

        while run:
            clock.tick(500)
            self.screen.blit(self.background_image, [0, 0])
            self.draw_text()
            self.draw_selection_cars()
            self.draw_car()
            self.draw_info()

            pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(9):
                        if (self.buttons_coord_x[i] + self.buttons_width[i] >
                                pos[0] > self.buttons_coord_x[i] and
                                self.buttons_coord_y[i] + self.buttons_height[i] >
                                pos[1] > self.buttons_coord_y[i]):
                            if i <= 6:
                                print(select_car_action[i])
                                self.temp_name = select_car_action[i]

                                self.display_info(self.get_transport_type(self.temp_name))

                                break
                            elif i == 7:
                                self.temp_name = ""
                            else:
                                car = self.get_transport_type(self.temp_name)
                                self.transport_objects.append(car)

                                for i in range(len(transport_list)):
                                    if car.get_name() == select_car_action[i]:
                                        car.set_pathway(car_path[i])
                                        self.get_xy()
                                        break

            self.draw()

        pygame.quit()

    def get_xy(self):
        for car in self.transport_objects:
            if car.xy_pathway == []:
                for path in car.get_pathway():
                    for a in adress:
                        if a.get_name() == path:
                            car.xy_pathway.append([a.get_x(), a.get_y()])
                            car.set_x(a.get_x())
                            car.set_y(a.get_y())
                if car.px is None and car.py is None:
                    px = car.xy_pathway[car.pathway_point]
                    car.px = px[0]
                    py = car.xy_pathway[car.pathway_point]
                    car.py = py[1]

    def scalar(self, x1, y1, x2, y2):
        return x1 * x2 + y1 * y2

    def mod(self, x, y):
        return sqrt(x * x + y * y)

    def get_angle(self, x1, y1, x2, y2):
        return degrees(acos(self.scalar(x1, y1, x2, y2) /
                            (self.mod(x1, y1) * self.mod(x2, y2))))

    def update_car_xy(self):
        for car in self.transport_objects:
            if car.px > car.get_x():
                car.set_x(car.get_x() + 1)
            elif car.px < car.get_x():
                car.set_x(car.get_x() - 1)
            elif car.py != car.get_y():
                if car.py > car.get_y():
                    car.set_y(car.get_y() + 1)
                elif car.py < car.get_y():
                    car.set_y(car.get_y() - 1)
            else:
                if car.pathway_point != len(car.xy_pathway) - 1:
                    car.pathway_point += 1

                    px = car.xy_pathway[car.pathway_point]
                    car.px = px[0]
                    py = car.xy_pathway[car.pathway_point]
                    car.py = py[1]
                else:
                    pass


    def draw_car(self):
        self.update_car_xy()
        for car in self.transport_objects:
            for j in range(len(transport)):
                if car.get_name() == transport[j].get_name():
                    im = self.buttons[j]
                    im_small = pygame.transform.rotozoom(im, 0, 0.2)
                    self.screen.blit(im_small, (car.get_x(), car.get_y()))

    def draw(self):
        pygame.display.update()

    def draw_text(self):
        font = pygame.font.Font('freesansbold.ttf', 24)
        select_car_text = font.render("SELECT A CAR", True, white)
        self.screen.blit(select_car_text, dest=(925, 14))

    def draw_selection_cars(self):
        self.screen.blit(self.motorcycle, (995, 90))
        self.screen.blit(self.pickup, (975, 150))
        self.screen.blit(self.city_bio, (980, 235))
        self.screen.blit(self.city_electric, (980, 330))
        self.screen.blit(self.city_gasolin, (980, 420))
        self.screen.blit(self.dump_track, (935, 500))
        self.screen.blit(self.bus, (890, 600))

    def get_transport_type(self, name):
        motorcycle = MotorCycle()
        pickup = PickupTruck()
        city_gasolin = CityGasolinCar()
        city_bio = CityBioFuelCar()
        city_electric = CityElectricCar()
        dump_track = DumpTruck()
        bus = Bus()

        if motorcycle.get_name() == name:
            return motorcycle
        if pickup.get_name() == name:
            return pickup
        if city_gasolin.get_name() == name:
            return city_gasolin
        if city_bio.get_name() == name:
            return city_bio
        if city_electric.get_name() == name:
            return city_electric
        if dump_track.get_name() == name:
            return dump_track
        if bus.get_name() == name:
            return bus

    def display_info(self, car):
        font = pygame.font.Font('freesansbold.ttf', 8)

        fuel = str(car.get_fuel())
        f_type = str(car.get_fuel_type())
        w = str(car.get_weight())
        max_s = str(car.get_max_speed())

        base_mount_of_fuel = font.render(fuel, True, white)
        fuel_type = font.render(f_type, True, white)
        weight = font.render(w, True, white)
        max_speed = font.render(max_s, True, white)

        temp_y = 632
        self.screen.blit(base_mount_of_fuel, dest=(105, temp_y))
        self.screen.blit(fuel_type, dest=(200, temp_y))
        self.screen.blit(weight, dest=(290, temp_y))
        self.screen.blit(max_speed, dest=(380, temp_y))

    def draw_info(self):
        if self.temp_name != "":
            self.screen.blit(self.info_box, (0, 600))
            self.display_info(self.get_transport_type(self.temp_name))
