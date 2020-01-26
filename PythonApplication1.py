import random
import os
from tkinter import *
from tkinter import ttk
HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
========''','''

  +---+
  |   |
  O   |
      |
      |
      |
========''','''

  +---+
  |   |
  O   |
  |   |
      |
      |
========''','''

  +---+
  |   |
  O   |
 /|   |
      |
      |
========''','''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
========''','''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========''','''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========''']

words_easy = 'ant bomb bat bear bait camel cat clam cobra colon'.split()
words_normal = 'extend extra moderator enhance gradient slope coherent collaborate collonial'.split()
words_hard = 'extravagant permutation disposable mongolian polycrystalline refridgerator luminusity'.split()
#words list

def dataStored(name, difficulty):
    f = open("Player info.txt", "a+")
    f.write(name + '  ' + difficulty +'\n')
    f.close()

def add_label():
    label_1 = Label(my_window, text ='Hello World')
    label_1.pack()


def getRandomWord(wordList):
    #This function returns a random string from the passed list of string.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print('H A N G M A N')
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Miss letters:', end = '')
    for letter in missedLetters:
        print(letter, end = '')
    print()
   
    blanks ='_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks= blanks[:i] + secretWord[i] + blanks[i+1:]
        
    for letter in blanks:
        print(letter, end = '')
    print()

def getSecretWord(difficult):
    if difficult == 'easy':
        secretWord = getRandomWord(words_easy)
    elif difficult == 'normal':
        secretWord = getRandomWord(words_normal)
    elif difficult == 'hard':
        secretWord = getRandomWord(words_hard)
    return secretWord

def getGuess(alreadyGuessed):
    #Return letter the player keyed in. This function makes sure the user to key in a single letter.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please key in a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter an alphabet letter.')
        else:
            return guess

def playAgain():
    #This function returns True if the player wants to play again, otherwise return False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def start(name):
    button_1 = ttk.Button(my_window_1, text = "Easy", command = lambda: main(name, 'easy')).grid(row = 3, column = 0)
    button_2 = ttk.Button(my_window_1, text = "Normal", command = lambda: main(name, 'normal')).grid(row = 3, column = 1)
    button_3 = ttk.Button(my_window_1, text = "Hard", command = lambda: main(name, 'hard')).grid(row = 3, column = 2)
    

def readData():
    f = open("Player info.txt", "r")
    print(f.read())
    f.close()

def tutorial():
    print('This is a word game. You have 5 chances for guessing the letters of the word.')

#Main funtion
def main(name, difficult):
    missedLetters =''
    correctLetters =''  
    secretWord = getSecretWord(difficult)
    gameIsDone = False
    while True:
        os.system('cls')
        displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
        #Let the player type in letters
        guess = getGuess(missedLetters + correctLetters)

        if guess in secretWord:
            correctLetters = correctLetters + guess
        
            #check if the player has won
            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                os.system('cls')
                displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
                print('Yes! The secret word is"'+secretWord+'"!You won!')
                gameIsDone = True
        else:
            missedLetters= missedLetters + guess

            #Check if player has lost
            if len(missedLetters) == len(HANGMANPICS) -1:
                os.system('cls')
                displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
                print('You have run out of guesses! The correct word is "' + secretWord + '"')
                gameIsDone = True
        
        #Ask to play again
        if gameIsDone:
            dataStored(name, difficult)
            if playAgain():
                missedLetters =''
                correctLetters =''
                gameIsDone = False
                secretWord = getSecretWord(difficult)
            else:
                os.system('cls')
                break


while True:
    
    my_window_1 = Tk()
    #my_window_1.geometry("500x200")
    my_window_1.title('Main menu')
    
    label = ttk.Label(my_window_1, text ="Enter your name")
    label.grid(row = 0, column = 0, columnspan =3)
    #label.pack()
    entry = ttk.Entry(my_window_1, width = 30)
    entry.grid(row = 1, column = 0, columnspan =3)
    #entry.pack()

    

    button_1 = ttk.Button(my_window_1, text = "Start", command = lambda : start(entry.get())).grid(row = 2, column =0) 
    button_2 = ttk.Button(my_window_1, text = "Information", command = readData).grid(row = 2, column =1) 
    button_3 = ttk.Button(my_window_1, text = "Tutorial", command = tutorial).grid(row = 2, column =2) 
    #button_1.pack()
    #button_2.pack()
    #button_3.pack()
    my_window_1.mainloop()
   
    



