from ..db import DButils


def get_orders_by_customerid(customer_id):
    return DButils.get_orders_by_id("customer_id", customer_id)


def get_orders_by_renterid(renter_id):
    return DButils.get_orders_by_id("renter_id", renter_id)


def place_order(house_id, renter_id, customer_id):
    DButils.place_order(house_id, renter_id, customer_id)

