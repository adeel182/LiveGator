import os
from flask import Flask, session, request, flash, redirect, render_template
from flask_login import LoginManager, login_required
from flask_restful import Api
from flask_restful_swagger import swagger
from backend.views.user import user_endpoints
from backend.views.listings import listing_endpoints
from backend.views.about_page import about_page_endpoints
from backend.views.dashboard import dashboard_endpoints
from backend.views.orders import order_endpoints
from backend.views.message import message_endpoints

from backend.models.user import User


app = Flask(__name__)
app.secret_key = os.urandom(24)
app.register_blueprint(user_endpoints)
app.register_blueprint(listing_endpoints)
app.register_blueprint(about_page_endpoints)
app.register_blueprint(dashboard_endpoints)
app.register_blueprint(order_endpoints)
app.register_blueprint(message_endpoints)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'
@login_manager.user_loader
def load_user(id):
    return User(id)

# Wrap the Api with swagger.docs. It is a thin wrapper around the Api class that adds some swagger smarts
api = swagger.docs(Api(app), apiVersion='0.1')


# url_map = Map([
#     Rule('/', endpoint='blog/index'),
#     Rule('/<int:house_id>/', endpoint='all_listings/'),
#     Rule('/<int:year>/<int:month>/', endpoint='blog/archive'),
#     Rule('/<int:year>/<int:month>/<int:day>/', endpoint='blog/archive'),
#     Rule('/<int:year>/<int:month>/<int:day>/<slug>',
#          endpoint='blog/show_post'),
#     Rule('/about', endpoint='blog/about_me'),
#     Rule('/feeds/', endpoint='blog/feeds'),
#     Rule('/feeds/<feed_name>.rss', endpoint='blog/show_feed')
# ])



@app.route("/", methods=['GET', 'POST'])
def home():
    flash('Logged in successfully')

    # cursor.execute("SELECT * from test")
    # data = cursor.fetchall()
    # print(data)
    return render_template('home.html')



if __name__ == "__main__":
    app.run()
