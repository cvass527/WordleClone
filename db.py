import sqlite3

def InitializeUserDatabase():
    conn = sqlite3.connect("Users.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
    Username TEXT UNIQUE NOT NULL
    Wins INTEGER DEFAULT 0,
    Loses INTEGER DEFAULT 0''')
    conn.commit
    conn.close


InitializeUserDatabase()