from flask import Flask, Blueprint, request, flash, url_for, redirect, render_template, make_response, jsonify
from flask_login import login_user, logout_user, current_user , login_required, LoginManager

from ..models import admin
from ..models.user import User


admin_endpoints = Blueprint('admin_endpoints', __name__)


@admin_endpoints.route('/get_all_to_approve', methods=['GET'])
@login_required
def get_all_to_approve():
    if current_user.role is not 2:
        return make_response(jsonify({'code': '400',
                                      'msg': 'You are not authorized'}), 400)
    return admin.get_all_to_approve()


@admin_endpoints.route('/get_all_to_approve/<house_id>', methods=['POST'])
@login_required
def approve_new_listing(house_id):
    if current_user.role is not 2:
        return make_response(jsonify({'code': '400',
                                      'msg': 'You are not authorized'}), 400)
    admin.approve_new_listing(house_id)


@admin_endpoints.route('/block_user/<user_id>', methods=['POST'])
@login_required
def block_user(user_id):
    if current_user.role is not 2:
        return make_response(jsonify({'code': '400',
                                      'msg': 'You are not authorized'}), 400)
    admin.block_user(user_id)