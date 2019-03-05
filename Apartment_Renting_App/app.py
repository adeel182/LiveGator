import os
from flask import Flask, session, request, flash, redirect, render_template
from flask_login import LoginManager, login_required
from werkzeug.routing import Map, Rule, NotFound, RequestRedirect
from backend.views.user import user_endpoints
from backend.views.listings import listing_endpoints
from backend.views.dashboard import dashboard_endpoints
from backend.views.orders import order_endpoints
from backend.views.message import message_endpoints

from backend.models.user import User


app = Flask(__name__)
app.secret_key = os.urandom(24)
app.register_blueprint(user_endpoints)
app.register_blueprint(listing_endpoints)
app.register_blueprint(dashboard_endpoints)
app.register_blueprint(order_endpoints)
app.register_blueprint(message_endpoints)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'
@login_manager.user_loader
def load_user(id):
    return User(id)



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


@app.route('/about', methods=['GET', 'POST'])
@login_required
def about():
    return render_template('about.html')


@app.route('/about/AmarisAboutMe', methods=['GET', 'POST'])
def aboutAmarisAboutMe():
    return render_template('AmarisAboutMe.html')


@app.route('/about/kim', methods=['GET', 'POST'])
def aboutKim():
    return render_template('Kim.html')


@app.route('/about/sushil', methods=['GET', 'POST'])
def aboutSushil():
    return render_template('sushil.html')

@app.route('/about/Kurtis', methods=['GET', 'POST'])
def aboutKurtis():
    return render_template('Kurtis.html')

@app.route('/about/Adeel', methods=['GET', 'POST'])
def aboutAdeel():
    return render_template('Adeel.html')

@app.route('/about/simon', methods=['GET', 'POST'])
def aboutSimon():
    return render_template('simon.html')

@app.route('/about/brian', methods=['GET', 'POST'])
def aboutBrian():
    return render_template('brian.html')

##Template copy the following three lines and make some changes:
##1. on first line, replace your name in the url; eg: '/about/kim'
##2. on second line, rename the def function (every def function needs to be unique); eg: def aboutKim()
##3. create your own html file under "templates" folder, and rename the html file properly; eg: Kim.html
##4. modify your html file properly. Please refer to TEMPLATE.html for instruction
##4. on third line, replace your html file name in the bracket (needs to be exactly same the name)


if __name__ == "__main__":
    app.run()
