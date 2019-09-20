from tile import Tile

# Jonah Golden
# Test file for Tile module


def test_constructor():
    """Test the Tile constructor method"""
    tile = Tile(1, 1)
    assert tile.row == 1
    assert tile.column == 1
    assert not tile.disk


def test_add_disk():
    """Test the add_disk method"""
    tile = Tile(1, 1)
    tile.add_disk(0)
    assert tile.disk


def test_tile_swap():
    """Test the tile_swap method"""
    BLACK = 0
    WHITE = 255
    tile = Tile(1, 1)
    assert not tile.tile_swap()
    tile.add_disk(BLACK)
    assert tile.disk.color == BLACK
    assert tile.tile_swap()
    assert tile.disk.color == WHITE
