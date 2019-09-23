import unittest
from computer import Computer
from board import Board

# Jonah Golden
# Test file for Computer module

WIDTH = 800
HEIGHT = 800
SPACING = 100
WHITE = 255

class TestComputer(unittest.TestCase):

    def setUp(self):
        self.board = Board(WIDTH, HEIGHT, SPACING)
        self.computer = Computer(self.board, WHITE)
    
    def test_constructor(self):
        """Test the constructor method"""
        assert self.computer.board == self.board
        assert self.computer.color == 255

    def test_add_disk(self):
        """Test add_disk method"""
        self.computer.add_disk(self.board.tiles[1])
        assert self.board.total_disks == 1
        assert self.board.tiles[1].disk.color == self.computer.color

    def test_swap(self):
        """Test swap method"""
        self.computer.add_disk(self.board.tiles[1])
        self.computer.swap([self.board.tiles[1]])
        assert self.board.tiles[1].disk.color != self.computer.color

    def test_no_moves(self):
        """Test no moves method"""
        assert self.computer.no_moves()
        self.computer.first_disks()
        self.board.add_disk(self.board.rows[3][4], 0)
        self.board.add_disk(self.board.rows[4][3], 0)
        assert not self.computer.no_moves()

    def test_first_disks(self):
        """Test first_disks method"""
        self.computer.first_disks()
        assert self.board.total_disks == 2
        assert self.board.rows[3][3].disk.color == self.computer.color
        assert self.board.rows[4][4].disk.color == self.computer.color

    def test_valid_move(self):
        """Test valid move method"""
        self.computer.first_disks()
        assert self.computer.valid_move(self.board.tiles[3]) == []
        self.board.add_disk(self.board.rows[3][4], 0)
        self.board.add_disk(self.board.rows[4][3], 0)
        assert len(self.computer.valid_move(self.board.rows[2][4])) == 1

    def test_make_move(self):
        """Test make_move function"""
        self.computer.first_disks()
        self.board.add_disk(self.board.rows[3][4], 0)
        self.board.add_disk(self.board.rows[4][3], 0)
        assert self.board.total_disks == 4
        self.computer.make_move()
        assert self.board.total_disks == 5

if __name__ == "__main__":
    unittest.main()