class Asteroid:
    def __init__(self, x_place, y_place, x_speed, y_speed, size):
        self.__x_place = x_place
        self.__y_place = y_place
        self.__x_speed = x_speed
        self.__y_speed = y_speed
        self.__size = size

    def get_place(self):
        return self.__x_place, self.__y_place

    def get_speed(self):
        return self.__x_speed, self.__y_speed

    def set_place(self, place):
        self.__x_place = place[0]
        self.__y_place = place[1]

    def set_speed(self, speed):
        self.__x_speed = speed[0]
        self.__y_speed = speed[1]

    def has_intersection_with(self, obj):
        obj_place = obj.get_place()
        distance = ((obj_place[0] - self.__x_place)**2
                    + (obj_place[1] - self.__y_place)**2) ** 0.5
        return distance <= self.__size + len(obj)

    def __len__(self):
        return self.__size*10 - 5

    def __str__(self):
        return str(self.__x_place) + ' ' + str(self.__y_place)
