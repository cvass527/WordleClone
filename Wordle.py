import ReadDictionary

class Wordle:

    def __init__(self):
        # '*' is the start state
        # '$' is game ongoing, not correctly guessed
        # '!' is game won, word correctly guessed
        # '~' is game lost


        self.state = '$'
        self.round = 0
        self.word = ''
        self.board = []

        self.StartWordleRound()



        # Serialize the instance to a dictionary
    def to_dict(self):
        toReturn = {}
        toReturn['state'] =self.state
        toReturn['round'] = self.round
        toReturn['word'] = self.word
        toReturn['board'] = self.board

        #print('ToDict board: ' + self.board)
        return toReturn



     # Add this method to deserialize data from the session
    @classmethod
    def from_dict(cls, data):
        wordle = cls()  # Create a new instance


        wordle.state = data['state']
        wordle.round = data['round']
        wordle.word = data['word']
        #print('From Dict Board' + data['board'])
        wordle.board = data['board']
        return wordle

    def InitBoard(self):
        self.board.clear()
        for row in range(0,5):
            self.board.append(['-','-','-','-','-'])

        #print('init board: ' + self.board)
        
    def UpdateBoard(self, userGuess):
        self.board[self.round-1].clear()
        for char in userGuess:
            self.board[self.round-1].append(char)
        #increment the round
        self.round = self.round + 1


    def RetrieveBoard(self):
        return self.board

    def StartWordleRound(self):
        self.word = ReadDictionary.ChooseRandomWord()
        self.state = '$'
        self.round = 1
        self.InitBoard()

    
    def WordGuess(self, userGuess):
        #if the letter is incorrect completely
        #'-' is returned
        #if the letter is not correct, but found
        #in the word the lowercase of the letter is returned
        #if the letter is correct, the uppercase is returned
        
        toReturn = []

        #Check how good the guess was
        for index in range(0,5):

            letterGuess = userGuess[index].upper()

            #self.guessedLetters.add(letterGuess)

            if(self.word[index] == letterGuess):
                toReturn.append(letterGuess)
            elif (letterGuess in self.word):
                toReturn.append(letterGuess.lower())
            else:
                toReturn.append('-')



        #If it's a match, they won!
        theCheckedGuess = ''.join(toReturn) 

        #self.UpdateBoard(theCheckedGuess)
        #self.board = theCheckedGuess



        return theCheckedGuess
        

'''

def PrintCurrentBoard(currentBoard):
    toPrint = ''

    for char in currentBoard:
        toPrint = toPrint + char + ' '

    print(toPrint)

def PromptToPlayAgain():

    userInput = input('Would you like to play again?(y/n): ')

    if(userInput == 'y'):
        return True
    else:
        return False

'''

'''Start an example game and check gameflow logic'''

'''
newGame = Wordle()

stillPlaying = True


print('Lets play some Wordle!')

newGame.StartWordleRound()

while stillPlaying:


    PrintCurrentBoard(newGame.board)

    print('Round ' + str(newGame.round) + '!')
    userGuess = input('Please enter your 5 letter guess: ')


    cleanedUserGuess = (userGuess.strip()).upper()
    currentState = newGame.WordGuess(cleanedUserGuess)

    currentBoard = newGame.board


    
    if(len(newGame.guessedLetters)> 0):

        guessedList = []

        for letter in newGame.guessedLetters:

            guessedList.append(letter)

        print("Letters Guessed: " + ''.join(guessedList).upper())

    if '!' in currentState:

        print('Congratulations! You guessed the word')

        stillPlaying = PromptToPlayAgain()

        if(stillPlaying):
            newGame.StartWordleRound()
        else:
            print('Thanks for playing!')


        #need to update the sql with a win
        #need to let the form know it won

    elif '~' in currentState:

        print('Game Over! Here is the word: ' + newGame.word)

        stillPlaying = PromptToPlayAgain()

        if(stillPlaying):
            newGame.StartWordleRound()
        else:
            print('Thanks for playing!')

        #need to update the sql with a loss
        #need to let eh form know it's a loss

'''