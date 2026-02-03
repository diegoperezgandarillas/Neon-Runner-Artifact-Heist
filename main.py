import curses
from game.level import Level
from game.hud import HUD
from game.constants import *
import time

class Game:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        curses.curs_set(0)  # Hide cursor
        self.stdscr.nodelay(True) # Non-blocking input
        self.stdscr.timeout(100)

        # Setup colors
        curses.start_color()
        curses.init_pair(PLAYER_COLOR_PAIR, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(ENEMY_COLOR_PAIR, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(COIN_COLOR_PAIR, curses.COLOR_YELLOW, curses.COLOR_BLACK)

        self.running = True
        self.game_over = False
        self.game_time = 0

        self.reset_game()

    def run(self):
        last_time = time.time()
        while self.running:
            current_time = time.time()
            dt = current_time - last_time
            last_time = current_time

            self.handle_events(dt)
            self.update(dt)
            self.draw()

            # Frame rate limiting
            time.sleep(max(1./FPS - (time.time() - current_time), 0))

    #def handle_events(self):
    def handle_events(self, dt):
        key = self.stdscr.getch()
        height, width = self.stdscr.getmaxyx()

        if self.game_over:
            if key == ord('r'):
                self.reset_game()
            elif key == ord('q'):
                self.running = False
        else:
            if key == ord('q'):
                self.running = False
            elif key == curses.KEY_LEFT or key == ord('a'):
                self.level.player.move(-1, 0, width, height)
            elif key == curses.KEY_RIGHT or key == ord('d'):
                self.level.player.move(1, 0, width, height)
            elif key == curses.KEY_UP or key == ord('w'):
                self.level.player.move(0, -1, width, height)
            elif key == curses.KEY_DOWN or key == ord('s'):
                self.level.player.move(0, 1, width, height)

    def update(self, dt):
        if not self.game_over:
            self.level.update(dt)
            self.game_time += dt
            if self.level.player.health <= 0:
                self.game_over = True

    def draw(self):
        self.stdscr.erase()
        height, width = self.stdscr.getmaxyx()

        # Draw game objects
        p = self.level.player
        px, py = int(p.x), int(p.y)
        if 0 <= py < height and 0 <= px < width:
            self.stdscr.addstr(py, px, p.char, curses.color_pair(PLAYER_COLOR_PAIR))

        for enemy in self.level.enemies:
            ex, ey = int(enemy.x), int(enemy.y)
            if 0 <= ey < height and 0 <= ex < width:
                self.stdscr.addstr(ey, ex, enemy.char, curses.color_pair(ENEMY_COLOR_PAIR))

        for coin in self.level.coins:
            cx, cy = int(coin.x), int(coin.y)
            if 0 <= cy < height and 0 <= cx < width:
                self.stdscr.addstr(cy, cx, coin.char, curses.color_pair(COIN_COLOR_PAIR))

        self.hud.draw(self.level.player, self.game_time)

        if self.game_over:
            self.hud.draw_game_over()

        self.stdscr.refresh()

    def reset_game(self):
        height, width = self.stdscr.getmaxyx()
        self.game_over = False
        self.game_time = 0
        self.level = Level(width, height)
        self.hud = HUD(self.stdscr)

def main(stdscr):
    game = Game(stdscr)
    game.run()

if __name__ == "__main__":
    curses.wrapper(main)
