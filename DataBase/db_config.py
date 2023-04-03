import sqlite3

PATH = 'DataBase/db_new_bot.db'

connect = sqlite3.connect(PATH)
corsor = connect.cursor()

def create_table():
    corsor.execute('''CREATE TABLE IF NOT EXISTS user (user_id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR, 
    tg_id INTEGER, phone VARCHAR, comment VARCHAR)''')
    connect.commit()

def add_new_user(new_user: tuple):
    corsor.execute('''INSERT INTO user(name, tg_id, phone, comment) VALUES (?, ?, ?, ?)''', new_user)
    connect.commit()

def find_user(name: tuple):
    user = corsor.execute('''SELECT * FROM user WHERE name=?''', name).fetchall()
    return user

def change_user(new_data: tuple):
    corsor.execute('''UPDATE user SET name=?, phone=?, comment=? WHERE user_id=?''', new_data)
    connect.commit()

def delete_user(user: tuple):
    corsor.execute('''DELETE FROM user WHERE user_id=?''', user)
    connect.commit()