 ===========
  P H I B S
 ===========
 
Find a friend to play this game with and choose a board size. 

Players make moves by adding phibs to the board. A phib can:
1. Add a 1 to the player's team.
2. Increase one of the player's numbers by 1.
3. Cancel out an opponent's 1.
4. Die pathetically against an opponent's number greater than 1.

Players move simultaneously by choosing a square, and either promising
not to change their minds, or writing down their choice.

Top left is (0, 0).

Between moves, the board runs one step at a time until it comes to a halt.
Each step, every number is pushed a certain distance by up to 4 neighbors.

 0 0 0
 2 x 0    Here, the x will be pushed East by 2, because of the 2 to it's West.
 0 0 0
 
 0 1 0
 2 x 2    Here, the x will be pushed South by 1, because pushes summate.
 0 0 0
 
 0 0 0 0    0 0 0 0
 0 1 1 0 -> 1 0 0 1    All pushes occur simultaneously.
 0 0 0 0    0 0 0 0
 
If 2 numbers land on the same square:
Each team sums their total phibs that landed on that square.
If one team has the highest sum for that square, they survive, and the rest die.
Otherwise, all phibs die.

Phibs pushed off the board die.
First player to create a 10 wins. Or something.

Type 'quit' at any time to quit.
