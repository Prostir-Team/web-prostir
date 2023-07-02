from utils import *
from sqlite3 import connect as sqlite_connect
from sqlite3 import Connection, Cursor


class News:
    def __init__(self):
        self.db = sqlite_connect("server.sqlite", check_same_thread=False)
        self.sql = self.db.cursor()

        self.sql.execute("CREATE TABLE IF NOT EXISTS main_news(uuid INT, title TEXT, img TEXT, date TEXT)")
        self.db.commit()

    def get_news(self):
        self.sql.execute("SELECT * FROM main_news")
        
        return self.sql.fetchall()
    
    def add_new(self, title, img_path):
        uuid = generate_uuid()
        current_date = get_date()

        self.sql.execute("INSERT INTO main_news VALUES (?, ?, ?, ?)", (uuid, title, img_path, current_date))
        self.db.commit()