import random

hangmanresults = [''''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# the user guess
human_incorrect = []
human_correct = []
visual_board = []
human_incorrect_count = 0

# hangman words to guess
hangman_dictionary = {'dogs': 'animals', 'cats': 'animals', 'keys': 'objects'}
hangman_list = list(hangman_dictionary.keys())

# the secret word
hangman = random.choice(hangman_list)

# input the hangman word in a list -> for each correct guess, remove the word from hangman list and put it into the human correct
hangman_word = []
for i in hangman:
    hangman_word.append(i)
    
word_to_guess = hangman_word[:]
# game start -> print hint (eg. This word belongs to which topic)
print(f'\nWELCOME TO THE HANGMAN GAME (((o(*ﾟ▽ﾟ*)o)))\nCAN YOU FIND THE WORD BEFORE THE HANGMAN HANGS '
      f'YOU?!\n----------------------------------------------------'
      f'\nThis words belongs to the topic: {hangman_dictionary[hangman].upper()}')

# visual: place to input word (how many word) --> eg. two => print _ _ _ => append _ _ _ into visual_board
count_word = len(hangman)
visual_empty = '_ '
x = 0
print(f"The word contain {count_word} letters")
while x < count_word:
    visual_board.append(visual_empty)
    print(visual_empty, end='')
    x += 1

while True:
    # criterial for game active -> human hasn't made 7 incorrect guesses
    if human_incorrect_count < 7:
        # not win (still word not have been guess)
        if word_to_guess:
            # input guess
            human_guess = input('\n\nInput your guess here: ').lower()
    
            # input > 1 letter or number -> not allowed (try - execept, use continue to input again)
            try:
                int(human_guess)
            except ValueError:
                if len(human_guess) > 1:
                    print('Only input one characters!')
                    continue
                else:
                    pass
            else:
                print('Only input characters! Number not allowed')
                continue
                
            # already guess -> rule out
            if human_guess in human_incorrect or human_guess in human_correct:
                print(f'You have already guess {human_guess}')
                # print word user have guess
                print('\nYour guess: ', end='')
                for w in human_correct:
                    print(w.upper(), end=' ')
            
            # acceptable guess -> correct or incorrect
            else:
                # incorrect -> hangman
                if human_guess not in hangman_word:
                    human_incorrect += human_guess
                    print(f'\nIncorrect! There is no {human_guess} in the word!')
                    
                    # hangman
                    print(hangmanresults[human_incorrect_count])
                    human_incorrect_count += 1
                else:
                    # correct -> how many letter in the word
                    count_guess = hangman_word.count(human_guess)
                    print(f'\nCorrect! There is {count_guess} {human_guess} in the word!')
                    
                    # visual board -> start with a board contain all correct word.
                    # Using an if loop: If the guess is correct -> pass. If wrong, print '_' instead of the correct word
                    visual_board = hangman_word[:]
                    for check in visual_board:
                        if check != human_guess:
                            if check not in human_correct:
                                index_guess = visual_board.index(check)
                                del visual_board[index_guess]
                                visual_board.insert(index_guess, '_')
                    for v in visual_board:
                        print(v.upper(), end=' ')
                    
                    # put the guess into the human correct, remove the word from the word_to_guess
                    human_correct.append(human_guess)
                    word_to_guess.remove(human_guess)
                    
        
        else:
            print('\n\n----------------------------------------\n'
                  'CONGRATULATIONS! YOU WIN O(≧∇≦o)')
            break
    
    # Game not active -> human made 7 mistakes
    else:
        print('\n\n----------------------------------------\n'
              'GAME OVER\nYOU LOSE.')
        break

# show results
print(f'\n> The secret word is: {hangman.upper()}')
