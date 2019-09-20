from board import Board
from game_controller import GameController

# Jonah Golden
# Test file for Board module

board = Board(800, 800, 100)


def test_constructor():
    """Test the Board constructor method"""
    assert board.WIDTH == board.HEIGHT == 800
    assert board.SPACING == 100
    assert len(board.tiles) == 64
    assert len(board.rows) == 8
    for row in range(8):
        assert len(board.rows[row]) == 8
    assert board.total_disks == 0
    assert board.total_black_disks == 0
    assert board.total_white_disks == 0
    assert board.message == "Let the game begin! Your turn."
    assert board.end_message == ""
    assert not board.game_over

    short_board = Board(400, 400, 100)
    assert len(short_board.tiles) == 16
    assert len(short_board.rows) == 4
    for row in range(4):
        assert len(short_board.rows[row]) == 4

    short_board = Board(200, 200, 100)
    assert len(short_board.tiles) == 4
    assert len(short_board.rows) == 2
    for row in range(2):
        assert len(short_board.rows[row]) == 2


def test_add_disk():
    """Test the add_disk method"""
    board.add_disk(board.tiles[0], 0)
    assert board.total_disks == 1
    assert board.rows[0][0].disk


def test_swap():
    """Test the swap method"""
    tiles_to_swap = [board.tiles[0]]
    assert tiles_to_swap[0].disk.color == 0
    board.swap(tiles_to_swap)
    assert board.total_disks == 1
    assert tiles_to_swap[0].disk.color == 255
    board.add_disk(board.tiles[1], 0)
    tiles_to_swap = [board.tiles[0], board.tiles[1]]
    board.swap(tiles_to_swap)
    assert tiles_to_swap[0].disk.color == 0
    assert tiles_to_swap[1].disk.color == 255


def test_count_disks():
    """Test the count_disks method"""
    board.count_disks()
    assert board.total_black_disks == 1
    assert board.total_white_disks == 1
    assert "Tie game!" in board.end_message
