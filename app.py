from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from Wordle import Wordle
import ReadDictionary
import sqlite3


app = Flask(__name__)
app.secret_key = 'your_secret_key' 



@app.route('/word')
def GetWord():
    word = ReadDictionary.ChooseRandomWord()
    session['word'] = word
    return jsonify({'word': word})


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/won')
def won():
    return render_template('won.html', word = session['word'])

@app.route('/lost')
def lost():
    return render_template('lost.html', word = session['word'])


@app.route("/submit_name", methods = ["POST"])
def AddNameAndStartGame():
    name = request.form["name"]

    return redirect(url_for('game'))



app.run()

