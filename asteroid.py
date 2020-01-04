class Asteroid:
    def __init__(self, x_place, y_place, x_speed, y_speed, size):
        self.__place = (x_place, y_place)
        self.__speed = (x_speed, y_speed)
        self.__size = size

    def get_place(self):
        return self.__place

    def get_speed(self):
        return self.__speed

    def set_place(self, place):
        self.__place = place

    def set_speed(self, speed):
        self.__speed = speed

    def has_intersection_with(self, obj):
        obj_plc = obj.get_place()
        distance = ((obj_plc[0] - self.__place[0])**2
                    + (obj_plc[1] - self.__place[1])**2) ** 0.5
        return distance <= self.__size + len(obj)

    def __len__(self):
        return self.__size*10 - 5
