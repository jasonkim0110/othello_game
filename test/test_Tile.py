import unittest
from tile import Tile

# Jonah Golden
# Test file for Tile module

BLACK = 0
WHITE = 255

class TestTile(unittest.TestCase):

    def setUp(self):
        self.tile = Tile(1, 1)

    def test_constructor(self):
        """Test the Tile constructor method"""
        assert self.tile.row == 1
        assert self.tile.column == 1
        assert not self.tile.disk


    def test_add_disk(self):
        """Test the add_disk method"""
        self.tile.add_disk(0)
        assert self.tile.disk


    def test_tile_swap(self):
        """Test the tile_swap method"""
        assert not self.tile.tile_swap()
        self.tile.add_disk(BLACK)
        assert self.tile.disk.color == BLACK
        assert self.tile.tile_swap()
        assert self.tile.disk.color == WHITE

if __name__ == "__main__":
    unittest.main()