Jonah Golden

1)  Did you attempt to make your computer player very smart -- i.e., do
    something more clever than just pick a random legal move?

I attempted to make the computer pick a move that swaps the most of the
opposing tiles as possible.

2)  If so, were you able to accomplish this?

I was able to accomplish this, however if there is a tie between moves
(multiple moves would swap the same number of tiles), the computer player
simply chooses the first move.

    Is your computer player as smart as you would like?

I would like it to be smarter. There are definite improvements that would make
it choose better moves and be less predictable.

3)  How did you determine which piece to play next?

The computer picks a move that swaps the most of the opposing tiles as
possible, choosing the "first" move in the event of a tie.

    Tell us about your “pick next move” algorithm.

The "pick next move" algorithm loops through every tile on the board. If the
tile is a valid move AND it would swap MORE tiles than any previously looked at
move, it assigns the tile and the number of opposing tiles the move would swap
to a dictionary, replacing the previous "move" that was in the dictionary.

4)  How often did your computer program beat you, or your friends, or whoever
tested it out for you?

The computer program beat most people that didn't have experience playing
Othello. However, after playing a few games, most people could beat the
computer program about half the time, and the more people played, the more
often they could beat the computer.

5)  How would you improve it in the future?

An easy improvement would be to make the computer randomly choose one of the 
"best moves" in the event of multiple moves swapping the same number of tiles.
This would make the computer less predictable. Another improvement would be to
weight the value of certain tiles. For example, it seems that getting a corner
tile early in the game is very valuable, so the computer could choose this move
over another move that might swap more tiles. It could also look at the
player's next available moves, and choose a move that limits the player's
potential moves on the next turn. Additionally, the computer could look down
the line at potential outcomes of the game, and choose a move that has the most
potential win scenarios. 
