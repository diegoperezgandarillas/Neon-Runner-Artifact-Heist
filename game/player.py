from .constants import *

class Player:
    """Represents the player character in the game."""
    
    def __init__(self, x, y):
        """
        Initialize a new player at the specified position.
        
        Args:
            x: Initial x-coordinate
            y: Initial y-coordinate
        """
        self.x = x
        self.y = y
        self.char = PLAYER_CHAR  # Visual character representation
        self.speed = PLAYER_SPEED  # Movement speed per frame
        self.health = PLAYER_START_HEALTH  # Current health points
        self.score = 0  # Player's accumulated score

    def move(self, dx, dy, max_x, max_y):
        """
        Move the player by the given delta values while keeping them within bounds.
        
        Args:
            dx: Change in x position (negative = left, positive = right)
            dy: Change in y position (negative = up, positive = down)
            max_x: Maximum x boundary (screen width)
            max_y: Maximum y boundary (screen height)
        """
        # Apply movement delta
        self.x += dx
        self.y += dy

        # Keep player on screen by clamping coordinates to valid bounds
        if self.x < 0:
            self.x = 0
        if self.x >= max_x:
            self.x = max_x - 1
        if self.y < 0:
            self.y = 0
        if self.y >= max_y:
            self.y = max_y - 1

    def take_damage(self, amount):
        """
        Reduce player health by the specified amount.
        
        Args:
            amount: Amount of damage to apply (positive number)
        """
        self.health -= amount
        # Prevent health from going below zero
        if self.health < 0:
            self.health = 0

    def add_score(self, amount):
        """
        Increase the player's score.
        
        Args:
            amount: Points to add to the score
        """
        self.score += amount