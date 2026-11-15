import sqlite3


def read(book: int, chapter: int, verse: int):
    con = sqlite3.connect('Bible_data/kjv.sqlite')

    with con as db:
        cursor = db.cursor()
        cursor.execute('SELECT ')

    con.close()