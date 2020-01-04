from screen import Screen
import sys
import random
from ship import Ship

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
        # TODO: Your code goes here
        ship = self.__ship
        screen = self.__screen
        screen.draw_ship(ship.get_x_place(), ship.get_y_place(),
                         ship.get_angle())
        if screen.is_left_pressed():
            ship.set_angle(ship.get_angle() + 7)
        if screen.is_right_pressed():
            ship.set_angle(ship.get_angle() - 7)
        if screen.is_up_pressed():
            ship.set_x_speed(ship.get_x_speed() + math.cos(ship.get_angle()))
            ship.set_y_speed(ship.get_y_speed() + math.sin(ship.get_angle()))
    
    def set_place(self, spot, speed, direction):
        if direction == 'x':
            new_spot = Screen.SCREEN_MIN_X + (spot + speed - Screen.SCREEN_MIN_X) % \
                       (Screen.SCREEN_MAX_X - Screen.SCREEN_MIN_X)
            return new_spot
        elif direction == 'y':
            new_spot = Screen.SCREEN_MIN_Y + (spot + speed - Screen.SCREEN_MIN_Y) % \
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
