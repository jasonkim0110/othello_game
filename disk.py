# Jonah Golden
# A disk class for Othello game


class Disk:
    """A disk class"""
    def __init__(self, row, column, color):
        """Disk constructor. Takes row, column, and color as inputs"""
        self.row = row
        self.column = column
        self.color = color

    def display(self):
        """Draws the disk"""
        DIAMETER = 90
        X_COORD = self.column * 100 + 50
        Y_COORD = self.row * 100 + 50
        fill(self.color)
        ellipse(X_COORD, Y_COORD, DIAMETER, DIAMETER)

    def color_swap(self):
        """Swap color of disk"""
        BLACK = 0
        WHITE = 255
        if self.color == BLACK:
            self.color = WHITE
        elif self.color == WHITE:
            self.color = BLACK
