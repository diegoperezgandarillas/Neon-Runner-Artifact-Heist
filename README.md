# Neon Runner: Artifact Heist

## Description

Neon Runner: Artifact Heist is a fast-paced, retro-style arcade game that runs directly in your terminal. Navigate a neon-drenched grid, collect valuable artifacts, and dodge relentless enemies in a thrilling chase for the high score.

## Gameplay

The objective of the game is to collect as many artifacts (represented by yellow characters) as possible while avoiding contact with enemies (represented by magenta characters). Your health decreases upon contact with an enemy. The game ends when your health reaches zero.

### Game Elements

*   **Player:** The character you control (cyan).
*   **Enemies:** Moving obstacles that will deplete your health on contact.
*   **Artifacts:** Collectible items that increase your score.

## Controls

*   **Move Up:** `w` or `Up Arrow`
*   **Move Down:** `s` or `Down Arrow`
*   **Move Left:** `a` or `Left Arrow`
*   **Move Right:** `d` or `Right Arrow`
*   **Quit Game:** `q`
*   **Restart Game (after Game Over):** `r`

## Requirements

*   Python 3
*   A terminal that supports the `curses` library (standard on Linux and macOS).

Note: This game may not run on native Windows Command Prompt or PowerShell due to its reliance on the `curses` library. It can be run on Windows using the Windows Subsystem for Linux (WSL).

## How to Run

1.  Navigate to the project directory in your terminal.
2.  Run the game using the following command:
    ```sh
    python3 main.py
    ```
