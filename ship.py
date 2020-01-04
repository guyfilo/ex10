class Ship:
    def __init__(self, x_place, y_place, x_speed,  y_speed, angle):
        self.__x_place = x_place
        self.__y_place = y_place
        self.__x_speed = x_speed
        self.__y_speed = y_speed
        self.__angle = angle

    def get_place(self):
        return (self.__x_place, self.__y_place)

    def get_speed(self):
        return (self.__y_speed, self.__y_speed)

    def set_place(self, place):
        self.__x_place = place[0]
        self.__y_place = place[1]

    def set_speed(self, speed):
        self.__x_place = speed[0]
        self.__y_place = speed[1]
       
    def set_angle(self, angle):
        self.__angle = angle

    def get_angle(self):
        return self.__angle
