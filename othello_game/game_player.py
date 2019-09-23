from abc import ABCMeta, abstractmethod

class GamePlayer:
    """Game player class. This contains code that is common to the player and
    computer classes."""

    def __init__(self, board, color):
        """Game player constructor with a board and a color for player's disks."""
        self.board = board
        self.color = color

    def add_disk(self, tile):
        """Add a disk to the board"""
        self.board.add_disk(tile, self.color)

    def swap(self, tiles):
        """Call board method swap on tiles to be swapped"""
        self.board.swap(tiles)

    def no_moves(self):
        """Return True if there are no valid moves"""
        # If there is a valid move, return false
        for tile in self.board.tiles:
            if (not tile.disk and self.valid_move(tile)):
                    return False
        return True

    def valid_move(self, tile):
        """Check if a tile without a disk is a valid move"""
        tiles_to_swap = []

        # Define a dictionary with each of 8 possible directions as the keys
        d = {(-1, -1): [],
             (-1, 0): [],
             (-1, 1): [],
             (0, 1): [],
             (1, 1): [],
             (1, 0): [],
             (1, -1): [],
             (0, -1): []}

        # Iterate through directions
        for line in d:

            # Reset row and col variables as the row and column of proposed
            # tile to make move on
            row = tile.row
            col = tile.column
            while True:

                # Set row and col of the next tile to look at
                row += line[0]
                col += line[1]

                # Break if next tile is off the board
                if not (0 <= row < len(self.board.rows) and
                        0 <= col < len(self.board.rows[row])):
                    break

                # Break if tile is empty
                if self.board.rows[row][col].disk is None:
                    break

                # Case where disk on next tile is of other color
                if self.board.rows[row][col].disk.color != self.color:
                    d[line].append(self.board.rows[row][col])

                # Case where disk on next tile is of same color
                elif self.board.rows[row][col].disk.color == self.color:

                    # Break if no tiles will be swapped
                    if len(d[line]) == 0:
                        break

                    # Case where this direction indicates a valid move
                    elif len(d[line]) > 0:
                        tiles_to_swap.extend(d[line])
                        break

        # Return empty list (False) if tile already has a disk
        # Return the tiles to swap from this move
        if tile.disk:
            return []
        else:
            return tiles_to_swap
