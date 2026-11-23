import sqlite3
from random import randint


def read(random = True, book = 0, chapter = 0, verse = 0):
    con = sqlite3.connect('data/kjv.sqlite')

    with con as db:
        cursor = db.cursor()

        if random and book == 0 and chapter == 0 and verse == 0:
            book = randint(1, 66)
            cursor.execute('SELECT MAX(chapter) FROM verses WHERE book = ?', (book,))
            chapter = randint(1, cursor.fetchone()[0])
            cursor.execute('SELECT MAX(verse) FROM verses WHERE book = ? AND chapter = ?', (book, chapter))
            verse = randint(1, cursor.fetchone()[0])
            cursor.execute('SELECT text FROM verses WHERE book = ? AND chapter = ? AND verse = ?', (book, chapter, verse))
            retdata = cursor.fetchone()[0]

        elif book != 0 and chapter != 0 and verse != 0:
            cursor.execute('SELECT text FROM verses WHERE book = ? AND chapter = ? AND verse = ?', (book, chapter, verse))
            retdata = cursor.fetchone()[0]

        else:
            retdata = ('false',)

    con.close()

    return str(retdata)