import curses

class HUD:
    def __init__(self, stdscr):
        self.stdscr = stdscr

    def draw(self, player, game_time):
        height, width = self.stdscr.getmaxyx()

        # Draw Score
        self.stdscr.addstr(0, 1, f"Score: {player.score}")

        # Draw Health
        self.stdscr.addstr(1, 1, f"Health: {player.health}")

        # Draw Timer
        timer_text = f"Time: {int(game_time)}"
        self.stdscr.addstr(0, width - len(timer_text) - 2, timer_text)

    def draw_game_over(self):
        height, width = self.stdscr.getmaxyx()
        game_over_txt = "GAME OVER!!!!"
        restart_txt = "Press 'r' to Restart or 'q' to Quit"
        self.stdscr.addstr(height // 2 - 1, width // 2 - len(game_over_txt) // 2, game_over_txt)
        self.stdscr.addstr(height // 2 + 1, width // 2 - len(restart_txt) // 2, restart_txt)
