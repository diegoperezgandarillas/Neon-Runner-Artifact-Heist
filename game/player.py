from .constants import *

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.char = PLAYER_CHAR
        self.speed = PLAYER_SPEED
        self.health = PLAYER_START_HEALTH
        self.score = 0

    def move(self, dx, dy, max_x, max_y):
        self.x += dx
        self.y += dy

        # Keep player on screen
        if self.x < 0:
            self.x = 0
        if self.x >= max_x:
            self.x = max_x - 1
        if self.y < 0:
            self.y = 0
        if self.y >= max_y:
            self.y = max_y - 1

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def add_score(self, amount):
        self.score += amount
