import sqlite3

class MovieDatabase:

    def __init__(self, name, connect_on_startup=True):
        self.name = name
        self.db_connection = None
        self.cursor = None

        if connect_on_startup:
            self.connect()

    def connect(self):
        self.db_connection = sqlite3.connect(self.name)
        self.cursor = self.db_connection.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY, "
            "title text, director text, language text, release_year integer)"
        )
        self.db_connection.commit()
        print(type(self.db_connection))
        print(type(self.cursor))

    def close_connection(self):
        self.db_connection.close()

    def insert(self, title, director, language, release_year):
        self.cursor.execute("INSERT INTO movies VALUES (NULL,?,?,?,?)",
                            (title, director, language, release_year))

    def view(self):
        self.cursor.execute("SELECT * FROM movies")
        rows = self.cursor.fetchall()
        return rows

    def delete(self, movie_id):
        self.cursor.execute("DELETE FROM movies WHERE id=?",(movie_id,))

    def search(self, title, director, language, release_year):
        self.cursor.execute(
            "SELECT * FROM book WHERE title=? OR director=? "
            "OR language=? OR release_year=?",
            (title, director, language, release_year))
        return self.cursor.fetchall()