import mysql.connector
conn = mysql.connector.connect(host = "localhost",
                            port = 3306,
                            database = 'CSC648',
                            user = 'root',
                            password = 'Derectorjin1',
                            auth_plugin='mysql_native_password')
cursor = conn.cursor()