from disk import Disk

# Jonah Golden
# A tile class for Othello game


class Tile:
    """A class for a tile of the Othello board"""

    def __init__(self, row, column):
        """Tile constructor. Takes row and column as inputs"""
        self.row = row
        self.column = column
        self.disk = None

    def add_disk(self, color):
        """Add disk to tile"""
        self.disk = Disk(self.row, self.column, color)

    def tile_swap(self):
        """Change color of disk on this tile"""
        if self.disk:
            self.disk.color_swap()
            return True
        else:
            print("This tile has no disk to color swap!")
            return False
    
    def __repr__(self):
        "Represents a tile with the row, col, and disk."
        return ("[" + str(self.row)
                + ", " + str(self.column)
                + "]: " + str(self.disk))

