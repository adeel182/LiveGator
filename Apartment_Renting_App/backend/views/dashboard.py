from flask import Flask, Blueprint, request, flash, url_for, redirect, render_template
from flask_login import login_user, logout_user, current_user , login_required
from werkzeug.security import check_password_hash, generate_password_hash

from ..models import user
from ..models.user import User

dashboard_endpoints = Blueprint('dashboard_endpoints', __name__)

# @dashboard_endpoints.route('/login', methods=['GET', 'POST'])
# def login():