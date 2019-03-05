from flask import Flask, Blueprint, request, flash, url_for, redirect, render_template, jsonify, make_response
from flask_login import login_user, logout_user, current_user , login_required
from werkzeug.security import check_password_hash, generate_password_hash

from ..models import orders
from ..models import listings


order_endpoints = Blueprint('order_endpoints', __name__)


@order_endpoints.route('/customer_dashboard/view_orders', methods=['GET'])
def customer_view_orders():
    customer_id = current_user.user_id
    return jsonify(orders.get_orders_by_customerid(customer_id))


@order_endpoints.route('/renter_dashboard/view_orders', methods=['GET'])
@login_required
def renter_view_orders():
    renter_id = current_user.user_id
    return jsonify(orders.get_orders_by_renterid(renter_id))


@order_endpoints.route('/place_order', methods=['POST'])
@login_required
def place_order():
    house_id = request.form['house_id']
    customer_id = current_user.user_id
    rented_house = listings.get_listing_by_houseid(house_id)
    print(rented_house)
    renter_id = rented_house[1]
    if renter_id == customer_id:
        return make_response(jsonify({'code': '404',
                                      'msg': 'You cannot rent your own house'}), 400)
    print("customer_id:", customer_id, "renter_id:", renter_id)
    orders.place_order(house_id, renter_id, customer_id)
    return jsonify("Order placed successfully", rented_house)

