from flask import Flask, Blueprint, request, flash, url_for, redirect, render_template, jsonify, make_response
from flask_login import login_user, logout_user, current_user , login_required
from werkzeug.security import check_password_hash, generate_password_hash

from ..models import orders
from ..models import listings
from ..models import user


order_endpoints = Blueprint('order_endpoints', __name__)


@order_endpoints.route('/customer_dashboard/view_orders', methods=['GET'])
def customer_view_orders():
    customer_id = current_user.user_id
    return jsonify(orders.get_orders_by_customerid(customer_id))


@order_endpoints.route('/renter_dashboard/view_pending_request', methods=['GET'])
@login_required
def renter_view_pending_request():
    renter_id = current_user.user_id
    data = orders.get_request_by_renterid(renter_id)
    result = []
    for d in data:
        customer_username = user.get_username_by_id(d[2])
        house = listings.get_listing_by_houseid(d[0])[0]
        # print(house)
        house_name = house[2]
        js = {"house_id": d[0], "landlord_id": d[1], "customer_id": d[2], "create_date": d[3], "status": d[4],
              "customer_username": customer_username, "house_name": house_name}
        result.append(js)
    # print(data)
    return render_template("renter_pending_request.html", data = result)


@order_endpoints.route('/customer_dashboard/view_pending_request', methods=['GET'])
@login_required
def customer_view_pending_request():
    customer_id = current_user.user_id
    return jsonify(orders.get_request_by_customerid(customer_id))


@order_endpoints.route('/renter_dashboard/view_orders', methods=['GET'])
@login_required
def renter_view_orders():
    renter_id = current_user.user_id
    data = orders.get_orders_by_renterid(renter_id)
    result = []
    for d in data:
        customer_username = user.get_username_by_id(d[2])
        landlord_username = user.get_username_by_id(renter_id)
        house = listings.get_listing_by_houseid(d[0])[0]
        # print(house)
        house_name = house[2]
        js = {"house_id": d[0], "landlord_id": d[1], "customer_id": d[2], "create_date": d[3],
              "customer_username": customer_username, "house_name": house_name, "landlord_username": landlord_username}
        result.append(js)
    return render_template("renter_orders.html", data = result, )


@order_endpoints.route('/place_order', methods=['POST'])
@login_required
def place_order():
    house_id = request.form['house_id']
    pending_request = orders.get_request_by_houseid(house_id)[0]
    renter_id = pending_request[1]
    customer_id = pending_request[2]
    orders.place_order(house_id, renter_id, customer_id)
    return redirect('/renter_dashboard/view_pending_request')


@order_endpoints.route('/delete_request', methods=['POST'])
@login_required
def delete_request():
    house_id = request.form['house_id']
    # renter_id = current_user.user_id
    # customer_id = request.form['customer_id']
    orders.delete_renting_request(house_id)
    return redirect('/renter_dashboard/view_pending_request')


@order_endpoints.route('/send_renting_request', methods=['POST'])
@login_required
def send_renting_request():
    house_id = request.form['house_id']
    customer_id = current_user.user_id
    rented_house = listings.get_listing_by_houseid(house_id)[0]

    renter_id = rented_house[1]
    if renter_id == customer_id:
        return make_response(jsonify({'code': '404',
                                      'msg': 'You cannot rent your own house'}), 400)
    orders.add_renting_request(house_id, renter_id, customer_id)
    return redirect('/customer_dashboard/view_pending_request')
