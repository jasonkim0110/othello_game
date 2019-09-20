from game_controller import GameController
import time

# Jonah Golden
# An Othello game

# Set constants
WIDTH = 800
HEIGHT = 800
SPACING = 100
COMP_TIME_DELAY = 0.7

# Initiate board and game controller
game_controller = GameController(WIDTH, HEIGHT, SPACING)

def setup():
    size(WIDTH + 200, HEIGHT)
    game_controller.start_game()


def draw():
    game_controller.update()
    if time.time() >= game_controller.last_move_time + COMP_TIME_DELAY:
        game_controller.computer_move()


def mousePressed():
    game_controller.player_move(mouseX, mouseY)
