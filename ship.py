class Ship:
    def __init__(self, x_place, y_place, x_speed,  y_speed, angle):
        self.__x_place = x_place
        self.__y_place = y_place
        self.__x_speed = x_speed
        self.__y_speed = y_speed
        self.__angle = angle

    def get_x_place(self):
        return self.__x_place

    def get_y_place(self):
        return self.__y_place

    def get_x_speed(self):
        return self.__x_speed

    def get_y_speed(self):
        return self.__y_speed

    def set_x_place(self, place):
        self.__x_place = place
        
    def set_y_place(self, place):    
        self.__y_place = place

    def set_x_speed(self, speed):
        self.__x_speed = speed

     def set_y_speed(self, speed):
        self.__y_place = speed

    def set_angle(self, angle):
        self.__angle = angle
