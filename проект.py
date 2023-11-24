import sqlite3
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS sites (
            id INTEGER PRIMARY KEY,
            url TEXT,
            content TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_site(self, url, content):
        query = "INSERT INTO sites (url, content) VALUES (?, ?)"
        self.conn.execute(query, (url, content))
        self.conn.commit()

    def clear_database(self):
        query = "DELETE FROM sites"
        self.conn.execute(query)
        self.conn.commit()

    def search_sites(self, query):
        query = f"SELECT url FROM sites WHERE content LIKE '%{query}%'"
        result = self.conn.execute(query).fetchall()
        return [row[0] for row in result]

class WebParser:
    def parse_site(self, url):

class UserInterface:
    def __init__(self, database, parser):
        self.database = database
        self.parser = parser
        self.root = tk.Tk()
        self.root.title("Пошук на сайтах")


    def run(self):
        self.root.mainloop()


def run():
    db = Database("sites.db")
    parser = WebParser()
    ui = UserInterface(db, parser)
    ui.run()

if __name__ == "__main__":
    run()

