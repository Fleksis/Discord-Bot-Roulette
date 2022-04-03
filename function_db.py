import db

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
    print(Mycursor.fetchall())

#Select; update; delete; insert;
def set_user(user_ID, Nickname):
    if not is_user_exist(user_ID):
        sql = "INSERT INTO user (user_ID, Nickname) VALUES ({0}, '{1}')".format(user_ID, Nickname)
        print(sql)
        # values = (user_ID, Nickname)
        Mycursor.execute(sql)

        database.commit()
        print(f"User {Nickname} is registered!")
    else:
        print("User is already registered!")

def is_user_exist(user_ID):
    sql = "SELECT * FROM user WHERE user_ID = '{0}'".format(user_ID)
    Mycursor.execute(sql)
    result = Mycursor.fetchall()

    if not result:
        return False
    else:
        return True

def get_user_profile(user_ID):
    sql = "SELECT * FROM user WHERE user_ID = '{0}'".format(user_ID)
    Mycursor.execute(sql)
    user_profile = Mycursor.fetchall()
    
    return user_profile

def update_user_profile(user_ID, value):
    sql = "UPDATE `user` SET `Wallet`='{0}' WHERE user_ID = {1}".format(value,user_ID)
    Mycursor.execute(sql)
    database.commit()