Running instructions:

1. Clone the project, and use pycharm to open "Apartment_Renting_App" folder
2. Click "Configure Python Interpreter" on top right corner on app.py file
3. On Project Interpreter preference page, click "Add.." on the right side, and then select "New environment", set location to be "~Apartment_Renting_App/venv", and uncheck "Inherit global site-packages". Click OK
4. If the interpreter is initialized with pip 7 or 8 or lower version then try another base interpreter (pip needs to be 10.0.1 or higher) 
5. Click "Terminal" tab on the bottom of pycharm, type 'pip install -r requirements.txt' to install all required dependencies
6. Run 'pip freeze > requirements.txt' everytime a new module is added (or before every commit)
7. cd to db folder, create a new file called "connection.py", and paste the following code with database, user and password updated using your credentials:

    
        import mysql.connector
        conn = mysql.connector.connect(host = "localhost",
                                   port = 3306,
                                   database = 'YOUR DATABASE NAME',
                                   user = 'YOUR USERNAME',
                                   password = 'YOUR PASSWORD',
                                   auth_plugin='mysql_native_password')
        cursor = conn.cursor()

8. Configure data source for this project (https://www.jetbrains.com/help/pycharm/managing-data-sources.html)
9. Under "mysql" folder, right click "schema.sql" to initialize db schema and testing data 
10. On pycharm terminal tab, type the followings command to display all registered routes:

        python
        >>> from app import app
        >>> app.url_map
