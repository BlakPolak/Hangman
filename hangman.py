import sys
import random
import time
from decimal import Decimal


capitals = ["ANDORRA","LA VELLA","AMSTERDAM","ANKARA","ASTANA","ATHENS","BAKU","BELGRADE","BERLIN","BERN","BRATISLAVA",
            "BRUSSELS","BUCHAREST","BUDAPEST","CHISINAU","COPENHAGEN","DUBLIN","HELSINKI","KYIV","LISBON","LJUBLJANA",
            "LONDON","LUXEMBOURG","MADRID","MINSK","MONACO","MOSCOW","NICOSIA","OSLO","PARIS","PODGORICA","PRAGUE",
            "PRISTINA","REYKJAVIK","RIGA","ROME","SAN MARINO","SARAJEVO","SKOPJE","SOFIA","STOCKHOLM","TALLINN",
            "TBILISI","VADUZ","VALLETTA","VATICAN","VIENNA","VILNIUS","WARSAW", "YEREVAN", "ZAGREB"]
print('Behold, puny human! I shall grind whole Europe, town by town. If you guess which capital I am going to destroy'
      ' in 10 tries, I shall leave it alone. For now! HA HA HA\nYou have only 10 chances so be focused!')


def main():
    """Here program starts, chooses random capital and does rest of needed stuff"""
    global capitals
    global capital
    global dash
    global lives
    global start
    global end
    global lettercount
    global not_in_word
    not_in_word = []
    capital = capitals.pop(random.randint(0,len(capitals)-1)) #Removes one element at the given position in the list capitals, and return it.
    #print (capital)- cheat
    dash = capital.replace(str(capital), ' _' *len(capital)) #Changes capital letters with dashes.
    print (dash)
    dash = dash.split()
    lives = 10
    lettercount = 0
    start = time.time() #starts counting time
    letterorword()


def you_won():
    """When you won, it shows you how long it takes you to save a city and how many letters you needded to guess.
    It gives you chance to save other capitals"""
    print("\nThis is it!")
    end = Decimal(time.time() - start)
    end = str(round(end, 1))
    global lettercount
    print("\nSaving " + capital + " took thou " + str(end) + " seconds and " + repr(lettercount) + " letters.")
    replay = input('Enter any number if you want to save another city, if not enter anything YOU COWARD!')
    if replay.isnumeric():
        main()
    else:
        print("Shame. I shall just destroy whole Europe at once. HA HA HA")
        sys.exit()


def chances():
    """Counting your lives"""
    global lives
    lives = lives - 1
    if lives < 1 :
        print('Thou failed! ' + capital + ' shall be erased from the Earth!')
        end = Decimal(time.time() - start) # checks how much time you needed from start. Changes to decimal.
        end = str(round(end, 1)) #round time to one decimal place
        print("\nThou have damned " + capital + " after just " + str(end) +" seconds and " + repr(lettercount) + " letters.")
        replay = input('Enter any number if you want to try saving another city, if not enter anything YOU COWARD! ')
        if replay.isnumeric():
            main()
        else:
            print("Shame. I shall just destroy whole Europe at once. HA HA HA")
            sys.exit()
    else:
        print('You have only ' + repr(lives) + ' chances left.')
        letterorword()


def word():
    """When you choose guessing with word this function checks if your answer is ok or not"""
    guessedword = input('What is your guess, mortal? ').upper()
    if guessedword == capital:
        you_won()
    else:
        global lives
        print ("Wrong!")
        lives -=1
        chances()


def letter():
    """When you choose guessing with letters this function checks if guess letter is in our capital or not"""
    global lettercount
    lettercount += 1
    guessedletter = input('What is your guess, mortal? ').upper()
    if len(guessedletter)!=1:
        print("Only one letter at the time!")
        letter()
    elif guessedletter in capital:
        changedletters = [i for i, x in enumerate(capital) if x == guessedletter] #Makes a list of indexes where appears guessed letter in capital word.
        for n in changedletters:
            dash[n] = guessedletter # Changes dashes with guessed letters.
        newdash = ' '.join(dash) # Only for better appearance (_ _ _ NOT _____)
        newdash2 = ''.join(dash)
        print ('\nYou got it!\n' + newdash)
        if newdash2 == capital:
          you_won()
        else:
            letterorword()
    else:
        print('\nWrong!')
        not_in_word.append(guessedletter) #Adds wrong letters to list not_in_word
        print ("\nLetters not in word:")
        print (not_in_word)
        chances()


def letterorword():
    """Chooses way to guess a capital. You can guess by letter or whole word"""
    letterORword= input("\nWould thou like to guess a letter or a whole word"
                        " (if thou fail guessing a word, thou shall lose two chances)?"
                        " Please enter L for letter or W for word: ").upper()
    if letterORword == 'L':
        letter()
    elif letterORword == 'W':
        word()
    else:
        letterorword()


main()