import unittest
from game_controller import GameController
from board import Board

# Jonah Golden
# Test file for GameController module

WIDTH = 800
HEIGHT = 800
SPACING = 100
BLACK = 0
WHITE = 255

class TestGameController(unittest.TestCase):
    
    def setUp(self):
        self.gc = GameController()

    def test_constructor(self):
        """Test the constructor method"""
        assert self.gc.WIDTH == WIDTH
        assert self.gc.HEIGHT == HEIGHT
        assert self.gc.SPACING == SPACING
        assert self.gc.player.color == BLACK
        assert self.gc.computer.color == WHITE
        assert self.gc.player_turn
        assert not self.gc.game_over
        assert not self.gc.do_prompt
        assert self.gc.last_move_time == 0.0
        assert self.gc.PAUSE_TIME == 0.7
        assert self.gc.user_name == ""
        assert self.gc.money_count == 1

    def test_start_game(self):
        """Test start_game method"""
        assert self.gc.board.total_disks == 0
        self.gc.start_game()
        assert self.gc.board.total_disks == 4

    def test_check_valid_moves(self):
        """Test check_valid_moves method"""
        assert self.gc.board.message == "Let the game begin! Your turn."
        self.gc.check_valid_moves()
        assert self.gc.board.message == "That's allllllll, folks"

    def test_player_move(self):
        """Test player_move method"""
        self.gc.start_game()
        assert not self.gc.player_move(700, 700)
        assert not self.gc.player_move(900, 900)
        assert self.gc.player_move(282, 305)
        assert not self.gc.player_move(399, 201)
        assert self.gc.board.rows[305//self.gc.SPACING][282//self.gc.SPACING].disk.color == 0
        assert self.gc.board.total_disks == 5
        assert not self.gc.player_turn
        assert self.gc.board.message == "Computer turn"

    def test_computer_move(self):
        """Test computer_move method"""
        self.gc.start_game()
        self.gc.player_move(282, 305)
        assert self.gc.computer_move()
        assert self.gc.board.total_disks == 6
        assert self.gc.board.message == "Your turn"

    def test_end_game(self):
        """Test end_game method"""
        self.gc.end_game()
        assert self.gc.game_over
        assert self.gc.do_prompt

    def test_high_score(self):
        """Test high_score method"""
        self.gc.board.total_black_disks = 65
        assert self.gc.high_score()

if __name__ == "__main__":
    unittest.main()