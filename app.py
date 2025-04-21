from flask import Flask, render_template, request, session, redirect, url_for
from Wordle import Wordle
import sqlite3


app = Flask(__name__)
app.secret_key = 'your_secret_key' 


@app.route('/game')
def PlayWordle():

    wordle_instance = Wordle.from_dict(session['current_game'])
    currentBoard = wordle_instance.RetrieveBoard()
    print("Current Board:", currentBoard)  # Debugging
    return render_template('game.html', board = currentBoard)

@app.route('/submit_guess', methods = ['POST'])
def SubmitGuess():
    guess = request.form['guess']

    wordleSession = Wordle.from_dict(session['current_game'])

    guessResult = wordleSession.WordGuess(guess)


    wordleSession.UpdateBoard(guessResult)

    currentBoard = wordleSession.RetrieveBoard()

    '''

    print('Wordle State: ' + wordleSession.state)
    print('Wordle Round: ' + str(wordleSession.round))
    print('Wordle Word: ' + wordleSession.word)


    for row in currentBoard:
        print('Wordle Board Row: ' + ''.join(row))
    '''



    if(guess == wordleSession.word.upper()):

        print('GAME WON')
        #append the round, then the game state, then
        #how the guess result
        wordleSession.state = '!'
        session['current_game'] = wordleSession.to_dict()
        session.modified = True
        return(render_template('won.html', word = wordleSession.word))

    elif(wordleSession.round > 5):

        print('GAME LOST')
        wordleSession.state = '~'
        session['current_game'] = wordleSession.to_dict()
        session.modified = True
        return(render_template('lost.html', word = wordleSession.word))

    else:
        print('Next Round')
        wordleSession.state = '$'
        session['current_game'] = wordleSession.to_dict()
        session.modified = True
        return(render_template('game.html', board = currentBoard, result = guessResult))







@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit_name", methods = ["POST"])
def AddNameAndStartGame():

    name = request.form["name"]

    print("Name: " + name)

    wordle_instance = Wordle()


    session['current_game'] = wordle_instance.to_dict()
    session.modified = True

    return redirect(url_for('PlayWordle'))

@app.route('/lost')
def lost():
    correct_word = "APPLE" 
    return render_template('lost.html', word=correct_word)


@app.route('/won')
def won():
    correct_word = "APPLE"  
    return render_template('won.html', word=correct_word)

