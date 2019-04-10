import mysql.connector
conn = mysql.connector.connect(host = "csc648-db-team13.covsgblvixwf.us-east-2.rds.amazonaws.com",
                            database = 'CSC648',
                            user = 'root',
                            password = 'root1234',
                            auth_plugin='mysql_native_password')
cursor = conn.cursor()


# conn = mysql.connector.connect(host = "localhost",
#                             database = 'CSC648',
#                             user = 'root',
#                             password = 'Derectorjin1',
#                             auth_plugin='mysql_native_password')
# cursor = conn.cursor()




