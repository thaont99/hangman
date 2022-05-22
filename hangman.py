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
already_guess = []
human_correct = []
human_incorrect_count = 0
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# hangman words to guess
hangman_dictionary = {
    'analytics': 'The scientific process of transforming data into insight for making better decisions. ',
    'big data': 'A set of data that cannot be managed, processed, or analyzed with commonly available software in a reasonable amount of time. Big '
                'data are characterized by great volume (a large amount of data), high velocity (fast collection and processing), or wide variety ('
                'could include nontraditional data such as video, audio, and text). ',
    'categorical data': 'Labels or names used to identify an attribute of each element. Categorical data use either the nominal or ordinal scale of '
                        'measurement and may be nonnumeric or numeric. ',
    'categorical variable': 'A variable with categorical data. ',
    'census': 'A survey to collect data on the entire population. ',
    'data set': 'All the data collected in a particular study. ',
    'descriptive statistics': 'Tabular, graphical, and numerical summaries of data. ',
    'elements': 'The entities on which data are collected. ',
    'interval scale': 'The scale of measurement for a variable if the data demonstrate the properties of ordinal data and the interval between '
                      'values is expressed in terms of a fixed unit of measure. Interval data are always numeric. ',
    'nominal scale': 'The scale of measurement for a variable when the data are labels or names used to identify an attribute of an element. '
                     'Nominal data may be nonnumeric or numeric. ',
    'ordinal scale': 'The scale of measurement for a variable if the data exhibit the properties of nominal data and the order or rank of the data '
                     'is meaningful. Ordinal data may be nonnumeric or numeric. ',
    'population': 'The set of all elements of interest in a particular study. ',
    'quantitative data': 'Numeric values that indicate how much or how many of something. Quantitative data are obtained using either the interval '
                         'or ratio scale of measurement. ',
    'quantitative variable': 'A variable with quantitative data. ',
    'ratio scale': 'The scale of measurement for a variable if the data demonstrate all the properties of interval data and the ratio of two values '
                   'is meaningful. Ratio data are always numeric. ',
    'sample': 'A subset of the population. ',
    'sample survey': 'A survey to collect data on a sample. ',
    'statistical inference': 'The process of using data obtained from a sample to make estimates or test hypotheses about the characteristics of a '
                             'population. ',
    'statistics': 'The art and science of collecting, analyzing, presenting, and interpreting data. ',
    'time series data': 'Data collected over several time periods. ',
    'variable': 'A characteristic of interest for the elements. ',
    'cross-sectional data': 'Data are collected at the same or approximately the same point in time. ',
    'time-series data': 'Data are collected over several time periods. ',
    'pooled data': 'A mixture of time-series data and cross-sectional data. ',
    'issue': ' A topic or subject to investigate ',
    'question': ' Designed to discover information ',
    'problem': ' An obstacle or complication that needs to be worked out ',
    'analytical skills': ' Qualities and characteristics associated with using facts to solve problems ',
    'analytical thinking': ' The process of identifying and defining a problem, then solving it by using data in an organized, step-by-step manner ',
    'attribute': ' A characteristic or quality of data used to label a column in a table ',
    'business task': ' The question or problem data analysis resolves for a business ',
    'context': ' The condition in which something exists or happens ',
    'data': ' A collection of facts ',
    'data analysis': 'The collection, transformation, and organization of data in order to draw conclusions, make predictions, and drive informed '
                     'decision-making ',
    'data analyst': 'Someone who collects, transforms, and organizes data in order to draw conclusions, make predictions, and drive informed '
                    'decision-making ',
    'data analytics': ' The science of data ',
    'data design': ' How information is organized ',
    'data-driven decision-making': ' Using facts to guide business strategy ',
    'data ecosystem': ' The various elements that interact with one another in order to produce, manage, store, organize, analyze, and share data ',
    'data science': ' A field of study that uses raw data to create new ways of modeling and understanding the unknown ',
    'data strategy': ' The management of the people, processes, and tools used in data analysis ',
    'data visualization': ' The graphical representation of data ',
    'database': ' A collection of data stored in a computer system ',
    'dataset': ' A collection of data that can be manipulated or analyzed as one unit ',
    'fairness': ' A quality of data analysis that does not create or reinforce bias ',
    'formula': ' A set of instructions used to perform a calculation using the data in a spreadsheet ',
    'function': ' A preset command that automatically performs a process or task using the data in a spreadsheet ',
    'gap analysis': 'A method for examining and evaluating the current state of a process in order to identify opportunities for improvement in the '
                    'future ',
    'observation': ' The attributes that describe a piece of data contained in a row of a table ',
    'query': ' A request for data or information from a database ',
    'query language': ' A computer programming language used to communicate with a database ',
    'root cause': ' The reason why a problem occurs ',
    'stakeholders': ' People who invest time and resources into a project and are interested in its outcome ',
    'technical mindset': ' The ability to break things down into smaller steps or pieces and work with them in an orderly and logical way ',
    'visualization': ' Refer to data visualization ',
    
}
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
      f'\nHint: {hangman_dictionary[hangman]}')

# visual: place to input word (how many word) --> eg. two => print _ _ _ => append _ _ _ into visual_board. If space -> visual space,
# if '-' -> visual cross

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
