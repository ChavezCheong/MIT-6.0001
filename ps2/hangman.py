# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
      if letter not in letters_guessed:
        return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents which letters in secret_word have been guessed so far.
    '''
    secret_word_list = ["_ " if letter not in letters_guessed else letter for letter in list(secret_word)]
    return "".join(secret_word_list)
        
def check_vowel(guess):
  '''
  guess: the letter/character guessed by the player.

  Checks whether letter is vowel or consonant.
  
  Returns true if vowel, false if not vowel.
  '''
  vowels = ["a","e","i","o","u"]
  if guess in vowels:
    return True
  else:
    return False

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not yet been guessed.
    '''
    return "".join([letter for letter in list(string.ascii_lowercase) if letter not in letters_guessed])

def check_warning(guess, secret_word, letters_guessed, warnings_remaining, guesses_remaining):
  '''
  guess: the letter/character guessed by the player.
  secret_word: string, the secret word to guess.
  letters_guessed: the list of letters guessed so far.
  warnings_remaining: the number of warnings left.
  guesses_remaining: the number of guesses left.

  Checks the inputs for warnings and returns a tuple of all the input states depending on what has been processed.  
  '''
  initial_warnings = warnings_remaining
  initial_guesses = guesses_remaining
  warning_check = True

  #Check for warnings.
  if warnings_remaining > 0:
    if len(guess) != 1:
      warnings_remaining -= 1
      print(f"Oops, please guess a single letter or a single character. You have {warnings_remaining} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
    elif not guess.isalpha():
      warnings_remaining -= 1
      print(f"Oops! That is not a valid letter. You have {warnings_remaining} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
    elif guess in letters_guessed:
      warnings_remaining -= 1
      print(f"Oops! You've already guessed that letter. You have {warnings_remaining} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
  elif warnings_remaining == 0:
    if len(guess) != 1:
      guesses_remaining -= 1
      print(f"Oops, please guess a single letter or a single character. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
    elif not guess.isalpha():
      guesses_remaining -= 1
      print(f"Oops! That is not a valid letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
    elif guess in letters_guessed:
      guesses_remaining -= 1
      print(f"Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
  
  #Check if warnings exist
  if initial_warnings == warnings_remaining and initial_guesses == guesses_remaining:
    warning_check = False
  
  #Return tuple of values
  return warnings_remaining, guesses_remaining, warning_check

def check_letter(guess, secret_word, letters_guessed, guesses_remaining):
    '''
    guess: the letter/character guessed by the player.
    secret_word: string, the secret word to guess.
    letters_guessed: the list of letters guessed so far.
    guesses_remaining: the number of guesses left.
    Checks the inputs and returns tuple of guesses remaining and letters guessed.
  '''
    letter = guess.lower()
  
    #Check whether letter is in word
    if letter in list(secret_word):
      letters_guessed.append(letter)
      print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
    else:
      letters_guessed.append(letter)
      print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
      if check_vowel(letter):
        guesses_remaining -= 1
      guesses_remaining -= 1

    return letters_guessed, guesses_remaining
    
def get_final_score(guesses_remaining, secret_word):
  '''
  guesses_remaining: number of remaining guesses
  secret_word: string, the secret word to guess.

  Calculates final score = guesses_remaining * number of unique letters in secret_word
  '''
  return guesses_remaining * len(set(secret_word))

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''

    # Set up the counts for the game
    guesses_remaining = 6
    warnings_remaining = 3

    #Introduction to the Game
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {warnings_remaining} warnings left.")
    letters_guessed = []

    #Game itself
    while not is_word_guessed(secret_word, letters_guessed) and guesses_remaining != 0:
      print(f"You have {guesses_remaining} guesses left")
      print(f"Available Letters: {get_available_letters(letters_guessed)}")

      #Guess letter
      guess = input("Please guess a letter:")

      #Check if input is valid and return values accordingly.
      warnings_remaining, guesses_remaining, warning_check = check_warning(guess, secret_word, letters_guessed, warnings_remaining, guesses_remaining)

      #Check if letter is correct, if no warnings
      if not warning_check:
        letters_guessed, guesses_remaining = check_letter(guess, secret_word, letters_guessed, guesses_remaining)

      #Print end-of-line
      print("------------")
    #Check win condition

    if guesses_remaining == 0:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}")
    else:
        print("Congratulatio, you won!")
        print(f"Your total score for this game: {get_final_score(guesses_remaining, secret_word)}")


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)
# -----------------------------------


def match_with_gaps(my_word, other_word, running_letters_guessed):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    running_letters_guessed: all the letters that have been guessed so far
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    counter = 0
    guessed_word = "".join(my_word.split())
    #Check if length 
    if len(guessed_word) != len(other_word):
      return False
    letters_guessed = set(list(guessed_word))
    guessed_word_list = list(guessed_word)
    other_word_list = list(other_word)

    for i in range(len(guessed_word)):
      if guessed_word_list[i] == other_word_list[i] or (guessed_word_list[i] == "_" and other_word_list[i] not in letters_guessed) and other_word_list[i] not in running_letters_guessed:
        counter += 1
    
    if counter == len(guessed_word):
      return True
    else:
      return False

  




def show_possible_matches(my_word, running_letters_guessed):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    full_wordlist = []
    for word in wordlist:
      if match_with_gaps(my_word, word, running_letters_guessed):
        full_wordlist.append(word)
    
    if len(full_wordlist) == 0:
      print("No matches found")
    else:
      print(" ".join(full_wordlist))




def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # Set up the counts for the game
    guesses_remaining = 6
    warnings_remaining = 3

    #Introduction to the Game
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {warnings_remaining} warnings left.")
    letters_guessed = []

    #Game itself
    while not is_word_guessed(secret_word, letters_guessed) and guesses_remaining != 0:
      print(f"You have {guesses_remaining} guesses left")
      print(f"Available Letters: {get_available_letters(letters_guessed)}")

      #Guess letter
      guess = input("Please guess a letter:")

      #Check if player is asking for hints.
      if guess == "*":
        show_possible_matches(get_guessed_word(secret_word, letters_guessed), letters_guessed)
      else:
        #Check if input is valid and return values accordingly.
        warnings_remaining, guesses_remaining, warning_check = check_warning(guess, secret_word, letters_guessed, warnings_remaining, guesses_remaining)

        #Check if letter is correct, if no warnings
        if not warning_check:
          letters_guessed, guesses_remaining = check_letter(guess, secret_word, letters_guessed, guesses_remaining)

      #Print end-of-line
      print("------------")
    #Check win condition

    if guesses_remaining == 0:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}")
    else:
        print("Congratulatio, you won!")
        print(f"Your total score for this game: {get_final_score(guesses_remaining, secret_word)}")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    
  secret_word = choose_word(wordlist)
  hangman_with_hints(secret_word)
