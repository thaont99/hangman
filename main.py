import random
import pandas as pd

hangman_results = [''''
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
already_guess = []
human_correct = []
human_incorrect_count = 0
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

# hangman words to guess

df = pd.read_excel('hangman.xlsx')
row = 0
hangman_dictionary = {}

x = len(df)
for i in range(0, x):
    word = df.loc[row, 'word']
    definition = df.loc[row, 'definition']
    row += 1
    hangman_dictionary[word[1:]] = definition  # [1:] to remove unicode char \xa0


hangman_list = list(hangman_dictionary.keys())

# the secret word
hangman = str(random.choice(hangman_list).lower().rstrip())

# input the hangman word in a list -> for each correct guess, remove the word from word to guess
hangman_word = []
for i in hangman:
    hangman_word.append(i)

letter_to_guess = []
for x in hangman_word:
    if x in alphabet_list:
        letter_to_guess.append(x)
word_to_guess = set(letter_to_guess)

# game start -> print hint (eg. This word belongs to which topic)
print(f'\nWELCOME TO THE HANGMAN GAME (((o(*ﾟ▽ﾟ*)o)))\nCAN YOU FIND THE WORD BEFORE THE HANGMAN HANGS '
      f'YOU?!\n----------------------------------------------------'
      f'\nSelect the letters that complete the word: "{hangman_dictionary[hangman].title()}" ')

# visual: place to input word (how many word) --> eg. two => print _ _ _ => append _ _ _ into visual_board. If space
# -> visual space, if '-' -> visual cross

count_word = len(hangman)

visual_board = []
visual_word = '_ '
visual_space = '/ '
visual_cross = '-'
for x in hangman:
    if x == ' ':
        visual_board.append(visual_space)
        print(visual_space, end='')
    elif x == '-':
        visual_board.append(visual_cross)
        print(visual_cross, end='')
    else:
        visual_board.append(visual_word)
        print(visual_word, end='')

while True:
    # criterial for game active -> human hasn't made 7 incorrect guesses
    if human_incorrect_count < 7:
        # not win (still word not have been guess)
        if word_to_guess:
            # input guess
            human_guess = input('\nInput your guess here: ').lower()

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
            if human_guess in already_guess:
                print(f'You have already guess {human_guess.upper()}')
                # print word user have guess
                print('\nYour guess: ', end='')
                for w in already_guess:
                    print(w.upper(), end=' ')

            # acceptable guess -> correct or incorrect
            else:
                # incorrect -> hangman, put the guess into the already_guess
                if human_guess not in hangman_word:
                    print(f'\nIncorrect! There is no {human_guess} in the word!')
                    already_guess.append(human_guess)

                    # hangman
                    print(hangman_results[human_incorrect_count])
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

                    # remove the word from the word_to_guess, put the guess into the human correct & already_guess
                    word_to_guess.remove(human_guess)
                    human_correct.append(human_guess)
                    already_guess.append(human_guess)

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




