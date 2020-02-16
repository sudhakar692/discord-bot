# db.py
import psycopg2
from datetime import datetime
import settings as appconfig
class Database():
    def __init__(self):
        self.connection = None
        self.cursor=None
        pass

    def connect(self):
        if self.connection:
            return
        config = {
            'user': appconfig.DATABASE_USER,
            'password': appconfig.DATABASE_PASSWORD,
            'host': appconfig.DATABASE_HOST,
            'database': appconfig.DATABASE_NAME,
            'sslmode': 'allow'
        }
        self.connection = psycopg2.connect(**config)
        self.cursor = self.connection.cursor()
    def get_cursor(self):
        return self.cursor


    def save_search_query(self,user_id, keyword):
        """
            save search query into the database table with respective user id
        """
        cursor = self.cursor
        cursor.execute("Insert into Search_History (search_query,user_id,created_on) Values('{}', '{}', '{}')".format(
             keyword,user_id,datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        self.connection.commit()
        self.connection.close()


    def fetch_recent_search_query(self,user_id, keyword):
        """
            fetch results match with keyword for respective user id 
        """
        cursor = self.cursor
        cursor.execute(
            "Select * from Search_History where user_id = '{}' and search_query like '%{}%'".format(user_id, keyword))
        results = cursor.fetchall()
        self.connection.close()
        return results
