from flask import Flask, Blueprint, request, flash, url_for, redirect, render_template
from flask_login import login_user, logout_user, current_user , login_required
from werkzeug.security import check_password_hash, generate_password_hash

from ..models import user
from ..models.user import User

dashboard_endpoints = Blueprint('dashboard_endpoints', __name__)


@dashboard_endpoints.route('/customer_dashboard', methods=['GET'])
@login_required
def customer_dashboard():
    return render_template('customer_dashboard.html')


@dashboard_endpoints.route('/renter_dashboard', methods=['GET'])
@login_required
def renter_dashboard():
    return render_template('renter_dashboard.html')



# @dashboard_endpoints.route('/admin_dashboard', methods=['GET'])
# @login_required
# def admin_dashboard():
#     loggedin_user = user.get_user_by_id(current_user.user_id)
#     if loggedin_user[4] != 2:
#         return redirect('/')
#     return render_template('admin_dashboard.html')