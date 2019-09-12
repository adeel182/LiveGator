####################################
# File name: user.py               #
# Description:
# Author: Team-13                  #
# Submission: Spring-2019          #
# Instructor: Dragutin Petkovic    #
####################################
from ..db import DButils


def get_user_by_id(user_id):
    return DButils.get_user("user_id", user_id)


def get_user_by_username(username):
    return DButils.get_user("username", username)

def get_username_by_id(user_id):
    user = DButils.get_user("user_id", user_id)
    return user[1]

def login(username):
    return DButils.login(username)


def signup(username, password, email, isStudent):
    DButils.signup(username, password, email, isStudent)


class User():
    # __tablename__ = "USER"
    # id = db.Column('user_id', db.Integer, primary_key=True)
    # username = db.Column('username', db.String(20), unique=True, index=True)
    # password = db.Column('password', db.String(10))
    # email = db.Column('email', db.String(50), unique=True, index=True)
    # registered_on = db.Column('registered_on', db.DateTime)

    def __init__(self, user_id):
        self.user_id = user_id



    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.user_id)

    def get_username(self):
        try:
            return get_user_by_id(self.user_id)[1]
        except:
            return "Visitor"
    # def __repr__(self):
    #     return '<User %r>' % (self.username)