from ..db.connection import cursor

def addUser():
    sqlStr = "SELECT * from test"
    cursor.execute(sqlStr)
    return cursor.fetchall()







