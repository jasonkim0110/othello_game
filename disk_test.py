from disk import Disk

# Jonah Golden
# Test file for Disk module


def test_constructor():
    """Test the Disk constructor method"""
    BLACK = 0
    disk = Disk(1, 1, 0)
    assert disk.row == 1
    assert disk.column == 1
    assert disk.color == BLACK


def test_color_swap():
    """Test the color_swap method"""
    BLACK = 0
    WHITE = 255
    disk = Disk(1, 1, BLACK)
    disk.color_swap()
    assert disk.color == WHITE
    disk.color_swap()
    assert disk.color == BLACK
