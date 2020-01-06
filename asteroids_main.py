from screen import Screen
import sys
import random
import math
from ship import Ship
from asteroid import Asteroid
from torpedo import Torpedo

DEFAULT_ASTEROIDS_NUM = 5
SCORE_BY_SIZE = {1: 100, 2: 50, 3: 20}


class GameRunner:

    def __init__(self, asteroids_amount):
        self.__asteroids_amount = asteroids_amount
        self.__asteroids_index = asteroids_amount + 1
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
        self.__torpedoes = []

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
        self.draw_objects()
        self.keyboard_interactions()
        self.move_objects()

    def keyboard_interactions(self):
        ship = self.__ship
        screen = self.__screen
        if screen.is_up_pressed():
            angle = math.radians(ship.get_angle())
            ship.set_speed((ship.get_speed()[0] + math.cos(angle)
                           , ship.get_speed()[1] + math.sin(angle)))
        if screen.is_left_pressed():
            ship.set_angle(ship.get_angle() + 7)
        if screen.is_right_pressed():
            ship.set_angle(ship.get_angle() - 7)
        if screen.is_space_pressed():
            torpedoes_num = len(self.__torpedoes)
            if torpedoes_num < 10:
                self.add_torpedo()

    def add_torpedo(self):
        ship = self.__ship
        torpedoes = self.__torpedoes
        ship_place = ship.get_place()
        ship_speed = ship.get_speed()
        ship_angle = ship.get_angle()
        torpedo_speed_x = ship_speed[0] + \
                          2 * math.cos(math.radians(ship_angle))
        torpedo_speed_y = ship_speed[1] + \
                          2 * math.sin(math.radians(ship_angle))
        torpedo = Torpedo(ship_place[0], ship_place[1],
                          torpedo_speed_x, torpedo_speed_y,
                          ship_angle)
        torpedoes.append([torpedo, 0])
        self.__screen.register_torpedo(torpedo)

    def draw_objects(self):
        ship = self.__ship
        screen = self.__screen
        asteroids = self.__asteroids
        torpedoes = self.__torpedoes
        screen.draw_ship(ship.get_place()[0], ship.get_place()[1],
                         ship.get_angle())
        for i in asteroids:
            screen.draw_asteroid(asteroids[i], asteroids[i].get_place()[0],
                                 asteroids[i].get_place()[1])
        for torpedo in torpedoes:
            screen.draw_torpedo(torpedo[0],
                                torpedo[0].get_place()[0],
                                torpedo[0].get_place()[1],
                                torpedo[0].get_angle())

    def move_objects(self):
        ship = self.__ship
        asteroids = self.__asteroids
        torpedoes = self.__torpedoes
        ship_p = ship.get_place()
        ship_s = ship.get_speed()
        ship.set_place(self.set_place(ship_p, ship_s))
        asteroids_crashed = []
        old_torpedoes = []
        for i in asteroids:
            asteroids[i].set_place(self.set_place(asteroids[i].get_place(),
                                                  asteroids[i].get_speed()))
            if self.intersection_with_ship(ship, asteroids[i]):
                asteroids_crashed.append(i)
        for j in asteroids_crashed:
            del asteroids[j]
        for k in range(len(torpedoes)):
            torpedo = torpedoes[k]
            self.intersection_with_torpedo(torpedo[0])
            torpedo[0].set_place(self.set_place(torpedo[0].get_place(),
                                                torpedo[0].get_speed()))
            torpedo[1] += 1
            if torpedo[1] >= 200:
                old_torpedoes.append(k)
        for j in old_torpedoes:
            self.__screen.unregister_torpedo(torpedoes[j][0])
            torpedoes.remove(torpedoes[j])

    def intersection_with_torpedo(self, torpedo):
        asteroids = self.__asteroids
        crashed_asteroids = []
        for i in asteroids:
            if asteroids[i].has_intersection_with(torpedo):
                crashed_asteroids.append(i)
        for i in crashed_asteroids:
            self.split_asteroid(asteroids[i], i, torpedo.get_speed())

    def split_asteroid(self, asteroid, index, trpdo_speed):
        size = asteroid.get_size()
        self.__ship.add_score(SCORE_BY_SIZE[size])
        self.__screen.set_score(self.__ship.get_score())
        asteroids = self.__asteroids
        self.__screen.unregister_asteroid(asteroid)
        if size in [2,3]:
            ast_speed = asteroid.get_speed()
            ast_plc = asteroid.get_place()
            const = ((ast_speed[0])**2 + (ast_speed[1])**2)**0.5
            speed_x = (trpdo_speed[0] + ast_speed[0]) / const
            speed_y = (trpdo_speed[1] + ast_speed[1]) / const
            asteroids[self.__asteroids_index] = Asteroid(ast_plc[0], ast_plc[1], speed_x, speed_y, size-1)
            self.__screen.register_asteroid(asteroids[self.__asteroids_index], size - 1)
            self.__asteroids_index += 1
            asteroids[self.__asteroids_index] = Asteroid(ast_plc[0], ast_plc[1], -1 * speed_x, -1 * speed_y, size - 1)
            self.__screen.register_asteroid(asteroids[self.__asteroids_index], size - 1)
            self.__asteroids_index += 1
        del asteroids[index]

    def set_place(self, spot, speed):
            new_x_spot = Screen.SCREEN_MIN_X + \
                       (spot[0] + speed[0] - Screen.SCREEN_MIN_X) % \
                       (Screen.SCREEN_MAX_X - Screen.SCREEN_MIN_X)
            new__y_spot = Screen.SCREEN_MIN_Y + \
                       (spot[1] + speed[1] - Screen.SCREEN_MIN_Y) % \
                       (Screen.SCREEN_MAX_Y - Screen.SCREEN_MIN_Y)
            return (new_x_spot, new__y_spot)

    def intersection_with_ship(self, ship, asteroid):
        if asteroid.has_intersection_with(ship):
            self.__screen.show_message('ouch!', 'your ship got hit')
            ship.lower_hit_point()
            self.__screen.remove_life()
            self.__screen.unregister_asteroid(asteroid)
            return True
        return False


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
