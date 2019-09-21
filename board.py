from tile import Tile

# Jonah Golden
# A board for the othello game

class Board():
    """A class for an Othello board"""

    def __init__(self, WIDTH, HEIGHT, SPACING):
        """Board constructor.
        Takes Width, Height, and Spacing of board as inputs"""
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SPACING = SPACING
        self.tiles = [Tile(row, column)
                      for row in range(0, HEIGHT//SPACING)
                      for column in range(0, WIDTH//SPACING)]
        self.rows = [[tile for tile in self.tiles if tile.row == row]
                     for row in range(0, self.HEIGHT//self.SPACING)]
        self.total_disks = 0
        self.total_black_disks = 0
        self.total_white_disks = 0
        self.message = "Let the game begin! Your turn."
        self.end_message = ""
        self.game_over = False

    def add_disk(self, tile, color):
        """Add a disk to a tile of the board"""
        tile.add_disk(color)
        self.total_disks += 1

    def swap(self, tiles):
        """Change color of disk on each tile in input"""
        for tile in tiles:
            tile.tile_swap()

    def display(self):
        """Display the board"""
        background(34, 139, 34)

        # Draw the disks that exist
        for tile in self.tiles:
            if tile.disk:
                tile.disk.display()

        # Draw the board lines
        strokeWeight(3)
        for x in range(self.SPACING, self.WIDTH + 1, self.SPACING):
            line(x, 0, x, self.HEIGHT)

        for y in range(self.SPACING, self.HEIGHT, self.SPACING):
            line(0, y, self.WIDTH, y)

        # Update the board
        self.update()

    def update(self):
        """Perform necessary updates"""
        # Display current message
        self.display_message(self.message)

        # Check if game is over
        if self.game_over:
            self.end_game()

    def display_message(self, message):
        """Print an input string as message on the board"""
        X = self.WIDTH + 5
        Y = self.HEIGHT/6
        WIDTH = 195
        HEIGHT = self.HEIGHT + 50

        fill(0)
        textSize(35)
        textAlign(CENTER)
        text(message, X, Y, WIDTH, HEIGHT)

    def end_game(self):
        """Print end of game message"""
        textSize(self.HEIGHT/12)
        textAlign(CENTER)
        fill(0)
        text(self.end_message, 0, 25, self.WIDTH, self.HEIGHT)
        fill(174, 67, 178)
        text(self.end_message, 2, 25, self.WIDTH, self.HEIGHT)

    def count_disks(self):
        """End of game disk count and winner message declaration"""
        BLACK = 0
        WHITE = 255
        for tile in self.tiles:
            if tile.disk:
                if tile.disk.color == BLACK:
                    self.total_black_disks += 1
                elif tile.disk.color == WHITE:
                    self.total_white_disks += 1
        if self.total_black_disks > self.total_white_disks:
            message = "You win!"
        elif self.total_black_disks == self.total_white_disks:
            message = "Tie game!"
        else:
            message = "You lose."

        # Set end of game message based on outcome of game
        self.end_message = ("Game over. " + message + "\nYou've got " +
                            str(self.total_black_disks) + " tiles\n")

    def print_board(self):
        "Prints a formatted version of the board tiles."
        for row in self.rows:
            print("".join(str(row)))

