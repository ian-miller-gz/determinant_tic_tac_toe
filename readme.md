# Determinant Tic-Tac-Toe
##### Ian Miller
##### Spring, 2018

Demonstrate the game Determinant Tic-Tac-Toe is unfair and that one player is guaranteed to win with perfect play.

Determinant Tic-Tac-Toe(DT) was a game designed to be a math challenge. In the game, two players will take turns marking out fields in a 3x3 matrix, much in the style of tic-tac-toe. The catch, however, is that neither player is aiming for three-in-a-row of 'x's or 'o's. Rather, each player will mark their fields with '1's or '0's respectively. The player writing down '1's aims for the matrix to have a determinant of 1, after all fields have been filled. This player wins if she succeeds and loses otherwise.

One way to prove the game is unfair is by showing there is a strategy that always wins for one players. 

There are four significant turns in Determinant Tic-Tac-Toe with player one places five 1's and player two placing four 0's. The last 1 placed is fixed. For any complete fixed strategy, there are 945 possible games that can be played. 

![equation](https://latex.codecogs.com/svg.image?\large&space;{\color{CadetBlue}\prod^4_{i=0}2i&plus;1&space;=&space;945})

Call any set of games that analyze a strategy a strategy-set. The existence of any strategy-set whose members are all winning for one player is sufficient to demonstrate that there exists a strategy that always wins for one player and,hence, proves the game is unfair.

This script generates one such set.
