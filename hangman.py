import random 

words = ["cat", "dog", "turtle", "bee", "lion", "eagle", 
         "tiger", "bear", "camel", "rabbit", "donkey", "fox", 
         "elephant", "deer", "horse", "cow", "goat"]


choosen_word = random.choice(words)
valid_letters = "abcdefghijklmnopqrstuvwxyz"
total_rights = 5
guess = ""

# game pictures 

HANGMAN = [
    """
      --------
      |    |
      |
      |
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |    |
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|\
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|\
      |   /
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|\
      |   / \
      |
    """
]

print("Welcome to Hangman Game")

while total_rights > 0:
    real_word = ""
    for letter in choosen_word:
        if letter in guess:
            real_word += letter
        else:
            real_word += "_"
        
    if real_word == choosen_word:
        print(real_word)
        print("Congrulations. You Win!")
        break

    print(HANGMAN[5-total_rights])
    print("Guess animal name: ", real_word)
    print(f"New guess right: {total_rights}")

    input_guess = input("Guess a letter: ").lower()

    if input_guess in valid_letters:
        guess += input_guess
        if input_guess not in choosen_word:
            total_rights -= 1
    else:
        print("Please enter a valid letter....")
else:
    print("Sorry, you lose the game. Correct word is: ", choosen_word)