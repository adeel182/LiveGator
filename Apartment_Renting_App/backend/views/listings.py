from flask import Flask, Blueprint, abort, request, flash, url_for, redirect, render_template, jsonify, g
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
    listing_type = request.args.get("type", "")
    sort = request.args.get("sort", 0)
    #0: date latest first
    #1: price low to high    2: price high to low
    #3: size low to high    4: size high to low
    #5: distance low to high    6: distance high to low
    search_key = request.args.get("search_key", "")
    data = listings.get_all_listings(price_low, price_high, size_low, size_high, distance_low, distance_high, listing_type, sort, search_key)
    # print(data)
    result = []
    for d in data:
        js = {"house_id": d[0], "landlord_id": d[1], "house_name": d[2], "type": d[3], "description": d[4], "price": d[5],
            "size": d[6], "distance": d[7], "number": d[8], "street": d[9], "city": d[10], "state": d[11], "zipcode": d[12],
            'image_url': d[13], "bedroom_count": d[14], "bathroom_count": d[15], "parking_count": d[16], "is_available:": d[17],
            "create_date": d[18], "approved": d[19]}
        result.append(js)
    # print(result)
    return result


@listing_endpoints.route('/all_listings/<house_id>', methods=['GET'])
def display_a_house(house_id):
    data = listings.get_listing_by_houseid(house_id)
    result = []

    # print(data)
    for d in data:
    #     print(d[6])
        result = {"house_id": d[0], "landlord_id": str(d[1]), "house_name": d[2], "type": d[3], "description": d[4], "price": d[5],
            "size": d[6], "distance": d[7], "number": d[8], "street": d[9], "city": d[10], "state": d[11], "zipcode": d[12],
            'image_url': d[13], "bedroom_count": d[14], "bathroom_count": d[15], "parking_count": d[16], "is_available": d[17],
            "create_date": d[18], "approved": d[19]}
    return render_template("home_search_single_listing.html", data = result)



@listing_endpoints.route('/renter_dashboard/view_listings', methods=['GET'])
@login_required
def get_listings_by_userid():
    # print(current_user.user_id)
    sort = request.args.get("sort", 0)
    # 0: date latest first
    # 1: price low to high    2: price high to low
    # 3: size low to high    4: size high to low
    # 5: distance low to high    6: distance high to low
    data = listings.get_listings_by_userid(current_user.user_id, sort)
    result = []
    for d in data:
        js = {
            "house_id": d[0], "landlord_id": d[1], "house_name": d[2], "type": d[3], "description": d[4], "price": d[5],
            "size": d[6], "distance": d[7], "number": d[8], "street": d[9], "city": d[10], "state": d[11], "zipcode": d[12],
            'image_url': d[13], "bedroom_count": d[14], "bathroom_count": d[15], "parking_count": d[16], "is_available:": d[17],
            "create_date": d[18], "approved": d[19]}
        result.append(js)
    # print(result)
    return render_template("renter_listings.html", data = result)



@listing_endpoints.route('/renter_dashboard/add_a_new_listing', methods=['GET', 'POST'])
@login_required
def add_a_new_listing():
    if request.method == 'GET':
        return render_template("renter_add_a_new_listing.html")
    try:
        user_id = current_user.user_id
        house_name = request.form.get("house_name", "N/A")
        type = request.form.get("type", "N/A")
        description = request.form.get("description", "N/A")
        price = request.form.get("price", "N/A")
        size = request.form.get("size", "N/A")
        distance = request.form.get("distance", "N/A")
        number = request.form.get("number", "N/A")
        street = request.form.get("street", "N/A")
        city = request.form.get("city", "N/A")
        state = request.form.get("state", "N/A")
        zipcode = request.form.get("zipcode", "N/A")
        image_url = request.form.get("image_url", "N/A")
        bedroom_count = request.form.get("bedroom_count", "N/A")
        bathroom_count = request.form.get("bathroom_count", "N/A")
        parking_count = request.form.get("parking_count", "N/A")
        listings.add_a_new_listing(user_id, house_name, type, description, price, size, distance, number, street, city, state, zipcode, image_url, bedroom_count, bathroom_count, parking_count)
        return redirect('/renter_dashboard/view_listings')
    except:
        return abort(400)


@listing_endpoints.route('/renter_dashboard/delete', methods=['POST'])
@login_required
def delete_a_listing():
    house_id = request.form["house_id"]
    listings.delete_listing(house_id)
    return redirect('renter_dashboard/view_listings')