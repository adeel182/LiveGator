from ..db.connection import conn, cursor


def get_user(user_id):
    sql_str = "SELECT * from USER WHERE user_id = %s"
    cursor.execute(sql_str, (user_id, ))
    return cursor.fetchall()


def login2(username, password):
    sql_str = "SELECT * from USER WHERE username = %s and password = %s"
    cursor.execute(sql_str, (username, password))
    return cursor.fetchone()


def login(username):
    sql_str = "SELECT * from USER WHERE username = %s"
    cursor.execute(sql_str, (username, ))
    return cursor.fetchone()


def signup(username, password, email, isStudent):
    sql_str = "INSERT INTO USER (username,password,email,isStudent) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql_str, (username, password, email, isStudent))
    conn.commit()
