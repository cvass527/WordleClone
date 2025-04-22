import sqlite3

from User import User


def InitializeUserDatabase():
    conn = sqlite3.connect("Users.db")
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    Username TEXT UNIQUE NOT NULL,
    Wins INTEGER DEFAULT 0,
    Losses INTEGER DEFAULT 0)
    ''')

    conn.commit()
    conn.close()



def TryAddUser(name):
    conn = sqlite3.connect("Users.db")
    cursor = conn.cursor()
    cursor.execute('''
    Select Username, Wins, Losses 
    From Users 
    WHERE Username = ?''',(name,))

    response = cursor.fetchone()

    if response is None:
        #Username doesn't exist
        cursor.execute('INSERT INTO Users (Username, Wins, Losses) VALUES (?, 0, 0)', (name,))
        conn.commit()
        conn.close()
        return User(name, 0, 0)
    else:
        #return wins losses
        return User(name, response[1], response[2])


def IncrementLoss(name):
    conn = sqlite3.connect("Users.db")
    cursor = conn.cursor()
    cursor.execute('''
    Select Losses 
    From Users 
    WHERE Username = ?''',(name,))

    response = cursor.fetchone()

    newLossAmount = response[0] + 1

    cursor.execute('''
    Update Users
    SET Losses = ?
    WHERE Username = ?''',(newLossAmount,name,))

    conn.commit()
    conn.close()

def IncrementWins(name):
    conn = sqlite3.connect("Users.db")
    cursor = conn.cursor()
    cursor.execute('''
    Select Wins 
    From Users 
    WHERE Username = ?''',(name,))

    response = cursor.fetchone()

    newWinAmount = response[0] + 1

    cursor.execute('''
    Update Users
    SET Wins = ?
    WHERE Username = ?''',(newWinAmount,name,))

    conn.commit()
    conn.close()