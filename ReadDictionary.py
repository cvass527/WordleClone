import sqlite3
import random

def ReadDictionaryFile():
    myFile = open('words.txt')

    #Luckily it's all on one line
    line = myFile.read()

    myFile.close()

    words = line.split(',')

    validWords = []

    for word in words:
        word = word.strip()
        if len(word) == 5:
            validWords.append(word.upper())

    return validWords

def PopulateWordleWordDB(Dictionary):

    conn = sqlite3.connect("wordle.db")
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Words(Word TEXT)')

    conn.commit()

    for word in Dictionary:
        cursor.execute('INSERT INTO Words (Word) VALUES (?)', (word,))

    conn.commit()
    conn.close()

def ChooseRandomWord():
    conn = sqlite3.connect("wordle.db")
    cursor = conn.cursor()
    cursor.execute('Select Count(*) FROM Words')

    wordCount = cursor.fetchone()


    randomIndex = random.randint(0,wordCount[0]-1)
    cursor.execute('SELECT Word FROM Words LIMIT 1 OFFSET (?)',(randomIndex,))

    randomWord = cursor.fetchone()
    conn.commit()
    conn.close()

    return randomWord[0]

newDictionary = ReadDictionaryFile()
PopulateWordleWordDB(newDictionary)





