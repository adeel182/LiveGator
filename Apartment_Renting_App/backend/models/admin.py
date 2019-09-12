####################################
# File name: admin.py              #
# Description:
# Author: Team-13                  #
# Submission: Spring-2019          #
# Instructor: Dragutin Petkovic    #
####################################
from ..db import DButils


def approve_new_listing(house_id):
    DButils.approve_new_listing(house_id)


def block_user(user_id):
    DButils.block_user(user_id)


def get_all_to_approve():
    return DButils.get_all_to_approve()