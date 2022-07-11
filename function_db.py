import db
import datetime
from datetime import timedelta

database = db.connect()

try:
    Mycursor = database.cursor()
except:
    print("Cursor failed to select")

def get_status():
    if database == False:
        print("[DB]: Not connected")
    else:
        print("[DB]: Connected")

def get_users():
    Mycursor.execute("SELECT * FROM user")
    users = Mycursor.fetchall()
    for user in range(len(users)):
        print(users[user][1])

#Select; update; delete; insert;
def set_user(user_ID, nickname):
    if not is_user_exist(user_ID):
        sql = "INSERT INTO user (user_ID, Nickname, daily_bonus) VALUES ({0}, '{1}', '{2}')".format(user_ID, nickname.name, datetime.datetime.now().date() - timedelta(days=1))
        # values = (user_ID, Nickname)
        Mycursor.execute(sql)

        database.commit()
        print(f"User {nickname.name} is registered!")
        print(f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-{nickname.name}-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    #else:
        #print("User is already registered!")

def is_user_exist(user_ID):
    sql = "SELECT * FROM user WHERE user_ID = '{0}'".format(user_ID)
    Mycursor.execute(sql)
    result = Mycursor.fetchall()

    if not result:
        return False
    else:
        return True

def set_daily_date(user_ID):
    now = datetime.datetime.now().date()
    
    sql = "UPDATE `user` SET `daily_bonus`='{0}' WHERE user_ID = {1}".format(now, user_ID)
    Mycursor.execute(sql)
    database.commit()

def get_user_profile(user_ID):
    sql = "SELECT * FROM user WHERE user_ID = '{0}'".format(user_ID)
    Mycursor.execute(sql)
    user_profile = Mycursor.fetchall()
    
    return user_profile

def update_user_profile(user_ID, value, winning, losing):
    sql = "UPDATE `user` SET `Wallet`='{0}', `winning` = '{1}', `losing` = '{2}' WHERE user_ID = {3}".format(value, winning, losing, user_ID)
    Mycursor.execute(sql)
    database.commit()