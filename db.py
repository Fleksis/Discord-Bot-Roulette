import mysql.connector

def connect():
    try:
        mydb = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password = "",
            database = "roulette_dc_bot"
        )
        return mydb
    except:
        return False