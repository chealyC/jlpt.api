import sqlite3
from questions_data import questions


def create_table():
    connection = sqlite3.connect("jlpt.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY,
            question TEXT NOT NULL,
            choice_a TEXT NOT NULL,
            choice_b TEXT NOT NULL,
            choice_c TEXT NOT NULL,
            choice_d TEXT NOT NULL,
            answer TEXT NOT NULL,
            level TEXT NOT NULL,
            category TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_questions():
    create_table()

    connection = sqlite3.connect("jlpt.db")
    cursor = connection.cursor()

    for q in questions:
        cursor.execute("""
            INSERT INTO questions
            (question, choice_a, choice_b, choice_c, choice_d,
             answer, level, category)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, q)

    connection.commit()
    connection.close()


def get_questions(level):
    add_questions()

    connection = sqlite3.connect("jlpt.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM questions
        WHERE level = ?
    """, (level.upper(),))

    results = cursor.fetchall()

    connection.close()

    return [
        {
            "id": row[0],
            "question": row[1],
            "choice_a": row[2],
            "choice_b": row[3],
            "choice_c": row[4],
            "choice_d": row[5],
            "answer": row[6],
            "level": row[7],
            "category": row[8],
        }
        for row in results
    ]

