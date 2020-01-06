class Ship:
    __size = 10
    __default_hp = 3

    def __init__(self, x_place, y_place, x_speed,  y_speed, angle):
        self.__x_place = x_place
        self.__y_place = y_place
        self.__x_speed = x_speed
        self.__y_speed = y_speed
        self.__angle = angle
        self.__hit_points = self.__default_hp
        self.__score = 0

    def get_place(self):
        return self.__x_place, self.__y_place

    def get_speed(self):
        return self.__x_speed, self.__y_speed

    def get_angle(self):
        return self.__angle

    def set_place(self, place):
        self.__x_place = place[0]
        self.__y_place = place[1]

    def set_speed(self, speed):
        self.__x_speed = speed[0]
        self.__y_speed = speed[1]

    def set_angle(self, angle):
        self.__angle = angle

    def lower_hit_point(self):
        self.__hit_points -= 1

    def get_score(self):
        return self.__score

    def add_score(self, points):
        self.__score += points

    def __len__(self):
        return self.__size
