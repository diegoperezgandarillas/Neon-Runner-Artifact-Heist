import random
from .player import Player
from .enemy import Enemy
from .coin import Coin
from .constants import *

class Level:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.enemies = []
        self.coins = []

        # The player is created
        self.player = Player(width // 2, height // 2)

        # Some timers
        self.enemy_spawn_timer = 0
        self.coin_spawn_timer = 0

    def update(self, dt):
        # Update enemies
        player_pos = (self.player.x, self.player.y)
        for enemy in self.enemies:
            enemy.update(player_pos, dt)

        # Handle spawning
        self._spawn_manager(dt)

        # Handle collisions
        self._handle_collisions()

    def _spawn_manager(self, dt):
        # Spawn enemies
        self.enemy_spawn_timer += dt
        if len(self.enemies) < MAX_ENEMIES and self.enemy_spawn_timer > ENEMY_SPAWN_RATE:
            self.enemy_spawn_timer = 0
            x = random.randint(0, self.width)
            y = random.choice([-1, self.height]) # Spawn off-screen
            self._spawn_enemy(x, y)

        # Some coins 
        self.coin_spawn_timer += dt
        if len(self.coins) < MAX_COINS and self.coin_spawn_timer > COIN_SPAWN_RATE:
            self.coin_spawn_timer = 0
            x = random.randint(1, self.width - 2)
            y = random.randint(1, self.height - 2)
            self._spawn_coin(x, y)

    def _spawn_enemy(self, x, y):
        enemy = Enemy(x, y)
        self.enemies.append(enemy)

    def _spawn_coin(self, x, y):
        coin = Coin(x, y)
        self.coins.append(coin)

    def _handle_collisions(self):
        player_pos_int = (int(self.player.x), int(self.player.y))

        # Player collides with enemies
        for enemy in self.enemies[:]:
            if (int(enemy.x), int(enemy.y)) == player_pos_int:
                self.player.take_damage(ENEMY_DAMAGE)
                self.enemies.remove(enemy)

        # Player collides with coins
        for coin in self.coins[:]:
            if (int(coin.x), int(coin.y)) == player_pos_int:
                self.player.add_score(COIN_SCORE)
                self.coins.remove(coin)