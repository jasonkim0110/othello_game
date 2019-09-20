from player import Player
from board import Board

# Jonah Golden
# Test file for Player module

WIDTH = 800
HEIGHT = 800
SPACING = 100
board = Board(WIDTH, HEIGHT, SPACING)

player = Player(board)


def test_constructor():
    """Test the constructor method"""
    assert player.board == board
    assert player.color == 0


def test_add_disk():
    """Test add_disk method"""
    player.add_disk(board.tiles[1])
    assert board.total_disks == 1
    assert board.tiles[1].disk.color == player.color


def test_swap():
    """Test swap method"""
    player.swap([board.tiles[1]])
    assert board.tiles[1].disk.color != player.color


def test_no_moves():
    """Test no moves method"""
    assert player.no_moves()
    player.add_disk(board.tiles[0])
    assert not player.no_moves()


def test_first_disks():
    """Test first_disks method"""
    assert board.total_disks == 2
    player.first_disks()
    assert board.total_disks == 4
    assert board.rows[3][4].disk.color == player.color
    assert board.rows[4][3].disk.color == player.color


def test_valid_move():
    """Test valid move method"""
    assert player.valid_move(board.tiles[3]) == []
    board.add_disk(board.rows[3][3], 255)
    board.add_disk(board.rows[4][4], 255)
    assert len(player.valid_move(board.rows[2][3])) == 1


def test_make_move():
    """Test make_move function"""
    assert board.total_disks == 6
    player.make_move(board.rows[2][3])
    assert board.total_disks == 7
