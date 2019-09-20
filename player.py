from game_player import GamePlayer

# Jonah Golden
# A player class, which extends GamePlayer

BLACK = 0


class Player(GamePlayer):
    """A class for the player"""

    def __init__(self, board):
        """Player constructor. Takes board as input"""
        self.board = board
        self.color = BLACK

    def first_disks(self):
        """Add first two disks to board"""
        for tile in self.board.tiles:
            if ((tile.row == (self.board.WIDTH/self.board.SPACING)/2 and
                tile.column == (self.board.HEIGHT/self.board.SPACING)/2 - 1) or
                (tile.row == (self.board.WIDTH/self.board.SPACING)/2 - 1 and
                    tile.column == (self.board.HEIGHT/self.board.SPACING)/2)):
                self.add_disk(tile)

    def make_move(self, tile):
        """Make a move"""
        tiles_to_swap = self.valid_move(tile)
        self.swap(tiles_to_swap)
        self.add_disk(tile)
