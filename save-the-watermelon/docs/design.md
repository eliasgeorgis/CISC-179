PROBLEM DESCRIPTION
the program picks a random word and the the user has 6 slices which are guess amounts to pick letters in order to guess the word. If the letter you pick isnt in the word you lose a slice if it is the amount stays the same. You win once you reveal all the letters and have an option to play again

The intended player is someone who likes trivia style games or guessing games and would find this fun

The player is trying to guess the word that is hidden by choosing letters they think the word has

GAME RULES
The game begins by asking the user for letter in put and gives instructions on how the game works 

The player types a letter in the terminal in order to make a guess and the game gives feedback

after a correct guess, the letter is revealed in the actual word and the user keeps players

after an incorrect guess, the user gets feedback that it was wrong and loses a slice

The player wins after all the letters are revealed

The players looses if the amount of slices or chances is equal to zero

PROGRAM DATA
I make a variable for the secret word in the beginning of the game 

I have a list that contains all the guessed letters

I have a nested loop that loops through all the letters guessed and the word to see if it matches

I have a variable called slices

PROGRAM ORGANIZATION
I need a select word function that chooses a random word from a list

I need a display word function that shows the underscores for the amount of letters and the revealed letters

I need a function to validate that the guess is valid and not a random number or multiple letters

I need a play game that initializes all variables and gives print statements for the users to know how the game is played

I need a main that calls play game and asks user if they want to play again and loops if so

PROGRAM FLOW
Start -> chose random word -> display hidden word -> get guess -> validate guess -> update game -> check win/loss -> repeat or end

