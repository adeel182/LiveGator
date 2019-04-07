from ..db import DButils


def get_orders_by_customerid(customer_id):
    return DButils.get_orders_by_id("customer_id", customer_id)


def get_orders_by_renterid(landlord_id):
    return DButils.get_orders_by_id("landlord_id", landlord_id)


def place_order(house_id, landlord_id, customer_id):
    DButils.place_order(house_id, landlord_id, customer_id)

