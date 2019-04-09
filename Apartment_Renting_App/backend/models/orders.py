from ..db import DButils


def get_orders_by_customerid(customer_id):
    return DButils.get_orders_by_id("customer_id", customer_id)


def get_orders_by_renterid(landlord_id):
    return DButils.get_orders_by_id("landlord_id", landlord_id)


def get_request_by_customerid(customer_id):
    return DButils.get_request_by_id("customer_id", customer_id)


def get_request_by_renterid(landlord_id):
    return DButils.get_request_by_id("landlord_id", landlord_id)

def get_request_by_houseid(house_id):
    return DButils.get_request_by_id("house_id", house_id)


def add_renting_request(house_id, landlord_id, customer_id):
    DButils.add_renting_request(house_id, landlord_id, customer_id)


def delete_renting_request(house_id):
    DButils.delete_renting_request(house_id)


def place_order(house_id, landlord_id, customer_id):
    DButils.place_order(house_id, landlord_id, customer_id)

