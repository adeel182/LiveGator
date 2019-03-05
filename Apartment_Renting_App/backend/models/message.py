from ..db import DButils


def get_msg_by_customerid(customer_id):
    return DButils.get_msg_by_customerid(customer_id)


def get_msg_by_renterid(renter_id):
    return DButils.get_msg_by_renterid(renter_id)

def send_msg(house_id, renter_id, customer_id):
    DButils.send_msg(house_id, renter_id, customer_id)

