import mysql.connector


class Database:
    def __init__(self):
        # Initialize the database if it doesn't already exist
        try:
            self.my_sql = mysql.connector.connect(host="localhost",
                                                  user="root",
                                                  password="yourpassword")
            cursor = self.my_sql.cursor()
            cursor.execute("CREATE DATABASE shortchanged")
        except:
            pass

        self.my_sql = mysql.connector.connect(host="localhost",
                                              user="root",
                                              password="yourpassword",
                                              database="shortchanged")
        try:
            # Add table short_changed to the database if it doesn't already exit
            cursor = self.my_sql.cursor()
            cursor.execute("CREATE TABLE short_changed (long_url VARCHAR(255), short_url VARCHAR(7))")

        except:
            pass

    # Add a row (long URL and short URL) to the database
    def add_data(self, longurl: str, shorturl: str):

        if not self.long_url_exists(longurl):
            cursor = self.my_sql.cursor()
            sql = f"INSERT INTO short_changed (long_url, short_url) VALUES ('{longurl}', '{shorturl}');"
            cursor.execute(sql)
            self.my_sql.commit()
            return True

        else:
            return False

    # Check if a long url is in the database
    def long_url_exists(self, longurl):
        cursor = self.my_sql.cursor()
        cursor.execute(f"SELECT EXISTS(SELECT * FROM short_changed WHERE long_url = '{longurl}');")
        result = cursor.fetchone()
        return bool(result[0])

    # Check if a short url is in the database
    def short_url_exists(self, shorturl):
        cursor = self.my_sql.cursor()
        cursor.execute(f"SELECT EXISTS(SELECT * FROM short_changed WHERE short_url = '{shorturl}');")
        result = cursor.fetchone()
        return bool(result[0])

    # Get the long url corresponding to a short URL
    def get_long_url(self, shorturl):
        cursor = self.my_sql.cursor()
        cursor.execute(f"SELECT long_url FROM short_changed WHERE short_url = '{shorturl}'")
        result = cursor.fetchone()
        return result[0]

    # Get the short url corresponding to a long URL
    def get_short_url(self, longurl):
        cursor = self.my_sql.cursor()
        cursor.execute(f"SELECT short_url FROM short_changed WHERE long_url = '{longurl}'")
        result = cursor.fetchone()
        return result[0]
