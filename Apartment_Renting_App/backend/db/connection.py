import mysql.connector
conn = mysql.connector.connect(host = "csc648-db-team13.covsgblvixwf.us-east-2.rds.amazonaws.com",
                            database = 'Team13_DBinstance',
                            user = 'root',
                            password = 'root1234',
                            auth_plugin='mysql_native_password')
cursor = conn.cursor()

#
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'root1234'
# app.config['MYSQL_DATABASE_DB'] = 'Team13_DBinstance'
# app.config['MYSQL_DATABASE_HOST'] = 'csc648-db-team13.covsgblvixwf.us-east-2.rds.amazonaws.com'
#
# mysql = MySQL()
# mysql.init_app(app)
# conn = mysql.connect()
# cursor = conn.cursor()


