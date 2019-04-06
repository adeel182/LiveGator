import os
from flask import Flask, session, request, flash, redirect, render_template, url_for
from flask_login import LoginManager, login_required, current_user
from flask_restful import Api
from flask_restful_swagger import swagger
from backend.views.user import user_endpoints
from backend.views.listings import listing_endpoints
from backend.views.about_page import about_page_endpoints
from backend.views.dashboard import dashboard_endpoints
from backend.views.orders import order_endpoints
from backend.views.admin import admin_endpoints
from backend.views.message import message_endpoints
from backend.models.user import User
from backend.views import listings
from flaskext.mysql import MySQL



app = Flask(__name__)
app.secret_key = os.urandom(24)
app.register_blueprint(user_endpoints)
app.register_blueprint(listing_endpoints)
app.register_blueprint(about_page_endpoints)
app.register_blueprint(dashboard_endpoints)
app.register_blueprint(order_endpoints)
app.register_blueprint(message_endpoints)
app.register_blueprint(admin_endpoints)

# Database connection info. Note that this igit@github.com:CSC-648-SFSU/csc648-sp19-team13.gitgit@github.com:CSC-648-SFSU/csc648-sp19-team13.gitgit@github.com:CSC-648-SFSU/csc648-sp19-team13.git not a secure connection.
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root1234'
app.config['MYSQL_DATABASE_DB'] = 'Team13_DBinstance'
app.config['MYSQL_DATABASE_HOST'] = 'csc648-db-team13.covsgblvixwf.us-east-2.rds.amazonaws.com'

mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'
@login_manager.user_loader
def load_user(id):
    return User(id)




@app.route("/", methods=['GET', 'POST'])
def home():
    flash('Logged in successfully')

    # cursor.execute("SELECT * from test")
    # data = cursor.fetchall()
    # print(data)
    return render_template('home.html')

@app.route("/search", methods=['GET', 'POST'])
def search():

    # cursor.execute("SELECT * from test")
    # data = cursor.fetchall()
    # print(data)

    # key = first_name = request.args.get("firstname")
    #
    data = listings.display_all_listings()
    return render_template('search.html', data = data)


if __name__ == "__main__":
    app.run()
