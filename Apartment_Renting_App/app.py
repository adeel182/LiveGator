####################################
# File name: app.py                #
# Description: 
# Author: Team-13                  #
# Submission: Spring-2019          #
# Instructor: Dragutin Petkovic    #
####################################

import os
from flask import Flask, session, request, flash, redirect, render_template, url_for
from flask_login import LoginManager, login_required, current_user
from flaskext.couchdb import CouchDBManager, Document, TextField, DateTimeField, ViewField
from flask_uploads import UploadSet, configure_uploads, IMAGES, UploadNotAllowed
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
from backend.models import user
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


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'
@login_manager.user_loader
def load_user(id):
    return User(id)


UPLOADED_PHOTOS_DEST = os.path.join('static', 'photos')
# COUCHDB_SERVER = 'http://localhost:5000/'
# COUCHDB_DATABASE = 'flask-photolog'
app.config.from_object(__name__)
# app.config.from_envvar('PHOTOLOG_SETTINGS', silent=True)
uploaded_photos = UploadSet('photos', IMAGES)
configure_uploads(app, uploaded_photos)
# manager = listings.manager
# manager.setup(app)


@app.route("/", methods=['GET', 'POST'])
def home():
    search_key = request.args.get("search_key", "")
    sort = request.args.get("sort", -1)
    type = request.args.get("type", "")
    data = listings.display_all_listings()
    # user = current_user
    username = "visitor"
    role = -1
    try:
        loggedin_user = user.get_user_by_id(current_user.user_id)
        username = loggedin_user[1]
        role = loggedin_user[4]
    except:
        username = "visitor"
        role = -1
    return render_template('home_search.html', data = data, current_user = current_user,
                           username = username, role = role, key = search_key, sort = sort, type = type)

@app.route("/search_results", methods=['GET', 'POST'])
def search_results():
    search_key = request.args.get("search_key", "")
    sort = request.args.get("sort", -1)
    type = request.args.get("type", "")
    data = listings.display_all_listings()
    username = "visitor"
    role = -1
    try:
        loggedin_user = user.get_user_by_id(current_user.user_id)
        username = loggedin_user[1]
        role = loggedin_user[4]
    except:
        username = "visitor"
        role = -1
    return render_template('home_search_results.html', data=data, current_user=current_user,
                           username=username, role = role, key=search_key, sort=sort, type=type)


@app.route("/search", methods=['GET', 'POST'])
def search():
    search_key = request.args.get("search_key", "")
    sort = request.args.get("sort", -1)
    type = request.args.get("type", "")
    data = listings.display_all_listings()
    username = "visitor"
    role = -1
    try:
        loggedin_user = user.get_user_by_id(current_user.user_id)
        username = loggedin_user[1]
        role = loggedin_user[4]
    except:
        username = "visitor"
        role = -1
    return render_template('home_search_results.html', data=data, current_user=current_user,
                           username=username, role = role, key=search_key, sort=sort, type=type)



    # when hosting on AWS server
    # Comment the app.run() and
    # Uncomment the app.run(host='0.0.0.0', port=80, debug=True) -- used for opening ports, and allow connections to website

if __name__ == "__main__":
    # app.run()
    app.run(host='0.0.0.0', port=80, debug=True)

