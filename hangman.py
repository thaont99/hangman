import random

# hangman words to guess
hangman_list = [
    " abruptly ", " absurd ", " abyss ", " affix ", " askew ", " avenue ", " awkward ", " axiom ", " azure ", " bagpipes ", " bandwagon ", " banjo ",
    " bayou ", " beekeeper ", " bikini ", " blitz ", " blizzard ", " boggle ", " bookworm ", " boxcar ", " boxful ", " buckaroo ", " buffalo ",
    " buffoon ", " buxom ", " buzzard ", " buzzing ", " buzzwords ", " caliph ", " cobweb ", " cockiness ", " croquet ", " crypt ", " curacao ",
    " cycle ", " daiquiri ", " dirndl ", " disavow ", " dizzying ", " duplex ", " dwarves ", " embezzle ", " equip ", " espionage ", " euouae ",
    " exodus ", " faking ", " fishhook ", " fixable ", " fjord ", " flapjack ", " flopping ", " fluffiness ", " flyby ", " foxglove ", " frazzled ",
    " frizzled ", " fuchsia ", " funny ", " gabby ", " galaxy ", " galvanize ", " gazebo ", " giaour ", " gizmo ", " glowworm ", " glyph ",
    " gnarly ", " gnostic ", " gossip ", " grogginess ", " haiku ", " haphazard ", " hyphen ", " iatrogenic ", " icebox ", " injury ", " ivory ",
    " ivy ", " jackpot ", " jaundice ", " jawbreaker ", " jaywalk ", " jazziest ", " jazzy ", " jelly ", " jigsaw ", " jinx ", " jiujitsu ",
    " jockey ", " jogging ", " joking ", " jovial ", " joyful ", " juicy ", " jukebox ", " jumbo ", " kayak ", " kazoo ", " keyhole ", " khaki ",
    " kilobyte ", " kiosk ", " kitsch ", " kiwifruit ", " klutz ", " knapsack ", " larynx ", " lengths ", " lucky ", " luxury ", " lymph ",
    " marquis ", " matrix ", " megahertz ", " microwave ", " mnemonic ", " mystify ", " naphtha ", " nightclub ", " nowadays ", " numbskull ",
    " nymph ", " onyx ", " ovary ", " oxidize ", " oxygen ", " pajama ", " peekaboo ", " phlegm ", " pixel ", " pizazz ", " pneumonia ", " polka ",
    " pshaw ", " psyche ", " puppy ", " puzzling ", " quartz ", " queue ", " quips ", " quixotic ", " quiz ", " quizzes ", " quorum ", " razzmatazz ",
    " rhubarb ", " rhythm ", " rickshaw ", " schnapps ", " scratch ", " shiv ", " snazzy ", " sphinx ", " spritz ", " squawk ", " staff ",
    " strength ", " strengths ", " stretch ", " stronghold ", " stymied ", " subway ", " swivel ", " syndrome ", " thriftless ", " thumbscrew ",
    " topaz ", " transcript ", " transgress ", " transplant ", " triphthong ", " twelfth ", " twelfths ", " unknown ", " unworthy ", " unzip ",
    " uptown ", " vaporize ", " vixen ", " vodka ", " voodoo ", " vortex ", " voyeurism ", " walkway ", " waltz ", " wave ", " wavy ", " waxy ",
    " wellspring ", " wheezy ", " whiskey ", " whizzing ", " whomever ", " wimpy ", " witchcraft ", " wizard ", " woozy ", " wristwatch ", " wyvern ",
    " xylophone ", " yachtsman ", " yippee ", " yoked ", " youthful ", " yummy ", " zephyr ", " zigzag ", " zigzagging ", " zilch ", " zipper ",
    " zodiac ", " zombie ",
]

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

# the secret word
hangman = random.choice(hangman_list).strip()
hangman_word = []
# input the hangman word in a list -> for each correct guess, remove the word from hangman list and put it into the human correct
for i in hangman:
    hangman_word.append(i)

# the user guess
human_incorrect = []
human_correct = []
visual_board = []
human_incorrect_count = 0

# game start
print('\nWELCOME TO THE HANGMAN GAME (((o(*ﾟ▽ﾟ*)o)))')

# visual: place to input word (how many word) --> eg. two => print _ _ _ => append _ _ _ into visual_board
count_word = len(hangman)
visual_empty = '_ '
print(f"The word contain {count_word} letters")
x = 0
while x < count_word:
    visual_board.append(visual_empty)
    print(visual_empty, end='')
    x += 1

while True:
    # criterial for game active -> human hasn't made 7 incorrect guesses
    if human_incorrect_count < 7:
        # not win (still word not have been guess)
        if hangman_word:
            
            # input guess
            human_guess = input('\n\nInput your guess here: ').lower()
            
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
                    
                    # visual board
                    index_guess = hangman.index(human_guess)
                    del visual_board[index_guess]
                    visual_board.insert(index_guess, human_guess)
                    for v in visual_board:
                        print(v.upper(), end=' ')
                    
                    # remove the word from hangman list -> put it into the human correct
                    hangman_word.remove(human_guess)
                    human_correct.append(human_guess)
                    
        else:
            print('\n\n----------------------------------------\n'
                  'Congratulate! YOU WIN O(≧∇≦o)')
            break
    
    # Game not active -> human made 7 mistakes
    else:
        print('\n\n----------------------------------------\n'
              'GAME OVER DOLL\nYOU LOSE.')
        break
        
# show results
print(f'\n> The secret word is: {hangman.upper()}')
