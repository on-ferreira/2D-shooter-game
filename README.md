# 2D Shooter Game

## Description
This is a simple 2D shooter game where the player can move around the screen and shoot at incoming enemies. The goal is to survive as long as possible by avoiding and destroying enemies. The game is built using the Pygame library.

## Features
- Player movement (up, down, left, right)
- Shooting bullets
- Enemy generation and movement
- Collision detection between bullets and enemies
- Score display in the top left corner

## Installation

### Prerequisites
- Python 3.x
- Pygame library

### Steps
1. Clone the repository:
   ```sh
   git clone <repository_url>
   ```

2. Navigate to the project directory:
   ```sh
   cd RTS
   ```

3. Create a virtual environment:
   ```sh
   python -m venv rts-venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```sh
     rts-venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```sh
     source rts-venv/bin/activate
     ```

5. Install the required dependencies:
   ```sh
   pip install pygame
   ```

## Usage

1. Make sure the virtual environment is activated.
2. Run the game:
   ```sh
   python game.py
   ```

## How to Play
- Use the arrow keys to move the player.
- Press the spacebar to shoot bullets.
- Avoid and shoot the red enemies to score points.
- The game ends if an enemy collides with the player.
