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
i = 0

# game start
print('\nWELCOME TO THE HANGMAN GAME (((o(*ﾟ▽ﾟ*)o)))')

# visual: place to input word (how many word)
count_word = len(hangman)
x = 0
print(f"The word contain {count_word} letters")
while x < count_word:
    print('_', end=' ')
    x += 1

while True:
    # criterial for game active -> human hasn't made 7 incorrect guesses
    if i < 7:
        # not win (still word not have been guess)
        if hangman_word:
            
            # input guess
            human_guess = input('\n\nInput your guess here: ').lower()
            
            # already guess -> rule out
            if human_guess in human_incorrect or human_guess in human_correct:
                print(f'You have already guess {human_guess}')
            
            # acceptable guess -> correct or incorrect
            else:
                # incorrect -> hangman
                if human_guess not in hangman_word:
                    human_incorrect += human_guess
                    print(f'\nIncorrect! There is no {human_guess} in the word!')
                    # hangman
                    print(hangmanresults[i])
                    i += 1
                else:
                    # correct -> how many letter in the word
                    count_guess = hangman_word.count(human_guess)
                    print(f'\nCorrect! There is {count_guess} {human_guess} in the word!')
                    
                    # visual board
                    index_guess = hangman.index(human_guess)
                    # first letter (eg. z_ _ _ _ _) -> check index by code below
                    # print(index_guess)
                    if index_guess == 0:
                        z = 1
                        print(human_guess, end=' ')
                        while z < count_word:
                            print('_', end=' ')
                            z += 1
                    elif 0 < index_guess < count_word:
                        wordbefore = int()
                        wordafter = index_guess + 1
                        while wordbefore < index_guess:
                            print('_', end=' ')
                            wordbefore += 1
                        print(human_guess, end=' ')
                        while index_guess < wordafter + 1 <= count_word:
                            print('_', end=' ')
                            wordafter += 1
                    elif index_guess == count_word:
                        zz = 1
                        while zz < count_word:
                            print('_', end=' ')
                            zz += 1
                    
                    # remove the word from hangman list -> put it into the human correct
                    hangman_word.remove(human_guess)
                    human_correct.append(human_guess)
                    # print word user have guess
                    print('\nYour guess: ', end='')
                    for w in human_correct:
                        print(w.upper(), end=' ')
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
