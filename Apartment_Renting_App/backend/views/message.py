from flask import Flask, Blueprint, request, flash, url_for, redirect, render_template, jsonify, make_response
from flask_login import login_user, logout_user, current_user , login_required
from werkzeug.security import check_password_hash, generate_password_hash

from ..models import message
from ..models import listings
from ..models import user


message_endpoints = Blueprint('message_endpoints', __name__)


@message_endpoints.route('/customer_dashboard/view_msg', methods=['GET']) #return list of renter usernmae
@login_required
def customer_view_msg():
    customer_id = current_user.user_id
    data = message.get_msg_by_customerid(customer_id)
    result = []
    for d in data:
        js = {"renter_username": d}
        result.append(js)
    return render_template("customer_messages.html", data = result)


@message_endpoints.route('/renter_dashboard/view_msg', methods=['GET'])#return list of customer usernmae
@login_required
def renter_view_msg():
    renter_id = current_user.user_id
    data = message.get_msg_by_renterid(renter_id)
    result = []
    for d in data:
        js = {"customer_username": d}
        result.append(js)
    return render_template("renter_messages.html", data = result)


@message_endpoints.route('/customer_dashboard/view_msg/<username>', methods=['GET'])
@login_required
def customer_view_msg_detail(username):
    customer_id = current_user.user_id
    renter = user.get_user_by_username(username)
    renter_id = renter[0]
    data = message.get_msg_detail(renter_id, customer_id)
    result = []
    for d in data:
        sender = user.get_username_by_id(d[2])
        js = {"sender": sender, "message": d[3], "date": d[4], "renter_username": username}
        result.append(js)
    return render_template("customer_messages_detail.html", data = result)


@message_endpoints.route('/renter_dashboard/view_msg/<username>', methods=['GET'])
@login_required
def renter_view_msg_detail(username):
    renter_id = current_user.user_id
    customer = user.get_user_by_username(username)
    customer_id = customer[0]
    data = message.get_msg_detail(renter_id, customer_id)
    result = []
    for d in data:
        sender = user.get_username_by_id(d[2])
        js = {"sender": sender, "message": d[3], "date": d[4], "customer_username": username}
        result.append(js)
    return render_template("renter_message_detail.html", data = result)



@message_endpoints.route('/send_direct_msg', methods=['POST'])
@login_required
def send_direct_msg():
    customer_id = current_user.user_id
    customer_username = user.get_user_by_id(customer_id)[1]
    house_id = request.form["house_id"]
    contact_house = listings.get_listing_by_houseid(house_id)
    renter_id = contact_house[1]
    msg_to_send = request.form["message"]
    send_msg(renter_id, customer_id, customer_username, msg_to_send)


@message_endpoints.route('/customer_dashboard/view_msg/<username>/send_msg', methods=['POST'])
@login_required
def customer_send_msg(username):
    customer_id = current_user.user_id
    customer_username = user.get_user_by_id(customer_id)[1]
    renter = user.get_user_by_username(username)
    renter_id = renter[0]
    msg_to_send = request.form["message"]
    send_msg(renter_id, customer_id, customer_id, msg_to_send)
    redirect_url = '/customer_dashboard/view_msg/' + username
    return redirect(redirect_url)


@message_endpoints.route('/renter_dashboard/view_msg/<username>/send_msg', methods=['POST'])
@login_required
def renter_send_msg(username):
    renter_id = current_user.user_id
    renter_username = user.get_user_by_id(renter_id)[1]
    customer = user.get_user_by_username(username)
    customer_id = customer[0]
    msg_to_send = request.form["message"]
    send_msg(renter_id, customer_id, renter_id, msg_to_send)
    redirect_url = '/renter_dashboard/view_msg/' + username
    return redirect(redirect_url)


def send_msg(renter_id, customer_id, sender, msg_to_send):
    # print(type(renter_id))
    if customer_id is renter_id:
        return make_response(jsonify({'code': '400',
                                      'msg': 'You cannot send message to yourself'}), 400)
    try:
        # print("renter:", renter_id, "customer:", customer_id)
        message.send_msg(renter_id, customer_id, sender, msg_to_send)
    except:
        return make_response(jsonify({'code': '400',
                                      'msg': 'Msg failed, please try again'}), 400)
    return jsonify("msg send", msg_to_send)
