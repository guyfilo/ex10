class Asteroid:
    def __init__(self, x_place, y_place, x_speed, y_speed, size):
        self.__x_place = x_place
        self.__y_place = y_place
        self.__x_speed = x_speed
        self.__y_speed = y_speed
        self.__size = size

    def get_x_place(self):
        return self.__x_place

    def get_y_place(self):
        return self.__y_place

    def get_x_speed(self):
        return self.__x_speed

    def get_y_speed(self):
        return self.__y_speed

    def set_x_place(self, x_place):
        self.__x_place = x_place

    def set_y_place(self, y_place):
        self.__y_place = y_place

    def set_x_speed(self, x_speed):
        self.__x_speed = x_speed

    def set_y_speed(self, y_speed):
        self.__y_speed = y_speed

    def has_intersection_with(self, obj):
        distance = ((obj.get_x_place() - self.__x_place)**2
                    + (obj.get_y_place() - self.__y_place)**2) ** 0.5
        return distance <= self.__size + len(obj)

    def __len__(self):
        return self.__size*10 - 5

    def __str__(self):
        return str(self.__x_place) + ' ' + str(self.__y_place)
