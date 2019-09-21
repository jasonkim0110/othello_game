## Othello
A version of the board game [Othello](https://en.wikipedia.org/wiki/Reversi) with a simple computer AI.

### Usage
Run the othello_game.pyde sketch in Processing in Python Mode. Click the board to make a move.

### Computer AI
At the moment, the computer player picks the next legal move that swaps the most opposing tiles possible. In the event of a tie (i.e. multiple moves would swap the same most number of tiles), the "first" (row, column) move is chosen.

This "pick next move" algorithm is implemented in the make_move method in the computer class. It essentially loops through every tile on the board, checking for each whether it is a valid move. If a valid move would swap more tiles than than the previous best move, the best move is replaced with the new best move.

There are several improvements I would like to explore for the computer AI:

- An easy improvement would be to make the computer randomly choose one of the "best moves" in the event of multiple moves swapping the same number of tiles. This would make the computer less predictable.
- Weight the value of certain tiles. For example, it seems that getting a corner tile early in the game is very valuable, so the computer could choose this move over another move that might swap more tiles.
- Weight moves that limits the other player's potential moves on the next turn.
- Look down the line at potential outcomes of the game, and choose a move that has the most potential win scenarios. 
