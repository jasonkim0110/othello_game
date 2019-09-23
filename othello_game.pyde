from game_controller import GameController
import time

# Jonah Golden
# An Othello game

# Set constants
COMP_TIME_DELAY = 0.7

# Initiate game controller and board
game_controller = GameController()

def setup():
    size(WIDTH + 200, HEIGHT)
    game_controller.start_game()


def draw():
    game_controller.update()
    if time.time() >= game_controller.last_move_time + COMP_TIME_DELAY:
        game_controller.computer_move()


def mousePressed():
    game_controller.player_move(mouseX, mouseY)
