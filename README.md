# Python_Dice_Game --- INSTRUCTOR FEEDBACK PROJECT  -
 
## General Requirements

- The game should have two players: a human player and a computer player. Both should have the same functionality.
- Both players will start with a counter of 10.
- Each player will have a particular die during the entire game.
- Both players will roll their corresponding die (once per round).
- The values of the dice will be compared to determine who wins the round. The player with the highest value wins the round.
- If the two values are equal, then there is a tie and there is no winner for that round. The counters are not modified.
- The counter of the player who wins a round will be decremented by 1.
- The counter of the player who loses a round will be incremented by 1.
- The counter will determine who wins the game. The player whose counter reaches the value 0 first wins the game.
- The game should show a descriptive message:
  - When the game starts.
  - When a new round starts.
  - When the game ends. This message should mention who won the game. 
  - Show the value of each die after the players roll the dice.
  - Mention the winner of the round or if there was a tie.
  - Show both counters when a round ends.

Classes: 

1 - Die

  Attributes:
  - value: random integer between 1 and 6 (inclusive). Private
  
  Methods:
  - Roll: assigns the random number to the value attribute.

2 - Player

  Attributes:
 - A Die instance.
 - A Boolean value (True/False) to indicate if the player is a human or the computer.
 - A counter. The initial value should be 10.
  
  
  Methods:
  - Increment the value of the counter by 1.
  - Decrement the value of the counter by 1.
  - Roll the die, for this I used Randint()
  

3 -  DiceGame

Attributes:
 - A human player instance.
 - A computer player instance.
For this I used aggregation

Methods:
 - Welcome message
 - Roll each dice
 - Playing logic of rounds
 - Update counters
 - Display messages of General Requierements
 - Show Winners and loosers and the counter reaching to zero.
