####################################
# File name: dashboard.py          #
# Description:
# Author: Team-13                  #
# Submission: Spring-2019          #
# Instructor: Dragutin Petkovic    #
####################################
from flask import Flask, Blueprint, request, flash, url_for, redirect, render_template
from flask_login import login_user, logout_user, current_user , login_required
from werkzeug.security import check_password_hash, generate_password_hash

from ..models import user

dashboard_endpoints = Blueprint('dashboard_endpoints', __name__)


@dashboard_endpoints.route('/customer_dashboard', methods=['GET'])
@login_required
def customer_dashboard():
    loggedin_user = user.get_user_by_id(current_user.user_id)
    username = loggedin_user[1]
    return render_template('customer_dashboard.html', username = username)


@dashboard_endpoints.route('/landlord_dashboard', methods=['GET'])
@login_required
def renter_dashboard():
    loggedin_user = user.get_user_by_id(current_user.user_id)
    username = loggedin_user[1]
    return render_template('renter_dashboard.html', username = username)



# @dashboard_endpoints.route('/admin_dashboard', methods=['GET'])
# @login_required
# def admin_dashboard():
#     loggedin_user = user.get_user_by_id(current_user.user_id)
#     if loggedin_user[4] != 2:
#         return redirect('/')
#     return render_template('admin_dashboard.html')