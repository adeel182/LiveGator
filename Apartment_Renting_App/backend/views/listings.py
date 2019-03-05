from flask import Flask, Blueprint, request, flash, url_for, redirect, render_template, jsonify, g
from flask_login import login_user, logout_user, current_user , login_required, LoginManager
from werkzeug.security import check_password_hash, generate_password_hash

from ..models import listings
from ..models.user import User

listing_endpoints = Blueprint('listing_endpoints', __name__)


@listing_endpoints.route('/all_listings', methods=['GET'])
def display_all_listings():
    return jsonify(listings.get_all_listings())


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

