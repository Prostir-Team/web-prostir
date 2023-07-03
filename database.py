from utils import *
from sqlite3 import connect as sqlite_connect


conn = sqlite_connect("server.sqlite", check_same_thread=False)
sql = conn.cursor()

class News:
    @staticmethod
    def start():
        sql.execute("CREATE TABLE IF NOT EXISTS main_news(uuid TEXT, title TEXT, img TEXT, date TEXT)")
        conn.commit()
        
    @staticmethod
    def get_news():
        sql.execute("SELECT * FROM main_news")
        
        return sql.fetchall()
    
    @staticmethod
    def get_article(uuid: str):
        sql.execute(f"SELECT * FROM main_news WHERE uuid='{uuid}'")
        
        return sql.fetchone()

    @staticmethod
    def add_new(title: str, img_path: str):
        uuid = generate_uuid()
        current_date = get_date()

        sql.execute("INSERT INTO main_news VALUES (?, ?, ?, ?)", (uuid, title, img_path, current_date))
        conn.commit()

        Article.start(uuid)

class Article:
    @staticmethod
    def start(uuid: str):
        sql.execute(f"CREATE TABLE IF NOT EXISTS {article_uuid(uuid)}(type INT, info TEXT)")
        conn.commit()
    
    @staticmethod
    def is_exist(uuid: str) -> bool:
        sql.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{article_uuid(uuid)}'")
        
        return sql.fetchall() != []

    @staticmethod
    def add_update(uuid: str, type: int, text: str):
        if not Article.is_exist(uuid): return
        
        sql.execute(f"INSERT INTO {article_uuid(uuid)} VALUES (?, ?)", (type, text))
        conn.commit()
    
    @staticmethod
    def get_info(uuid: str):
        if not Article.is_exist(uuid): return

        sql.execute(f"SELECT * FROM {article_uuid(uuid)}")
        return convert_types(sql.fetchall())


