import sqlite3


def create_bd():
    """Function to create sqlite database to keep results of all users"""
    try:
        open("data.sqlite")
    except FileNotFoundError:
        print(1231)
        con = sqlite3.connect("data.sqlite")
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                score INT NOT NULL
            )
        """)
        con.commit()


def insert_score_in_database(name: str, score: int):
    """Function to add a new recording to database"""
    con = sqlite3.connect("data.sqlite")
    cur = con.cursor()
    cur.execute(f"""
                INSERT INTO data (name, score)
                VALUES ('{name}', {score})
            """)
    con.commit()


def get_max_score_by_name(name: str = None):
    """Function to get max score of user by name"""
    con = sqlite3.connect("data.sqlite")
    cur = con.cursor()
    if name is None:
        data = cur.execute("""SELECT score FROM data""").fetchall()
        return max(data)
    else:
        data = cur.execute(f"""SELECT score FROM data WHERE name = '{name}'""").fetchall()
        return max(data if data else (0, 0))
