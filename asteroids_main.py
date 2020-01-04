from screen import Screen
import sys
import random
import math
from ship import Ship
from asteroid import Asteroid

DEFAULT_ASTEROIDS_NUM = 5


class GameRunner:

    def __init__(self, asteroids_amount):
        self.__screen = Screen()
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        ship_x = random.randint(self.__screen_min_x, self.__screen_max_x)
        ship_y = random.randint(self.__screen_min_y, self.__screen_max_y)
        self.__ship = Ship(ship_x, ship_y, 0, 0, 0.0)
        self.__asteroids = {}
        for i in range(asteroids_amount):
            self.__asteroids[i] = self.get_random_asteroid(self.__ship)
            self.__screen.register_asteroid(self.__asteroids[i], 3)

    def get_random_asteroid(self, ship):
        size = 3
        far_enough = False
        while not far_enough:
            asteroid_x = random.randint(self.__screen_min_x,
                                        self.__screen_max_x)
            asteroid_y = random.randint(self.__screen_min_y,
                                        self.__screen_max_y)
            speed_x, speed_y = random.randint(1, 5), random.randint(1, 5)
            asteroid = Asteroid(asteroid_x, asteroid_y, speed_x, speed_y, size)
            far_enough = not asteroid.has_intersection_with(ship)
        return asteroid

    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You should not to change this method!
        self._game_loop()
        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def _game_loop(self):
        ship = self.__ship
        screen = self.__screen
        self.draw_objects()
        if screen.is_up_pressed():
            angle = math.radians(ship.get_angle())
            ship.set_x_speed(ship.get_x_speed() + math.cos(angle))
            ship.set_y_speed(ship.get_y_speed() + math.sin(angle))
        if screen.is_left_pressed():
            ship.set_angle(ship.get_angle() + 7)
        if screen.is_right_pressed():
            ship.set_angle(ship.get_angle() - 7)
        self.move_objects()

    def draw_objects(self):
        ship = self.__ship
        screen = self.__screen
        asteroids = self.__asteroids
        screen.draw_ship(ship.get_x_place(), ship.get_y_place(),
                         ship.get_angle())
        for i in asteroids:
            screen.draw_asteroid(asteroids[i], asteroids[i].get_x_place(),
                                 asteroids[i].get_y_place())

    def move_objects(self):
        ship = self.__ship
        asteroids = self.__asteroids
        ship.set_x_place(self.set_place(ship.get_x_place(),
                                        ship.get_x_speed(), 'x'))
        ship.set_y_place(self.set_place(ship.get_y_place(),
                                        ship.get_y_speed(), 'y'))
        for i in asteroids:
            asteroids[i].set_x_place(self.set_place(asteroids[i].get_x_place(),
                                                    asteroids[i].get_x_speed(), 'x'))
            asteroids[i].set_y_place(self.set_place(asteroids[i].get_y_place(),
                                                    asteroids[i].get_y_speed(), 'x'))

    def set_place(self, spot, speed, direction):
        if direction == 'x':
            new_spot = Screen.SCREEN_MIN_X + \
                       (spot + speed - Screen.SCREEN_MIN_X) % \
                       (Screen.SCREEN_MAX_X - Screen.SCREEN_MIN_X)
            return new_spot
        elif direction == 'y':
            new_spot = Screen.SCREEN_MIN_Y + \
                       (spot + speed - Screen.SCREEN_MIN_Y) % \
                       (Screen.SCREEN_MAX_Y - Screen.SCREEN_MIN_Y)
            return new_spot


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
