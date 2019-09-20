from computer import Computer
from board import Board

# Jonah Golden
# Test file for Computer module

WIDTH = 800
HEIGHT = 800
SPACING = 100
board = Board(WIDTH, HEIGHT, SPACING)

computer = Computer(board)


def test_constructor():
    """Test the constructor method"""
    assert computer.board == board
    assert computer.color == 255


def test_add_disk():
    """Test add_disk method"""
    computer.add_disk(board.tiles[1])
    assert board.total_disks == 1
    assert board.tiles[1].disk.color == computer.color


def test_swap():
    """Test swap method"""
    computer.swap([board.tiles[1]])
    assert board.tiles[1].disk.color != computer.color


def test_no_moves():
    """Test no moves method"""
    assert computer.no_moves()
    computer.add_disk(board.tiles[0])
    assert not computer.no_moves()


def test_first_disks():
    """Test first_disks method"""
    assert board.total_disks == 2
    computer.first_disks()
    assert board.total_disks == 4
    assert board.rows[3][3].disk.color == computer.color
    assert board.rows[4][4].disk.color == computer.color


def test_valid_move():
    """Test valid move method"""
    assert computer.valid_move(board.tiles[3]) == []
    board.add_disk(board.rows[3][4], 0)
    board.add_disk(board.rows[4][3], 0)
    assert len(computer.valid_move(board.rows[2][4])) == 1


def test_make_move():
    """Test make_move function"""
    assert board.total_disks == 6
    computer.make_move()
    assert board.total_disks == 7
