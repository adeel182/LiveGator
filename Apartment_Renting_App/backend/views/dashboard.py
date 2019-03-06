from flask import Flask, Blueprint, request, flash, url_for, redirect, render_template
from flask_login import login_user, logout_user, current_user , login_required
from werkzeug.security import check_password_hash, generate_password_hash



dashboard_endpoints = Blueprint('dashboard_endpoints', __name__)


@dashboard_endpoints.route('/customer_dashboard', methods=['GET'])
def customer_dashboard():
    return render_template('customer_dashboard.html')


@dashboard_endpoints.route('/renter_dashboard', methods=['GET'])
def renter_dashboard():
    return render_template('renter_dashboard.html')