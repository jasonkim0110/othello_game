import unittest
from player import Player
from board import Board

# Jonah Golden
# Test file for Player module

WIDTH = 800
HEIGHT = 800
SPACING = 100
BLACK = 0
WHITE = 255

class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        self.board = Board(WIDTH, HEIGHT, SPACING)
        self.player = Player(self.board, BLACK) 

    def test_constructor(self):
        """Test the constructor method"""
        assert self.player.board == self.board
        assert self.player.color == BLACK

    def test_add_disk(self):
        """Test add_disk method"""
        self.player.add_disk(self.board.tiles[1])
        assert self.board.total_disks == 1
        assert self.board.tiles[1].disk.color == self.player.color

    def test_swap(self):
        """Test swap method"""
        self.player.add_disk(self.board.tiles[1])
        self.player.swap([self.board.tiles[1]])
        assert self.board.tiles[1].disk.color != self.player.color

    def test_no_moves(self):
        """Test no moves method"""
        self.player.add_disk(self.board.tiles[1])
        self.player.swap([self.board.tiles[1]])
        assert self.player.no_moves()
        self.player.add_disk(self.board.tiles[0])
        assert not self.player.no_moves()

    def test_first_disks(self):
        """Test first_disks method"""
        self.player.add_disk(self.board.tiles[1])
        self.player.swap([self.board.tiles[1]])
        self.player.add_disk(self.board.tiles[0])
        assert self.board.total_disks == 2
        self.player.first_disks()
        assert self.board.total_disks == 4
        assert self.board.rows[3][4].disk.color == self.player.color
        assert self.board.rows[4][3].disk.color == self.player.color

    def test_valid_move(self):
        """Test valid move method"""
        self.player.first_disks()
        assert self.player.valid_move(self.board.tiles[3]) == []
        self.board.add_disk(self.board.rows[3][3], WHITE)
        self.board.add_disk(self.board.rows[4][4], WHITE)
        assert len(self.player.valid_move(self.board.rows[2][3])) == 1

    def test_make_move(self):
        """Test make_move function"""
        self.player.first_disks()
        self.board.add_disk(self.board.rows[3][3], WHITE)
        self.board.add_disk(self.board.rows[4][4], WHITE)
        assert self.board.total_disks == 4
        self.player.make_move(self.board.rows[2][3])
        assert self.board.total_disks == 5

if __name__ == "__main__":
    unittest.main()