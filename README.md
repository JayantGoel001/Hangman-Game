# Hangman Game
<p>
Hangman is an old school favorite, a word game where the goal is simply to find the missing word or words.

You will be presented with a number of blank spaces representing the missing letters you need to find.

Use the keyboard to guess a letter (I recommend starting with vowels).

If your chosen letter exists in the answer, then all places in the answer where that letter appear will be revealed.

After you've revealed several letters, you may be able to guess what the answer is and fill in the remaining letters.

Be warned, every time you guess a letter wrong you loose a life and the hangman begins to appear, piece by piece.

Solve the puzzle before the hangman dies.
</p><a><img src="https://github.com/CormacKrum/Hangman-Game/blob/master/Hangman_game.jpg" alt="Hangman Game"/></a>

The following example game illustrates a player trying to guess the word hangman using a strategy based solely on letter frequency. As the player continues, a part of the stick figure on the noose is added. Once a full body is drawn, the game is over, and the player lost.

0	
<a>
<img src="https://github.com/CormacKrum/Hangman-Game/blob/master/Hangman-0.png" alt="Hangman Game"/>
</a>
<a>
Word:	hangman<br>
Guess:	E<br>
Misses:<br>
</a>	
1	
<img src="https://github.com/CormacKrum/Hangman-Game/blob/master/Hangman-1.png" alt="Hangman Game"/>
Word:	_ _ _ _ _ _ _
Guess:	T
Misses:	e
2	
<img src="https://github.com/CormacKrum/Hangman-Game/blob/master/Hangman-2.png" alt="Hangman Game"/>
Word:	_ _ _ _ _ _ _
Guess:	A
Misses:	e, t
3	
<img src="https://github.com/CormacKrum/Hangman-Game/blob/master/Hangman-2.png" alt="Hangman Game"/>
Word:	_ A _ _ _ A _
Guess:	O
Misses:	e, t
4	
<img src="https://github.com/CormacKrum/Hangman-Game/blob/master/Hangman-3.png" alt="Hangman Game"/>
Word:	_ A _ _ _ A _
Guess:	I
Misses:	e, o, t
5	
<img src="https://github.com/CormacKrum/Hangman-Game/blob/master/Hangman-4.png" alt="Hangman Game"/>
Word:	_ A _ _ _ A _
Guess:	S
Misses:	e, i, o, t
6	
<img src="https://github.com/CormacKrum/Hangman-Game/blob/master/Hangman-5.png" alt="Hangman Game"/>
Word:	_ A _ _ _ A _
Guess:	N
Misses:	e, i, o, s, t
7	
<img src="https://github.com/CormacKrum/Hangman-Game/blob/master/Hangman-5.png" alt="Hangman Game"/>
Word:	_ A N _ _ A N
Guess:	R
Misses:	e ,i, o, s, t
8	
<img src="https://github.com/CormacKrum/Hangman-Game/blob/master/Hangman-6.png" alt="Hangman Game"/>
Word:	_ A N _ _ A N
Guess:	
Misses:	e, i, o, r, s, t


**The guessing player has lost this game as the diagram had been completed before all the letters were guessed.**
