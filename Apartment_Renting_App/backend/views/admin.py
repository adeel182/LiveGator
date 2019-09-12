####################################
# File name: admin.py              #
# Description:
# Author: Team-13                  #
# Submission: Spring-2019          #
# Instructor: Dragutin Petkovic    #
####################################
from flask import Flask, Blueprint, request, flash, url_for, redirect, render_template, make_response, jsonify
from flask_login import login_user, logout_user, current_user , login_required, LoginManager

from ..models import admin
from ..models import user
from ..models.user import User


admin_endpoints = Blueprint('admin_endpoints', __name__)


# @admin_endpoints.route('/get_all_to_approve', methods=['GET'])
# @login_required
# def get_all_to_approve():
#     if current_user.role is not 2:
#         return make_response(jsonify({'code': '400',
#                                       'msg': 'You are not authorized'}), 400)
#     return admin.get_all_to_approve()


@admin_endpoints.route('/approve_new_listing', methods=['GET','POST'])
@login_required
def approve_new_listing():
    role = user.get_user_by_id(current_user.user_id)[4]
    if role is not 2:
        return make_response(jsonify({'code': '400',
                                      'msg': 'You are not authorized'}), 400)
    if request.method == 'GET':
        data = admin.get_all_to_approve()
        result = []
        for d in data:
            landlord = user.get_username_by_id(d[1])
            js = {"house_id": d[0], "house_name": d[2],"landlord": landlord, "create_date": d[18]}
            result.append(js)
        return render_template("admin_dashboard.html", data = result)
    house_id = request.form["house_id"]
    admin.approve_new_listing(house_id)
    return redirect('/approve_new_listing')

@admin_endpoints.route('/block_user/<user_id>', methods=['POST'])
@login_required
def block_user(user_id):
    if current_user.role is not 2:
        return make_response(jsonify({'code': '400',
                                      'msg': 'You are not authorized'}), 400)
    admin.block_user(user_id)