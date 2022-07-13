import db
import datetime
from datetime import timedelta

database = db.connect()

try:
    Mycursor = database.cursor(dictionary=True)
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
        print(users[user]["nickname"])

def set_guild(guild):
    if not is_guild_exist(guild.id):
        sql = "INSERT INTO guilds (guild_id, guild_name) VALUES ('{0}', '{1}')".format(guild.id, guild.name)
        Mycursor.execute(sql)

        database.commit()
        print(f"Guild {guild.name} is registered!")
        print(f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-{guild.name}-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

def is_guild_exist(guild_id):
    sql = "SELECT * FROM guilds WHERE guild_id = '{0}'".format(guild_id)
    Mycursor.execute(sql)
    result = Mycursor.fetchone()

    if not result:
        return False
    else:
        return True
def get_guild(guild_id):
    sql = "SELECT * FROM guilds WHERE guild_id = '{0}'".format(guild_id)
    Mycursor.execute(sql)
    guild = Mycursor.fetchone()

    return guild

def set_user(user_id, nickname):
    if not is_user_exist(user_id):
        sql = "INSERT INTO user (user_id, Nickname, daily_bonus) VALUES ({0}, '{1}', '{2}')".format(user_id, nickname.name, datetime.datetime.now().date() - timedelta(days=1))
        Mycursor.execute(sql)

        database.commit()
        print(f"User {nickname.name} is registered!")
        print(f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-{nickname.name}-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

def is_user_exist(user_id):
    sql = "SELECT * FROM user WHERE user_ID = '{0}'".format(user_id)
    Mycursor.execute(sql)
    result = Mycursor.fetchall()

    if not result:
        return False
    else:
        return True

def set_daily_date(user_id):
    now = datetime.datetime.now().date()
    
    sql = "UPDATE `user` SET `daily_bonus`='{0}' WHERE user_id = {1}".format(now, user_id)
    Mycursor.execute(sql)
    database.commit()

def get_user_profile(user_id):
    sql = "SELECT * FROM user WHERE user_id = '{0}'".format(user_id)
    Mycursor.execute(sql)
    user_profile = Mycursor.fetchone()
    
    return user_profile

def get_users_profile():
    Mycursor.execute("SELECT * FROM user")
    users = Mycursor.fetchall()
    return users


def update_user_profile(user, value):
    sql = "UPDATE `user` SET `wallet`='{0}' WHERE user_id = {1}".format(value, user.id)
    Mycursor.execute(sql)
    database.commit()

def update_stats(user, user_winning, user_loss, guild_winning, guild_loss):
    sql = [
        "UPDATE `user` SET `winning` = '{0}', `loss` = '{1}' WHERE user_id = {2}".format(user_winning, user_loss,user.author.id),
        "UPDATE `guilds` SET `total_winning` = '{0}', `total_loss` = '{1}' WHERE guild_id = {2}".format(guild_winning, guild_loss, user.guild.id)
    ]
    for e in sql:
        Mycursor.execute(e)
    database.commit()