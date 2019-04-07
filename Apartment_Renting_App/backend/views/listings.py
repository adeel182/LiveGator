from flask import Flask, Blueprint, request, flash, url_for, redirect, render_template, jsonify, g
from flask_login import login_user, logout_user, current_user , login_required, LoginManager
from werkzeug.security import check_password_hash, generate_password_hash

from ..models import listings
from ..models.user import User

listing_endpoints = Blueprint('listing_endpoints', __name__)


@listing_endpoints.route('/all_listings', methods=['GET'])
#1. sort by price, by size, by distance, by listing date
#2. filter by price, size, distance
def display_all_listings():
    price_low = request.args.get("price_low", "")
    price_high = request.args.get("price_high", "")
    size_low = request.args.get("size_low", "")
    size_high = request.args.get("size_high", "")
    distance_low = request.args.get("distance_low", "")
    distance_high = request.args.get("distance_high", "")
    sort = request.args.get("sort", 0)
    #0: date latest first
    #1: price low to high    2: price high to low
    #3: size low to high    4: size high to low
    #5: distance low to high    6: distance high to low
    search_key = request.args.get("search_key", "")
    data = listings.get_all_listings(price_low, price_high, size_low, size_high, distance_low, distance_high, sort, search_key)
    # print(data)
    result = []
    for d in data:
        js = {
            "house_id" : d[0],"landlord_id" : d[1], "house_name" : d[2], "type" : d[3], "description" : d[4], "price": d[5], "size" : d[6],
            "distance" : d[7], "number" : d[8], "street" : d[9], "city" : d[10], "state" : d[11], "zipcode" : d[12],
            'image_url' : d[13], "bedroom_count" : d[14], "bathroom_count" : d[15], "parking_count" : d[16], "create_date" : d[17]}
        result.append(js)
    # print(result)
    return result


@listing_endpoints.route('/all_listings/<house_id>', methods=['GET'])
def display_a_house(house_id):
    return jsonify(listings.get_listing_by_houseid(house_id))


# @listing_endpoints.before_request
# def load_users():
#    g.user_id = current_user.user_id


@listing_endpoints.route('/renter_dashboard/view_listings', methods=['GET'])
@login_required
def get_listings_by_userid():
    print(current_user.user_id)
    return jsonify(listings.get_listings_by_userid(current_user.user_id))

