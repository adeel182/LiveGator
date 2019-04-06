from flask import Flask, Blueprint, request, flash, url_for, redirect, render_template
from flask_login import login_user, logout_user, current_user , login_required
from werkzeug.security import check_password_hash, generate_password_hash

from ..models import user
from ..models.user import User

user_endpoints = Blueprint('user_endpoints', __name__)



@user_endpoints.route('/login', methods=['GET', 'POST'])
def login():
    # print(1)
    if request.method == 'GET':
        # print(2)
        return render_template('login.html')
    # print(request)
    username = request.form['username']
    password = request.form['password']
    # hash_pwd = generate_password_hash(password)
    # print("username:", username, "password:", password)
    # user_found2 = user.login2(username, password)
    # print("2", type(user_found2))
    user_query = user.login(username)
    # print("1", type(user_found))

    if user_query is None:
        print("username not found")
        flash('Username is invalid' , 'error')
        return redirect('/login')
    print(user_query)
    hashed_pwd = user_query[2]
    # print(hashed_pwd)
    if not check_password_hash(hashed_pwd, password):
        print("invalid password")
        flash('Password is invalid', 'error')
        return redirect('/login')
    user_found = User(user_query[0])
    login_user(user_found)
    flash('Logged in successfully')
    print("Logged in successfully")
    return redirect(request.args.get('next') or '/')



@user_endpoints.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    try:
    # print(request.form['is_student'])
        password = request.form['password']
        hashed_pwd = generate_password_hash(password)
        user.signup(request.form['username'], hashed_pwd, request.form['email'], request.form['is_student'])
    except:
        flash('Duplicate username. Please try again')
        return redirect('/signup')
    flash('User successfully registered')
    return redirect('/login')


@user_endpoints.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))