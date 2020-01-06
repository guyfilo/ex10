class Torpedo:
    __size = 5

    def __init__(self, x_place, y_place, x_speed,  y_speed, angle):
        self.__x_place = x_place
        self.__y_place = y_place
        self.__x_speed = x_speed
        self.__y_speed = y_speed
        self.__angle = angle

    def get_place(self):
        return self.__x_place, self.__y_place

    def get_angle(self):
        return self.__angle

    def get_speed(self):
        return self.__x_speed, self.__y_speed

    def set_place(self, place):
        self.__x_place, self.__y_place = place

    def __len__(self):
        return self.__size
