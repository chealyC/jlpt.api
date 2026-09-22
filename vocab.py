import sqlite3
from vocabulary_data import vocabulary

def create_table():
    connection = sqlite3.connect("jlpt.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vocabulary (
            id INTEGER PRIMARY KEY,
            word TEXT NOT NULL UNIQUE,
            reading TEXT NOT NULL,
            meaning TEXT NOT NULL,
            level TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_vocab():
    create_table()

    connection = sqlite3.connect("jlpt.db")
    cursor = connection.cursor()

    for word in vocabulary:
        cursor.execute("""
            INSERT OR IGNORE INTO vocabulary
            (word, reading, meaning, level)
            VALUES (?, ?, ?, ?)
        """, word)

    connection.commit()
    connection.close()

def get_vocab(level):
    add_vocab()

    connection = sqlite3.connect("jlpt.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM vocabulary
        WHERE level = ?
    """, (level,))

    results = cursor.fetchall()

    connection.close()

    return [
        {
            "id": row[0],
            "word": row[1],
            "reading": row[2],
            "meaning": row[3],
            "level": row[4],
        }
        for row in results
    ]


