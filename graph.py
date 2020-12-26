from collections import defaultdict
from heapq import *


from math import sqrt
from roads import *

dirt_road = DirtRoad()
simple_city_road = SimpleCityRoad()
city_express_road = CityExpressRoad()
highway = Highway()
freeway = Freeway()

max_speed = 90


def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))

    q, seen, mins = [(0, f, [])], set(), {f: 0}
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = [v1] + path
            if v1 == t:
                return (path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen:
                    continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf"), []


class Node():
    def __init__(self, name, x, y):
        self._x = x
        self._y = y
        self._name = name

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_name(self):
        return self._name

    def __str__(self):
        return self._name


class Edge():
    def __init__(self, node_1, node_2, road, orientation, car_max_speed):
        self._car_max_speed = car_max_speed
        self._node_1 = node_1
        self._node_2 = node_2
        self._road = road
        self._orientation = orientation

    def get_node_1(self):
        return self._node_1

    def get_node_2(self):
        return self._node_2

    def get_car_max_speeed(self):
        return self._car_max_speed

    def get_road(self):
        return self._road

    def get_orientation(self):
        return self._orientation

    def get_time(self):
        if self._road.get_max_speed() < self._car_max_speed:
            self._car_max_speed = self._road.get_max_speed()

        length = sqrt((self._node_1.get_x() - self._node_2.get_x()) *
                      (self._node_1.get_x() - self._node_2.get_x()) +
                      ((self._node_1.get_y() - self._node_2.get_y()) *
                       (self._node_1.get_y() - self._node_2.get_y())))

        return length / self._car_max_speed

    def __gt__(self, value):
        return self.get_time() > value.get_time

    def __lt__(self, value):
        return self.get_time() < value.get_time

    def __le__(self, value):
        return self.get_time() <= value.get_time

    def __ge__(self, value):
        return self.get_time() >= value.get_time


trash = Node("trash", 79, 36)
left_corner_1 = Node("left_corner_1", 89, 99)
left_corner_2 = Node("left_corner_2", 89, 113)

house_1 = Node("house_1", 71, 173)

left_corner_3 = Node("left_corner_3", 89, 175)
left_corner_4 = Node("left_corner_4", 89, 190)

left_corner_51 = Node("left_corner_51", 89, 259)
left_corner_52 = Node("left_corner_52", 89, 271)

factory = Node("factory", 71, 296)

left_corner_61 = Node("left_corner_61", 89, 325)
left_corner_62 = Node("left_corner_62", 89, 338)

left_corner_71 = Node("left_corner_71", 89, 398)
left_corner_72 = Node("left_corner_72", 89, 412)

work_1 = Node("work_1", 71, 428)

left_corner_81 = Node("left_corner_81", 89, 434)
left_corner_82 = Node("left_corner_82", 89, 448)

left_corner_9 = Node("left_corner_9", 89, 493)
left_corner_10 = Node("left_corner_10", 89, 507)

house_2 = Node("house_2", 71, 544)

left_corner_11 = Node("left_corner_11", 89, 569)
left_corner_12 = Node("left_corner_12", 89, 583)

left_bot_corner = Node("left_bot_corner", 81, 633)

top_right_corner = Node("top_right_corner", 808, 36)
right_corner_1 = Node("right_corner_1", 800, 99)
right_corner_2 = Node("right_corner_2", 800, 113)

house_12 = Node("house_1", 818, 193)  # TODO

right_corner_3 = Node("right_corner_3", 800, 175)
right_corner_4 = Node("right_corner_4", 800, 190)

right_corner_51 = Node("right_corner_51", 800, 259)
right_corner_52 = Node("right_corner_52", 800, 271)

school = Node("school", 818, 296)

right_corner_61 = Node("right_corner_61", 800, 325)
right_corner_62 = Node("right_corner_62", 800, 338)

right_corner_71 = Node("right_corner_71", 800, 398)
right_corner_72 = Node("right_corner_72", 800, 412)

work_2 = Node("work_2", 818, 428)

right_corner_81 = Node("right_corner_81", 800, 434)
right_corner_82 = Node("right_corner_82", 800, 448)

right_corner_9 = Node("right_corner_9", 800, 493)
right_corner_10 = Node("right_corner_10", 800, 507)

house_5 = Node("house_5", 818, 544)

right_corner_11 = Node("right_corner_11", 800, 569)
right_corner_12 = Node("right_corner_12", 800, 583)

right_bot_corner = Node("right_bot_corner", 808, 633)

house_3 = Node("house_3", 256, 633)
house_4 = Node("house_4", 666, 633)

house_6 = Node("house_6", 666, 38)
house_7 = Node("house_7", 250, 38)

house_8 = Node("house_8", 437, 175)
house_9 = Node("house_9", 250, 190)
house_10 = Node("house_10", 664, 190)
house_11 = Node("house_11", 443, 507)

bs_1 = Node("bs_1", 256, 569)
bs_2 = Node("bs_2", 256, 584)

bs_3 = Node("bs_3", 666, 569)
bs_4 = Node("bs_4", 666, 584)

bs_5 = Node("bs_5", 256, 100)
bs_6 = Node("bs_6", 256, 113)

bs_7 = Node("bs_7", 666, 100)
bs_8 = Node("bs_8", 666, 113)

adress = [bs_8, bs_7, bs_6, bs_5, bs_4, bs_3, bs_2, bs_1,
          house_1, house_2, house_3, house_4, house_5, house_6,
          house_7, house_8, house_9, house_10, house_11, house_12,
          work_1, work_2, trash, factory, school,
          right_bot_corner, right_corner_1, right_corner_2, right_corner_3, right_corner_4,
          right_corner_51, right_corner_52, right_corner_61, right_corner_62,
          right_corner_71, right_corner_72, right_corner_81, right_corner_82,
          right_corner_9, right_corner_10, right_corner_11, right_corner_12,
          top_right_corner, left_bot_corner, right_bot_corner]

graph = [
    (house_7.get_name(), trash.get_name(), Edge(house_7, trash, dirt_road, 'l', max_speed).get_time()),
    (house_6.get_name(), house_7.get_name(), Edge(house_6, house_7, dirt_road, 'l', max_speed).get_time()),
    (top_right_corner.get_name(), house_6.get_name(),
     Edge(top_right_corner, house_6, dirt_road, 'l', max_speed).get_time()),

    (trash.get_name(), house_1.get_name(), Edge(trash, house_1, highway, 'd', max_speed).get_time()),
    (house_1.get_name(), factory.get_name(), Edge(house_1, factory, highway, 'd', max_speed).get_time()),
    (factory.get_name(), work_1.get_name(), Edge(factory, work_1, highway, 'd', max_speed).get_time()),
    (work_1.get_name(), house_2.get_name(), Edge(work_1, house_2, highway, 'd', max_speed).get_time()),
    (
    house_2.get_name(), left_bot_corner.get_name(), Edge(house_2, left_bot_corner, highway, 'd', max_speed).get_time()),

    (left_bot_corner.get_name(), house_3.get_name(),
     Edge(left_bot_corner, house_3, dirt_road, 'r', max_speed).get_time()),
    (house_3.get_name(), house_4.get_name(), Edge(house_3, house_4, dirt_road, 'r', max_speed).get_time()),
    (house_4.get_name(), right_bot_corner.get_name(),
     Edge(house_4, right_bot_corner, dirt_road, 'r', max_speed).get_time()),

    (right_bot_corner.get_name(), house_5.get_name(),
     Edge(right_bot_corner, house_5, highway, 'u ', max_speed).get_time()),
    (house_5.get_name(), work_2.get_name(), Edge(house_5, work_2, highway, 'u ', max_speed).get_time()),
    (work_2.get_name(), school.get_name(), Edge(work_2, school, highway, 'u ', max_speed).get_time()),
    (school.get_name(), house_12.get_name(), Edge(school, house_12, highway, 'u ', max_speed).get_time()),
    (house_12.get_name(), top_right_corner.get_name(),
     Edge(house_12, top_right_corner, highway, 'u ', max_speed).get_time()),

    (top_right_corner.get_name(), right_corner_1.get_name(),
     Edge(top_right_corner, right_corner_1, highway, 'd', max_speed).get_time()),
    (right_corner_1.get_name(), right_corner_2.get_name(),
     Edge(right_corner_1, right_corner_2, highway, 'd', max_speed).get_time()),
    (right_corner_2.get_name(), right_corner_3.get_name(),
     Edge(right_corner_2, right_corner_3, highway, 'd', max_speed).get_time()),
    (right_corner_3.get_name(), right_corner_4.get_name(),
     Edge(right_corner_3, right_corner_4, highway, 'd', max_speed).get_time()),
    (right_corner_51.get_name(), right_corner_52.get_name(),
     Edge(right_corner_51, right_corner_52, highway, 'd', max_speed).get_time()),
    (right_corner_52.get_name(), right_corner_61.get_name(),
     Edge(right_corner_52, right_corner_61, highway, 'd', max_speed).get_time()),
    (right_corner_61.get_name(), right_corner_62.get_name(),
     Edge(right_corner_61, right_corner_62, highway, 'd', max_speed).get_time()),
    (right_corner_62.get_name(), right_corner_71.get_name(),
     Edge(right_corner_62, right_corner_71, highway, 'd', max_speed).get_time()),
    (right_corner_71.get_name(), right_corner_72.get_name(),
     Edge(right_corner_71, right_corner_72, highway, 'd', max_speed).get_time()),
    (right_corner_72.get_name(), right_corner_81.get_name(),
     Edge(right_corner_72, right_corner_81, highway, 'd', max_speed).get_time()),
    (right_corner_81.get_name(), right_corner_82.get_name(),
     Edge(right_corner_81, right_corner_82, highway, 'd', max_speed).get_time()),
    (right_corner_82.get_name(), right_corner_9.get_name(),
     Edge(right_corner_82, right_corner_9, highway, 'd', max_speed).get_time()),
    (right_corner_9.get_name(), right_corner_10.get_name(),
     Edge(right_corner_9, right_corner_10, highway, 'd', max_speed).get_time()),
    (right_corner_10.get_name(), right_corner_11.get_name(),
     Edge(right_corner_10, right_corner_11, highway, 'd', max_speed).get_time()),
    (right_corner_11.get_name(), right_corner_12.get_name(),
     Edge(right_corner_11, right_corner_12, highway, 'd', max_speed).get_time()),
    (right_corner_12.get_name(), right_bot_corner.get_name(),
     Edge(right_corner_12, right_bot_corner, highway, 'd', max_speed).get_time()),

    (left_corner_1.get_name(), trash.get_name(), Edge(left_corner_1, trash, highway, 'u', max_speed).get_time()),
    (left_corner_2.get_name(), left_corner_1.get_name(),
     Edge(left_corner_2, left_corner_1, highway, 'u', max_speed).get_time()),
    (left_corner_3.get_name(), left_corner_2.get_name(),
     Edge(left_corner_3, left_corner_2, highway, 'u', max_speed).get_time()),
    (left_corner_4.get_name(), left_corner_3.get_name(),
     Edge(left_corner_4, left_corner_3, highway, 'u', max_speed).get_time()),
    (left_corner_52.get_name(), left_corner_51.get_name(),
     Edge(left_corner_52, left_corner_51, highway, 'u', max_speed).get_time()),
    (left_corner_61.get_name(), left_corner_52.get_name(),
     Edge(left_corner_61, left_corner_52, highway, 'u', max_speed).get_time()),
    (left_corner_62.get_name(), left_corner_61.get_name(),
     Edge(left_corner_62, left_corner_61, highway, 'u', max_speed).get_time()),
    (left_corner_71.get_name(), left_corner_62.get_name(),
     Edge(left_corner_71, left_corner_62, highway, 'u', max_speed).get_time()),
    (left_corner_72.get_name(), left_corner_71.get_name(),
     Edge(left_corner_72, left_corner_71, highway, 'u', max_speed).get_time()),
    (left_corner_81.get_name(), left_corner_72.get_name(),
     Edge(left_corner_81, left_corner_72, highway, 'u', max_speed).get_time()),
    (left_corner_82.get_name(), left_corner_81.get_name(),
     Edge(left_corner_82, left_corner_81, highway, 'u', max_speed).get_time()),
    (left_corner_9.get_name(), left_corner_82.get_name(),
     Edge(left_corner_9, left_corner_82, highway, 'u', max_speed).get_time()),
    (left_corner_10.get_name(), left_corner_9.get_name(),
     Edge(left_corner_10, left_corner_9, highway, 'u', max_speed).get_time()),
    (left_corner_11.get_name(), left_corner_10.get_name(),
     Edge(left_corner_11, left_corner_10, highway, 'u', max_speed).get_time()),
    (left_corner_12.get_name(), left_corner_11.get_name(),
     Edge(left_corner_12, left_corner_11, highway, 'u', max_speed).get_time()),
    (left_bot_corner.get_name(), right_corner_12.get_name(),
     Edge(left_bot_corner, right_corner_12, highway, 'u', max_speed).get_time()),

    (left_corner_1.get_name(), bs_5.get_name(), Edge(left_corner_1, bs_5, simple_city_road, 'r', max_speed).get_time()),
    (bs_5.get_name(), bs_7.get_name(), Edge(bs_5, bs_7, simple_city_road, 'r', max_speed).get_time()),
    (bs_7.get_name(), right_corner_1.get_name(),
     Edge(bs_7, right_corner_1, simple_city_road, 'r', max_speed).get_time()),

    (bs_7.get_name(), left_corner_2.get_name(), Edge(bs_7, left_corner_2, simple_city_road, 'l', max_speed).get_time()),
    (bs_8.get_name(), bs_7.get_name(), Edge(bs_8, bs_7, simple_city_road, 'l', max_speed).get_time()),
    (right_corner_2.get_name(), bs_8.get_name(),
     Edge(right_corner_2, bs_8, simple_city_road, 'l', max_speed).get_time()),

    (left_corner_3.get_name(), house_8.get_name(), Edge(left_corner_3, house_8, highway, 'r', max_speed).get_time()),
    (house_8.get_name(), right_corner_3.get_name(), Edge(house_8, right_corner_3, highway, 'r', max_speed).get_time()),

    (left_corner_4.get_name(), house_9.get_name(),
     Edge(left_corner_4, house_9, simple_city_road, 'r', max_speed).get_time()),
    (house_9.get_name(), house_10.get_name(), Edge(house_9, house_10, simple_city_road, 'r', max_speed).get_time()),
    (house_10.get_name(), right_corner_4.get_name(),
     Edge(house_10, right_corner_4, simple_city_road, 'r', max_speed).get_time()),

    (right_corner_51.get_name(), left_corner_51.get_name(),
     Edge(right_corner_51, left_corner_51, freeway, 'l', max_speed).get_time()),
    (left_corner_52.get_name(), right_corner_52.get_name(),
     Edge(left_corner_52, right_corner_52, freeway, 'r', max_speed).get_time()),
    (right_corner_61.get_name(), left_corner_61.get_name(),
     Edge(right_corner_61, left_corner_61, freeway, 'l', max_speed).get_time()),
    (left_corner_62.get_name(), right_corner_62.get_name(),
     Edge(left_corner_62, right_corner_62, freeway, 'r', max_speed).get_time()),

    (right_corner_71.get_name(), left_corner_71.get_name(),
     Edge(right_corner_71, left_corner_71, city_express_road, 'l', max_speed).get_time()),
    (left_corner_72.get_name(), right_corner_72.get_name(),
     Edge(left_corner_72, right_corner_72, city_express_road, 'r', max_speed).get_time()),
    (right_corner_81.get_name(), left_corner_71.get_name(),
     Edge(right_corner_81, left_corner_71, city_express_road, 'l', max_speed).get_time()),
    (left_corner_82.get_name(), right_corner_72.get_name(),
     Edge(left_corner_82, right_corner_72, city_express_road, 'r', max_speed).get_time()),

    (right_corner_9.get_name(), left_corner_9.get_name(),
     Edge(right_corner_9, left_corner_9, highway, 'l', max_speed).get_time()),

    (
    house_11.get_name(), left_corner_10.get_name(), Edge(house_11, left_corner_10, highway, 'r', max_speed).get_time()),
    (right_corner_10.get_name(), house_11.get_name(),
     Edge(right_corner_10, house_11, highway, 'r', max_speed).get_time()),

    (left_corner_11.get_name(), bs_2.get_name(),
     Edge(left_corner_11, bs_2, simple_city_road, 'r', max_speed).get_time()),
    (bs_2.get_name(), bs_4.get_name(), Edge(bs_2, bs_4, simple_city_road, 'r', max_speed).get_time()),
    (bs_4.get_name(), right_corner_11.get_name(),
     Edge(bs_4, right_corner_11, simple_city_road, 'r', max_speed).get_time()),

    (bs_1.get_name(), left_corner_12.get_name(),
     Edge(bs_1, left_corner_12, simple_city_road, 'l', max_speed).get_time()),
    (bs_3.get_name(), bs_1.get_name(), Edge(bs_3, bs_1, simple_city_road, 'l', max_speed).get_time()),
    (right_corner_12.get_name(), bs_3.get_name(),
     Edge(right_corner_12, bs_3, simple_city_road, 'l', max_speed).get_time())
]

# print(graph)
print(dijkstra(graph, house_4.get_name(), trash.get_name()))
