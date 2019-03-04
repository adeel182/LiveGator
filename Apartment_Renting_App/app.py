import os
from flask import Flask, session, request, flash, redirect, render_template
from flask_login import LoginManager
from backend.views.user import user_endpoints
from backend.models.user import User
from flask_login import login_user, logout_user , current_user , login_required

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.register_blueprint(user_endpoints)

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
