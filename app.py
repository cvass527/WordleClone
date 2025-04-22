from flask import Flask, render_template, request, session, redirect, url_for, jsonify

import ReadDictionary

import db

from User import User


app = Flask(__name__)
app.secret_key = 'your_secret_key'

currentDB = db.InitializeUserDatabase()



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
    user = session.get('user')
    return render_template('game.html',user = user)

@app.route('/won')
def won():
    user = session.get('user')
    db.IncrementWins(user['name'])

    updatedUser = User.from_dict(user)
    updatedUser.IncrementWins()
    session['user'] =  updatedUser.to_dict()

    return render_template('won.html', word = session['word'])

@app.route('/lost')
def lost():
    user = session.get('user')
    db.IncrementLoss(user['name'])

    updatedUser = User.from_dict(user)
    updatedUser.IncrementLosses()
    session['user'] =  updatedUser.to_dict()

    return render_template('lost.html', word = session['word'])


@app.route("/submit_name", methods = ["POST"])
def AddNameAndStartGame():
    name = request.form["name"]

    currentUser = db.TryAddUser(name)

    session['user'] = currentUser.to_dict()

    return redirect(url_for('game'))



app.run()

