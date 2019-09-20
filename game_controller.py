from board import Board
from player import Player
from computer import Computer
import time
import re

# Jonah Golden
# A game controller for Othello game


class GameController:
    """A game controller for Othello"""

    def __init__(self, WIDTH, HEIGHT, SPACING): # , board):
        """GameController constructor. Takes Width, Height, Spacing, and board
        as inputs"""
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SPACING = SPACING
        self.board = Board(WIDTH, HEIGHT, SPACING) # board
        self.player = Player(self.board)
        self.computer = Computer(self.board)
        self.player_turn = True
        self.game_over = False
        self.do_prompt = False
        self.last_move_time = 0.0
        self.PAUSE_TIME = 0.7
        self.user_name = ""
        self.money_count = 1

    def start_game(self):
        """Start the game, place the first tiles"""
        self.player.first_disks()
        self.computer.first_disks()

    def check_valid_moves(self):
        """Handle case where there are no valid moves for the current turn"""
        if not self.game_over:
            if (self.player.no_moves() and self.computer.no_moves()):
                self.board.message = "That's allllllll, folks"
                self.end_game()
            elif (self.player_turn and self.player.no_moves()):
                self.last_move_time = time.time() + self.PAUSE_TIME
                self.player_turn = False
                self.board.message = "No valid moves. Computer turn."
            elif (not self.player_turn and self.computer.no_moves()):
                self.player_turn = True
                self.board.message = "No valid moves. Your turn."

    def player_move(self, x, y):
        """Takes x and y coordinates of mouse click as input. Add disk if tile
        is empty, end game if board is full."""
        if (x < self.WIDTH and y < self.HEIGHT):
            row = y//self.SPACING
            col = x//self.SPACING
            tile = self.board.rows[row][col]

            # Make move if click is a valid move and it's player's turn and 
            if (self.player_turn and self.player.valid_move(tile)):
                self.player.make_move(tile)
                self.player_turn = False
                self.last_move_time = time.time()
                self.board.message = "Computer turn"
                return True
        else:
            return False

    def computer_move(self):
        """Call computer to make a move if it is computer's move"""
        if (self.game_over or self.player_turn):
            return False
        else:
            self.computer.make_move()
            self.player_turn = True
            self.board.message = "Your turn"
            return True

    def update(self):
        """Updates to make in draw function"""
        # Prompt for username when game is over
        if self.do_prompt:
            self.prompt()
            self.do_prompt = False

        # Check for valid moves and display the board
        self.check_valid_moves()
        self.board.display()

        # Actions if the game is over
        if self.game_over:
            self.board.end_game()
            if not self.do_prompt:
                self.print_score()

            self.board.message = "$"*self.money_count
            if self.money_count < 80:
                self.money_count += 1
            else:
                self.money_count = 0

    def end_game(self):
        """Execute game over changes"""
        self.game_over = True
        self.do_prompt = True
        self.board.count_disks()
        if self.high_score():
            self.board.end_message += "That's a high score!"

    def prompt(self):
        """Prompt user for name and add score to scores file"""
        # Sleep before prompt
        time.sleep(self.PAUSE_TIME)
        self.user_name = self.input("Enter your name:")

        # Record score only if username of at least one char was entered 
        if (self.user_name and len(self.user_name) > 0):
            self.record_score()

    def record_score(self):
        """Record score in scores.txt"""
        with open('scores.txt', 'r') as f:
            previous_scores = f.read()
        
        # Write at top of scores if it's a high score
        if self.high_score():
            with open('scores.txt', 'w') as f:
                f.write(self.user_name + " " +
                        str(self.board.total_black_disks) + "\n")
                f.write(previous_scores)
        
        # Write at bottom of scores if it's not a high score
        else:
            with open('scores.txt', 'a') as f:
                f.write(self.user_name + " " +
                        str(self.board.total_black_disks) + "\n")

    def high_score(self):
        """Check if score is a high score"""
        with open('scores.txt', 'r') as f:
            previous_scores = f.read()
            for score in re.findall(r'(\d+)\n', previous_scores):
                if self.board.total_black_disks <= int(score):
                    return False
        return True

    def print_score(self):
        """Print message after prompt is completed"""
        if (self.user_name and len(self.user_name) > 0):
            message = ("Score recorded:\n" + str(self.user_name) +
                       ", " + str(self.board.total_black_disks))
        else:
            message = "No name entered, score not recorded."
        textSize(self.HEIGHT/12)
        textAlign(CENTER)
        fill(0)
        text(message, 4, self.HEIGHT/2, self.WIDTH - 4, self.HEIGHT/4)
        fill(86, 92, 160)
        text(message, 6, self.HEIGHT/2 + 2, self.WIDTH - 6, self.HEIGHT/4)

    def input(self, message=''):
        """Takes a string that will prompt user, returns user input"""
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)
