from ..db.connection import cursor

def addUser():
    sqlStr = "SELECT * from USER"
    cursor.execute(sqlStr)
    return cursor.fetchall()







