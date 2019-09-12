####################################
# File name: message.py            #
# Description:
# Author: Team-13                  #
# Submission: Spring-2019          #
# Instructor: Dragutin Petkovic    #
####################################
from ..db import DButils

def get_msg_by_customerid(customer_id):
    all_msg = DButils.get_all_msg_by_id("customer_id", customer_id)
    # renter_id_set = set()
    # for msg in all_msg:
    #     renter_id_set.add(msg[0])
    # renter_username = []
    # for renter_id in renter_id_set:
    #     renter = DButils.get_user("user_id", renter_id)
    #     renter_username.append(renter[1])
    return all_msg


def get_msg_by_renterid(landlord_id):
    all_msg = DButils.get_all_msg_by_id("landlord_id", landlord_id)
    # customer_id_set = set()
    # for msg in all_msg:
    #     customer_id_set.add(msg[1])
    # customer_username = []
    # for landlord_id in customer_id_set:
    #     renter = DButils.get_user("user_id", landlord_id)
    #     customer_username.append(renter[1])
    return all_msg

''' Below are the old messaging system. Discarded on April 30 by Kim
# def get_msg_by_customerid(customer_id):
#     all_msg = DButils.get_all_msg_by_id("customer_id", customer_id)
#     renter_id_set = set()
#     for msg in all_msg:
#         renter_id_set.add(msg[0])
#     renter_username = []
#     for renter_id in renter_id_set:
#         renter = DButils.get_user("user_id", renter_id)
#         renter_username.append(renter[1])
#     return renter_username
# 
# 
# def get_msg_by_renterid(landlord_id):
#     all_msg = DButils.get_all_msg_by_id("landlord_id", landlord_id)
#     customer_id_set = set()
#     for msg in all_msg:
#         customer_id_set.add(msg[1])
#     customer_username = []
#     for landlord_id in customer_id_set:
#         renter = DButils.get_user("user_id", landlord_id)
#         customer_username.append(renter[1])
#     return customer_username
'''

def get_msg_detail(renter_id, customer_id):
    return DButils.get_msg_detail(renter_id, customer_id)



def send_msg(renter_id, customer_id, house_id, sender, msg):
    DButils.send_msg(renter_id, customer_id, house_id, sender, msg)

#
#
# def send_msg_from_dashboard()