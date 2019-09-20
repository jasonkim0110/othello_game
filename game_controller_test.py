from game_controller import GameController
from board import Board

# Jonah Golden
# Test file for GameController module

WIDTH = 800
HEIGHT = 800
SPACING = 100
board = Board(WIDTH, HEIGHT, SPACING)

gc = GameController(WIDTH, HEIGHT, SPACING, board)


def test_constructor():
    """Test the constructor method"""
    assert gc.WIDTH == WIDTH
    assert gc.HEIGHT == HEIGHT
    assert gc.SPACING == SPACING
    assert gc.board == board
    assert gc.player.color == 0
    assert gc.computer.color == 255
    assert gc.player_turn
    assert not gc.game_over
    assert not gc.do_prompt
    assert gc.last_move_time == 0.0
    assert gc.PAUSE_TIME == 0.7
    assert gc.user_name == ""
    assert gc.money_count == 1


def test_start_game():
    """Test start_game method"""
    assert gc.board.total_disks == 0
    gc.start_game()
    assert gc.board.total_disks == 4


def test_check_valid_moves():
    """Test check_valid_moves method"""
    gc.check_valid_moves()
    assert gc.board.message == "Let the game begin! Your turn."
    board = Board(WIDTH, HEIGHT, SPACING)
    g_c = GameController(WIDTH, HEIGHT, SPACING, board)
    g_c.check_valid_moves()
    assert g_c.board.total_disks == 0
    assert g_c.board.message == "That's allllllll, folks"


def test_player_move():
    """Test player_move method"""
    assert not gc.player_move(700, 700)
    assert not gc.player_move(900, 900)
    assert gc.player_move(282, 305)
    assert not gc.player_move(399, 201)
    assert gc.board.rows[305//gc.SPACING][282//gc.SPACING].disk.color == 0
    assert gc.board.total_disks == 5
    assert not gc.player_turn
    assert gc.board.message == "Computer turn"


def test_computer_move():
    """Test computer_move method"""
    assert gc.computer_move()
    assert gc.board.total_disks == 6
    assert gc.player_turn
    assert gc.board.message == "Your turn"


def test_end_game():
    """Test end_game method"""
    gc.end_game()
    assert gc.game_over
    assert gc.do_prompt


def test_high_score():
    """Test high_score method"""
    gc.board.total_black_disks = 65
    assert gc.high_score()
