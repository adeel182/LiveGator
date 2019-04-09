from flask import Flask, Blueprint, request, flash, url_for, redirect, render_template
from flask_login import login_user, logout_user, current_user , login_required
from werkzeug.security import check_password_hash, generate_password_hash



about_page_endpoints = Blueprint('about_page_endpoints', __name__)


@about_page_endpoints.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@about_page_endpoints.route('/about/AmarisAboutMe', methods=['GET', 'POST'])
def aboutAmarisAboutMe():
    return render_template('about_AmarisAboutMe.html')


@about_page_endpoints.route('/about/kim', methods=['GET', 'POST'])
def aboutKim():
    return render_template('about_Kim.html')


@about_page_endpoints.route('/about/sushil', methods=['GET', 'POST'])
def aboutSushil():
    return render_template('about_sushil.html')


@about_page_endpoints.route('/about/Kurtis', methods=['GET', 'POST'])
def aboutKurtis():
    return render_template('about_Kurtis.html')


@about_page_endpoints.route('/about/Adeel', methods=['GET', 'POST'])
def aboutAdeel():
    return render_template('about_Adeel.html')


@about_page_endpoints.route('/about/simon', methods=['GET', 'POST'])
def aboutSimon():
    return render_template('about_simon.html')


@about_page_endpoints.route('/about/brian', methods=['GET', 'POST'])
def aboutBrian():
    return render_template('about_brian.html')