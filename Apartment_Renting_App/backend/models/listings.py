from ..db import DButils


def get_all_listings():
    return DButils.get_all_listings()


def get_listings_by_userid(user_id):
    return DButils.get_listings_by_userid(user_id)


def get_listing_by_houseid(house_id):
    return DButils.get_listing_by_houseid(house_id)


def create_new_listing(user_id, house_name, price, size, distance, number, street, city, state, zipcode, image_url):
    DButils.create_new_listing(user_id, house_name, price, size, distance, number, street, city, state, zipcode, image_url)


def delete_listing(house_id):
    DButils.delete_listing(house_id)