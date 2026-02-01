import math
from .constants import *

class Enemy:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.char = ENEMY_CHAR
        self.speed = ENEMY_SPEED

    def update(self, player_pos, dt):
        # Chase AI that moves on one axis at a time
        dx = player_pos[0] - self.x
        dy = player_pos[1] - self.y

        # Decide whether to move horizontally or vertically based on which distance is greater
        if abs(dx) > abs(dy):
            # Move horizontally
            if dx > 0:
                self.x += self.speed * dt
            else:
                self.x -= self.speed * dt
        elif abs(dy) > 0:  # Use elif to avoid moving diagonally when dx and dy are equal
            # Move vertically
            if dy > 0:
                self.y += self.speed * dt
            else:
                self.y -= self.speed * dt
