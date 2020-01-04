class Ship:
    __size = 1

    def __init__(self, x_place, y_place, x_speed,  y_speed, angle):
        self.__place = (x_place, y_place)
        self.__speed = (x_speed, y_speed)
        self.__angle = angle

    def get_place(self):
        return self.__place

    def get_speed(self):
        return self.__speed

    def get_angle(self):
        return self.__angle

    def set_place(self, place):
        self.__place = place

    def set_speed(self, speed):
        self.__speed = speed


    def set_angle(self, angle):
        self.__angle = angle

    def __len__(self):
        return self.__size
