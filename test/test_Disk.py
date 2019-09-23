import unittest
from disk import Disk

# Jonah Golden
# Test file for Disk module

BLACK = 0
WHITE = 255

class TestDisk(unittest.TestCase): 

    def test_constructor(self):
        """Test the Disk constructor method"""
        disk = Disk(1, 1, BLACK)
        assert disk.row == 1
        assert disk.column == 1
        assert disk.color == BLACK


    def test_color_swap(self):
        """Test the color_swap method"""
        disk = Disk(1, 1, BLACK)
        disk.color_swap()
        assert disk.color == WHITE
        disk.color_swap()
        assert disk.color == BLACK

if __name__ == "__main__":
    unittest.main()