from game_player import GamePlayer

# Jonah Golden
# A computer player class, which extendes GamePlayer

class Computer(GamePlayer):
    """A class for the computer player"""

    def first_disks(self):
        """Add first two disks to board"""
        for tile in self.board.tiles:
            if ((tile.row == (self.board.WIDTH/self.board.SPACING)/2 - 1 and
                tile.column == (self.board.HEIGHT/self.board.SPACING)/2 - 1) or
                (tile.row == (self.board.WIDTH/self.board.SPACING)/2 and
                    tile.column == (self.board.HEIGHT/self.board.SPACING)/2)):
                self.add_disk(tile)

    def make_move(self):
        """Make a valid move"""
        move = {'tile': None,
                'tiles to swap': []}

        # Loop through tiles of board, replacing 'move' if move on that tile
        # would swap more disks than previous best move
        for tile in self.board.tiles:
            if len(self.valid_move(tile)) > len(move['tiles to swap']):
                move['tile'] = tile
                move['tiles to swap'] = self.valid_move(tile)
        
        # Make best move
        self.swap(move['tiles to swap'])
        self.add_disk(move['tile'])
