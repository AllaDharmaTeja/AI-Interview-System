import sqlite3

def save_result(question, answer, score):

    conn = sqlite3.connect("results.db")

    cursor = conn.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS results (question TEXT, answer TEXT, score REAL)"
    )

    cursor.execute(
        "INSERT INTO results VALUES (?,?,?)",
        (question, answer, score)
    )

    conn.commit()
    conn.close()