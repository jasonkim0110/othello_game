import unittest
from board import Board
from game_controller import GameController

# Jonah Golden
# Test file for Board module

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board(800, 800, 100)

    def test_constructor(self):
        """Test the Board constructor method"""
        assert self.board.WIDTH == self.board.HEIGHT == 800
        assert self.board.SPACING == 100
        assert len(self.board.tiles) == 64
        assert len(self.board.rows) == 8
        for row in range(8):
            assert len(self.board.rows[row]) == 8
        assert self.board.total_disks == 0
        assert self.board.total_black_disks == 0
        assert self.board.total_white_disks == 0
        assert self.board.message == "Let the game begin! Your turn."
        assert self.board.end_message == ""
        assert not self.board.game_over

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


    def test_add_disk(self):
        """Test the add_disk method"""
        self.board.add_disk(self.board.tiles[0], 0)
        assert self.board.total_disks == 1
        assert self.board.rows[0][0].disk


    def test_swap(self):
        """Test the swap method"""
        self.board.add_disk(self.board.tiles[0], 0)
        tiles_to_swap = [self.board.tiles[0]]
        assert tiles_to_swap[0].disk.color == 0
        self.board.swap(tiles_to_swap)
        assert self.board.total_disks == 1
        assert tiles_to_swap[0].disk.color == 255
        self.board.add_disk(self.board.tiles[1], 0)
        tiles_to_swap = [self.board.tiles[0], self.board.tiles[1]]
        self.board.swap(tiles_to_swap)
        assert tiles_to_swap[0].disk.color == 0
        assert tiles_to_swap[1].disk.color == 255


    def test_count_disks(self):
        """Test the count_disks method"""
        self.board.add_disk(self.board.tiles[0], 0)
        self.board.add_disk(self.board.tiles[1], 255)
        self.board.count_disks()
        assert self.board.total_black_disks == 1
        assert self.board.total_white_disks == 1
        assert "Tie game!" in self.board.end_message

if __name__ == "__main__":
    unittest.main()
