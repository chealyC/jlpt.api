import sqlite3
from kanji_data import kanji

def create_table():
    connection = sqlite3.connect("jlpt.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS kanji (
        id INTEGER PRIMARY KEY,
        character TEXT NOT NULL UNIQUE,
        meaning TEXT NOT NULL,
        onyomi TEXT NOT NULL,
        kunyomi TEXT NOT NULL,
        level TEXT NOT NULL
        ) 
    """)

    connection.commit()
    connection.close()

def add_kanji():
    create_table()

    connection = sqlite3.connect("jlpt.db")
    cursor = connection.cursor()

    for ji in kanji:
        cursor.execute("""
            INSERT OR IGNORE INTO kanji
            (character, meaning, onyomi,
            kunyomi, level)
            VALUES (?, ?, ?, ?, ?)
        """, ji)

    connection.commit()
    connection.close()

def get_kanji(level):
    add_kanji()

    connection = sqlite3.connect("jlpt.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM kanji
        WHERE level = ?
    """, (level,))

    results = cursor.fetchall()

    connection.close()

    return [
        {
            "id": row[0],
            "character": row[1],
            "meaning": row[2],
            "onyomi": row[3],
            "kunyomi": row[4],
            "level": row[5],
        }
        for row in results
    ]


