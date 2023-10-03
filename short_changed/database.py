import mysql.connector


class Database:
    def __init__(self):
        """ THE CODE THAT IS COMMENTED OUT IN THE __INIT__ FUNCTION CAN BE USED TO CREATE THE DATABASE
        THE FIRST TIME THE PROGRAM IS RUN """

        # Initialize the database
        # self.my_sql = mysql.connector.connect(host="localhost",
        #                                       user="root",
        #                                       password="CWkkW&1lTg6+&(4")
        # cursor = self.my_sql.cursor()
        # cursor.execute("CREATE DATABASE shortchanged")

        self.my_sql = mysql.connector.connect(host="localhost",
                                              user="root",
                                              password="your password",  # change this to your mysql password
                                              database="shortchanged")

        # Add table short_changed to the database
        # cursor = self.my_sql.cursor()
        # cursor.execute("CREATE TABLE short_changed (long_url VARCHAR(255), short_url VARCHAR(7))")

    # Add a row (long URL and short URL) to the database
    def add_data(self, longurl: str, shorturl: str):

        if not self.long_url_exists(longurl):
            cursor = self.my_sql.cursor()
            sql = f"INSERT INTO url_shortener (long_url, short_url) VALUES ('{longurl}', '{shorturl}');"
            cursor.execute(sql)
            self.my_sql.commit()
            return True

        else:
            return False

    # Check if a long url is in the database
    def long_url_exists(self, longurl):
        cursor = self.my_sql.cursor()
        cursor.execute(f"SELECT EXISTS(SELECT * FROM url_shortener WHERE long_url = '{longurl}');")
        result = cursor.fetchone()
        return bool(result[0])

    # Check if a short url is in the database
    def short_url_exists(self, shorturl):
        cursor = self.my_sql.cursor()
        cursor.execute(f"SELECT EXISTS(SELECT * FROM url_shortener WHERE short_url = '{shorturl}');")
        result = cursor.fetchone()
        return bool(result[0])

    # Get the long url corresponding to a short URL
    def get_long_url(self, shorturl):
        cursor = self.my_sql.cursor()
        cursor.execute(f"SELECT long_url FROM url_shortener WHERE short_url = '{shorturl}'")
        result = cursor.fetchone()
        return result[0]

    # Get the short url corresponding to a long URL
    def get_short_url(self, longurl):
        cursor = self.my_sql.cursor()
        cursor.execute(f"SELECT short_url FROM url_shortener WHERE long_url = '{longurl}'")
        result = cursor.fetchone()
        return result[0]
