Running instructions:

1. Clone the project
2. Open a new terminal and cd to Apartment_Renting_Application folder
3. Type 'pip install -r requirements.txt' to install all required dependencies
4. Run 'pip freeze > requirements.txt' everytime a new module is added (or before every commit)
5. cd to db folder, create a new file called "connection.py", and paste the following code with database, user and password updated using your credentials:
    
    import mysql.connector

    conn = mysql.connector.connect(host = "localhost",
                               port = 3306,
                               database = 'YOUR DATABASE NAME',
                               user = 'YOUR USERNAME',
                               password = 'YOUR PASSWORD',
                               auth_plugin='mysql_native_password')
    cursor = conn.cursor()
