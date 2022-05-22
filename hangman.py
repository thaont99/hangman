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
visual_board = []
human_incorrect_count = 0

# hangman words to guess
hangman_dictionary = {'answer': 'school', 'arithmetic': 'school', 'assignment': 'school', 'atlas': 'school', 'backpack': 'school',
                      'ballpoint pen': 'school', 'binder': 'school', 'blackboard': 'school', 'book': 'school', 'bookcase': 'school',
                      'bookmark': 'school', 'calculator': 'school', 'calendar': 'school', 'chalk': 'school', 'classroom': 'school',
                      'compass': 'school', 'computer': 'school', 'crayons': 'school', 'desk': 'school', 'dictionary': 'school', 'dividers': 'school',
                      'easel': 'school', 'encyclopedia': 'school', 'English': 'school', 'eraser': 'school', 'exam': 'school', 'examination': 'school',
                      'experiment': 'school', 'folder': 'school', 'geography': 'school', 'globe': 'school', 'glossary': 'school', 'glue': 'school',
                      'grades': 'school', 'gym': 'school', 'highlighter': 'school', 'history': 'school', 'homework': 'school', 'ink': 'school',
                      'intelligent': 'school', 'keyboard': 'school', 'language': 'school', 'learn': 'school', 'lesson': 'school', 'library': 'school',
                      'lunch ': 'school', 'markers': 'school', 'math': 'school', 'mathematics': 'school', 'memorize': 'school', 'paper': 'school',
                      'paste': 'school', 'pen': 'school', 'pencil': 'school', 'printer': 'school', 'project': 'school', 'protractor': 'school',
                      'pupil': 'school', 'question': 'school', 'quiz': 'school', 'reading': 'school', 'recess': 'school', 'rubber': 'school',
                      'ruler': 'school', 'science': 'school', 'scissors': 'school', 'sharpener': 'school', 'smart': 'school', 'stapler': 'school',
                      'student': 'school', 'tape': 'school', 'teacher': 'school', 'test': 'school', 'thesaurus': 'school', 'think': 'school',
                      'vocabulary': 'school', 'watercolors': 'school', 'whiteboard': 'school', 'yardstick': 'school', 'map': 'school',
                      'writing': 'school', 'adoption': 'family', 'ancestor': 'family', 'aunt': 'family', 'bachelor': 'family', 'bride': 'family',
                      'bridegroom': 'family', 'brother': 'family', 'brotherhood': 'family', 'brotherly': 'family', 'child': 'family',
                      'childhood': 'family', 'children': 'family', 'clan': 'family', 'connection': 'family', 'cousin': 'family', 'dad': 'family',
                      'daddy': 'family', 'daughter': 'family', 'descendant': 'family', 'devoted': 'family', 'divorce': 'family', 'eligible': 'family',
                      'engaged': 'family', 'engagement': 'family', 'estranged': 'family', 'accountant': 'Office, Business, Workplace',
                      'accounting': 'Office, Business, Workplace', 'accounts': 'Office, Business, Workplace',
                      'accruals': 'Office, Business, Workplace', 'ads': 'Office, Business, Workplace', 'advertise': 'Office, Business, Workplace',
                      'affordable': 'Office, Business, Workplace', 'agenda': 'Office, Business, Workplace',
                      'agreement': 'Office, Business, Workplace', 'arbitration': 'Office, Business, Workplace',
                      'benefits': 'Office, Business, Workplace', 'board': 'Office, Business, Workplace', 'bond': 'Office, Business, Workplace',
                      'bonus': 'Office, Business, Workplace', 'bookkeeping': 'Office, Business, Workplace', 'borrow': 'Office, Business, Workplace',
                      'boss': 'Office, Business, Workplace', 'briefcase': 'Office, Business, Workplace', 'budget': 'Office, Business, Workplace',
                      'business': 'Office, Business, Workplace', 'buy': 'Office, Business, Workplace', 'buyer': 'Office, Business, Workplace',
                      'calculate': 'Office, Business, Workplace', 'capital': 'Office, Business, Workplace',
                      'capitalist': 'Office, Business, Workplace', 'career': 'Office, Business, Workplace', 'cargo': 'Office, Business, Workplace',
                      'chairman': 'Office, Business, Workplace', 'chairwoman': 'Office, Business, Workplace', 'charge': 'Office, Business, Workplace',
                      'clause': 'Office, Business, Workplace', 'client': 'Office, Business, Workplace', 'close': 'Office, Business, Workplace',
                      'collateral': 'Office, Business, Workplace', 'commerce': 'Office, Business, Workplace',
                      'commercial': 'Office, Business, Workplace', 'commission': 'Office, Business, Workplace',
                      'commodity': 'Office, Business, Workplace', 'company': 'Office, Business, Workplace',
                      'competition': 'Office, Business, Workplace', 'compromise': 'Office, Business, Workplace',
                      'consumer': 'Office, Business, Workplace', 'contract': 'Office, Business, Workplace',
                      'copyright': 'Office, Business, Workplace', 'corporate': 'Office, Business, Workplace',
                      'corporation': 'Office, Business, Workplace', 'cost': 'Office, Business, Workplace', 'coupon': 'Office, Business, Workplace',
                      'credit': 'Office, Business, Workplace', 'cubicle': 'Office, Business, Workplace', 'currency': 'Office, Business, Workplace',
                      'customer': 'Office, Business, Workplace', 'database': 'Office, Business, Workplace', 'deadline': 'Office, Business, Workplace',
                      'deal': 'Office, Business, Workplace', 'debit': 'Office, Business, Workplace', 'deflation': 'Office, Business, Workplace',
                      'demand': 'Office, Business, Workplace', 'department': 'Office, Business, Workplace', 'director': 'Office, Business, Workplace',
                      'discount': 'Office, Business, Workplace', 'dismiss': 'Office, Business, Workplace',
                      'distribution': 'Office, Business, Workplace', 'diversify': 'Office, Business, Workplace',
                      'dividend': 'Office, Business, Workplace', 'download': 'Office, Business, Workplace', 'duties': 'Office, Business, Workplace',
                      'duty': 'Office, Business, Workplace', 'economical': 'Office, Business, Workplace', 'economics': 'Office, Business, Workplace',
                      'efficiency': 'Office, Business, Workplace', 'employ': 'Office, Business, Workplace', 'employee': 'Office, Business, Workplace',
                      'employer': 'Office, Business, Workplace', 'employment': 'Office, Business, Workplace',
                      'entrepreneur': 'Office, Business, Workplace', 'equipment': 'Office, Business, Workplace',
                      'estimate': 'Office, Business, Workplace', 'executive': 'Office, Business, Workplace',
                      'expenses': 'Office, Business, Workplace', 'export': 'Office, Business, Workplace', 'facility': 'Office, Business, Workplace',
                      'factory': 'Office, Business, Workplace', 'fax': 'Office, Business, Workplace', 'figures': 'Office, Business, Workplace',
                      'finance': 'Office, Business, Workplace', 'financial': 'Office, Business, Workplace', 'fire': 'Office, Business, Workplace',
                      'foreman': 'Office, Business, Workplace', 'framework': 'Office, Business, Workplace', 'freight': 'Office, Business, Workplace',
                      'fund': 'Office, Business, Workplace', 'goods': 'Office, Business, Workplace', 'graph': 'Office, Business, Workplace',
                      'gross': 'Office, Business, Workplace', 'growth': 'Office, Business, Workplace', 'guidebook': 'Office, Business, Workplace',
                      'headhunter': 'Office, Business, Workplace', 'headquarters': 'Office, Business, Workplace',
                      'high': 'Office, Business, Workplace', 'hire': 'Office, Business, Workplace', 'hours': 'Office, Business, Workplace',
                      'import': 'Office, Business, Workplace', 'incentive': 'Office, Business, Workplace', 'income': 'Office, Business, Workplace',
                      'inflation': 'Office, Business, Workplace', 'insurance': 'Office, Business, Workplace', 'intern': 'Office, Business, Workplace',
                      'interview': 'Office, Business, Workplace', 'inventory': 'Office, Business, Workplace', 'invest': 'Office, Business, Workplace',
                      'investment': 'Office, Business, Workplace', 'invoice': 'Office, Business, Workplace', 'job': 'Office, Business, Workplace',
                      'labor': 'Office, Business, Workplace', 'laborer': 'Office, Business, Workplace', 'laptop': 'Office, Business, Workplace',
                      'lead': 'Office, Business, Workplace', 'lease': 'Office, Business, Workplace', 'leave': 'Office, Business, Workplace',
                      'letterhead': 'Office, Business, Workplace', 'liability': 'Office, Business, Workplace', 'loan': 'Office, Business, Workplace',
                      'loss': 'Office, Business, Workplace', 'low': 'Office, Business, Workplace', 'lucrative': 'Office, Business, Workplace',
                      'mailbox': 'Office, Business, Workplace', 'mainframe': 'Office, Business, Workplace', 'manage': 'Office, Business, Workplace',
                      'management': 'Office, Business, Workplace', 'manager': 'Office, Business, Workplace', 'market': 'Office, Business, Workplace',
                      'marketing': 'Office, Business, Workplace', 'meeting': 'Office, Business, Workplace', 'memo': 'Office, Business, Workplace',
                      'merchandise': 'Office, Business, Workplace', 'merchant': 'Office, Business, Workplace', 'money': 'Office, Business, Workplace',
                      'monopoly': 'Office, Business, Workplace', 'motherboard': 'Office, Business, Workplace',
                      'negotiate': 'Office, Business, Workplace', 'negotiation': 'Office, Business, Workplace', 'net': 'Office, Business, Workplace',
                      'network': 'Office, Business, Workplace', 'niche': 'Office, Business, Workplace', 'notebook': 'Office, Business, Workplace',
                      'notice': 'Office, Business, Workplace', 'occupation': 'Office, Business, Workplace', 'offer': 'Office, Business, Workplace',
                      'office': 'Office, Business, Workplace', 'offline': 'Office, Business, Workplace', 'online': 'Office, Business, Workplace',
                      'open': 'Office, Business, Workplace', 'opportunity': 'Office, Business, Workplace', 'order': 'Office, Business, Workplace',
                      'organization': 'Office, Business, Workplace', 'outgoing': 'Office, Business, Workplace',
                      'overdraft': 'Office, Business, Workplace', 'overhead': 'Office, Business, Workplace', 'owner': 'Office, Business, Workplace',
                      'paperweight': 'Office, Business, Workplace', 'partner': 'Office, Business, Workplace',
                      'password': 'Office, Business, Workplace', 'pay': 'Office, Business, Workplace', 'payment': 'Office, Business, Workplace',
                      'perk': 'Office, Business, Workplace', 'personnel': 'Office, Business, Workplace', 'plan': 'Office, Business, Workplace',
                      'policy': 'Office, Business, Workplace', 'portfolio': 'Office, Business, Workplace', 'position': 'Office, Business, Workplace',
                      'presentation': 'Office, Business, Workplace', 'president': 'Office, Business, Workplace',
                      'price': 'Office, Business, Workplace', 'principal': 'Office, Business, Workplace', 'product': 'Office, Business, Workplace',
                      'production': 'Office, Business, Workplace', 'profit': 'Office, Business, Workplace',
                      'profitable': 'Office, Business, Workplace', 'promotion': 'Office, Business, Workplace',
                      'proposal': 'Office, Business, Workplace', 'prospects': 'Office, Business, Workplace', 'proxy': 'Office, Business, Workplace',
                      'purchasing': 'Office, Business, Workplace', 'quarter': 'Office, Business, Workplace', 'quit': 'Office, Business, Workplace',
                      'rank': 'Office, Business, Workplace', 'receipt': 'Office, Business, Workplace', 'recruit': 'Office, Business, Workplace',
                      'recruiter': 'Office, Business, Workplace', 'refund': 'Office, Business, Workplace', 'resign': 'Office, Business, Workplace',
                      'retail': 'Office, Business, Workplace', 'retailer': 'Office, Business, Workplace', 'retire': 'Office, Business, Workplace',
                      'resume': 'Office, Business, Workplace', 'risk': 'Office, Business, Workplace', 'salary': 'Office, Business, Workplace',
                      'sale': 'Office, Business, Workplace', 'salesman': 'Office, Business, Workplace', 'saleswoman': 'Office, Business, Workplace',
                      'secretary': 'Office, Business, Workplace', 'sell': 'Office, Business, Workplace', 'seller': 'Office, Business, Workplace',
                      'service': 'Office, Business, Workplace', 'shareholder': 'Office, Business, Workplace', 'ship': 'Office, Business, Workplace',
                      'shipment': 'Office, Business, Workplace', 'shipping': 'Office, Business, Workplace', 'shop': 'Office, Business, Workplace',
                      'sign': 'Office, Business, Workplace', 'signature': 'Office, Business, Workplace', 'spreadsheet': 'Office, Business, Workplace',
                      'staff': 'Office, Business, Workplace', 'statement': 'Office, Business, Workplace', 'stock': 'Office, Business, Workplace',
                      'stockholder': 'Office, Business, Workplace', 'strike': 'Office, Business, Workplace', 'success': 'Office, Business, Workplace',
                      'superintendent': 'Office, Business, Workplace', 'supervisor': 'Office, Business, Workplace',
                      'supply': 'Office, Business, Workplace', 'target': 'Office, Business, Workplace', 'tariff': 'Office, Business, Workplace',
                      'tax': 'Office, Business, Workplace', 'temp': 'Office, Business, Workplace', 'terms': 'Office, Business, Workplace',
                      'trade': 'Office, Business, Workplace', 'trainee': 'Office, Business, Workplace', 'transaction': 'Office, Business, Workplace',
                      'treasurer': 'Office, Business, Workplace', 'treasury': 'Office, Business, Workplace', 'trend': 'Office, Business, Workplace',
                      'typeface': 'Office, Business, Workplace', 'typewriter': 'Office, Business, Workplace',
                      'unemployment': 'Office, Business, Workplace', 'union': 'Office, Business, Workplace', 'upgrade': 'Office, Business, Workplace',
                      'upload': 'Office, Business, Workplace', 'username': 'Office, Business, Workplace', 'vacancy': 'Office, Business, Workplace',
                      'venture': 'Office, Business, Workplace', 'volume': 'Office, Business, Workplace', 'warranty': 'Office, Business, Workplace',
                      'wastebasket': 'Office, Business, Workplace', 'waybill': 'Office, Business, Workplace',
                      'wholesale': 'Office, Business, Workplace', 'wholesaler': 'Office, Business, Workplace',
                      'withdraw': 'Office, Business, Workplace', 'work': 'Office, Business, Workplace', 'worker': 'Office, Business, Workplace',
                      'workroom': 'Office, Business, Workplace', 'workspace': 'Office, Business, Workplace', 'yield': 'Office, Business, Workplace',
                      'ant': 'animals',	'bird': 'animals',	'cat': 'animals',	'chicken': 'animals',	'cow': 'animals',	'dog': 'animals',
                      'elephant': 'animals',	'fish': 'animals',	'fox': 'animals',	'horse': 'animals',	'kangaroo': 'animals',	'lion': 'animals',
                      'monkey': 'animals',	'penguin': 'animals',	'pig': 'animals',	'rabbit': 'animals',	'sheep': 'animals',
                      'tiger': 'animals',	'whale': 'animals',	'wolf': 'animals'
                      }
hangman_list = list(hangman_dictionary.keys())

# the secret word
hangman = random.choice(hangman_list)

# input the hangman word in a list -> for each correct guess, remove the word from word to guess
hangman_word = []
for i in hangman:
    hangman_word.append(i)

word_to_guess = set(hangman_word)

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
