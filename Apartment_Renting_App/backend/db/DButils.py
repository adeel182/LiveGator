from ..db.connection import conn, cursor

#user
def get_user(role, parameter):
    conn.connect()
    cur = conn.cursor()
    sql_str = "SELECT * from USER WHERE {} = %s".format(role)
    cursor.execute(sql_str, (parameter, ))
    data = cursor.fetchone()
    cur.close()
    conn.close()
    return data

def login(username):
    conn.connect()
    cur = conn.cursor()
    sql_str = "SELECT * from USER WHERE username = %s"
    cursor.execute(sql_str, (username, ))
    data = cursor.fetchone()
    # cursor.close()
    conn.close()
    return data

def signup(username, password, email, isStudent):
    conn.connect()
    cur = conn.cursor()
    sql_str = "INSERT INTO USER (username,password,email,isStudent) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql_str, (username, password, email, isStudent))
    conn.commit()
    cur.close()
    conn.close()

#listing
def get_all_listings(price_low, price_high, size_low, size_high, distance_low, distance_high, listing_type, key):
    conn.connect()
    cur = conn.cursor()
    sql_str = "SELECT * from LISTINGS WHERE isAvailable = TRUE AND approved = TRUE"
    if price_low is not "":
        sql_str = sql_str + " AND price >= {}".format(price_low)
    if price_high is not "":
        sql_str = sql_str + " AND price <= {}".format(price_high)
    if size_low is not "":
        sql_str = sql_str + " AND size >= {}".format(size_low)
    if size_high is not "":
        sql_str = sql_str + " AND size <= {}".format(size_high)
    if distance_low is not "":
        sql_str = sql_str + " AND distance >= {}".format(distance_low)
    if distance_high is not "":
        sql_str = sql_str + " AND distance <= {}".format(distance_high)
    if listing_type is not "":
        sql_str = sql_str + " AND type = '{}'".format(listing_type)
    if key is not "":
        sql_str = sql_str + " AND house_name LIKE '%{}%'".format(key) + " OR type LIKE '%{}%'".format(
            key) + " OR description LIKE '%{}%'".format(key) + " OR street LIKE '%{}%'".format(
            key) + " OR city LIKE '%{}%'".format(key) + " OR zipcode LIKE '%{}%'".format(key)
    sql_str = sql_str + " ORDER BY create_date"
    # print(sql_str)
    cursor.execute(sql_str)
    data = cursor.fetchall()
    cur.close()
    conn.close()
    return data


def get_listings_by_userid(user_id):
    conn.connect()
    cur = conn.cursor()
    sql_str = "SELECT * from LISTINGS WHERE landlord_id = %s ORDER BY create_date"
    cursor.execute(sql_str, (user_id, ))
    data = cursor.fetchall()
    cur.close()
    conn.close()
    return data

def get_listing_by_houseid(house_id):
    conn.connect()
    cur = conn.cursor()
    sql_str = "SELECT * from LISTINGS WHERE house_id = %s ORDER BY create_date"
    cursor.execute(sql_str, (house_id, ))
    data = cursor.fetchall()
    cur.close()
    conn.close()
    return data

def create_new_listing(user_id, house_name, type, description, price, size, distance, number, street, city, state, zipcode, image_url, bedroom_count, bathroom_count, parking_count):
    conn.connect()
    cur = conn.cursor()
    sql_str = "INSERT INTO LISTINGS (landlord_id, house_name, type, description, price, size, distance, number, street, city, state, zipcode, image_url, bedroom_count, bathroom_count, parking_count, create_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, now())"
    cursor.execute(sql_str, (user_id, house_name, type, description, price, size, distance, number, street, city, state, zipcode, image_url, bedroom_count, bathroom_count, parking_count))
    conn.commit()
    cur.close()
    conn.close()

def delete_listing(house_id):
    conn.connect()
    cur = conn.cursor()
    sql_str = "DELETE from LISTINGS WHERE house_id = %s"
    cursor.execute(sql_str, (house_id, ))
    conn.commit()
    cur.close()
    conn.close()


#order
def add_renting_request(house_id, renter_id, customer_id):
    conn.connect()
    cur = conn.cursor()
    try:
        sql_str_order = "INSERT INTO PENDING_REQUEST (house_id, landlord_id, customer_id, create_date) VALUES (%s, %s, %s, NOW())"
        cursor.execute(sql_str_order, (house_id, renter_id, customer_id))
        sql_str_listings = "UPDATE LISTINGS SET isAvailable = %s WHERE house_id = %s"
        cursor.execute(sql_str_listings, (0, house_id))
        conn.commit()
    except:
        conn.rollback()
    cur.close()
    conn.close()


def delete_renting_request(house_id):
    conn.connect()
    cur = conn.cursor()
    try:
        sql_str_order = "UPDATE PENDING_REQUEST SET status = 2 WHERE house_id = %s"
        cursor.execute(sql_str_order, (house_id, ))
        sql_str_listings = "UPDATE LISTINGS SET isAvailable = %s WHERE house_id = %s"
        cursor.execute(sql_str_listings, (1, house_id))
        conn.commit()
    except:
        conn.rollback()
    cur.close()
    conn.close()


def get_orders_by_id(role, user_id):
    conn.connect()
    cur = conn.cursor()
    sql_str = "SELECT * from ORDERS WHERE {} = %s ORDER BY create_date".format(role)
    # print(sql_str, (user_id, ))
    cursor.execute(sql_str, (user_id, ))
    data = cursor.fetchall()
    cur.close()
    conn.close()
    return data


def get_request_by_id(role, user_id):
    conn.connect()
    cur = conn.cursor()
    sql_str = "SELECT * from PENDING_REQUEST WHERE {} = %s ORDER BY create_date".format(role)
    cursor.execute(sql_str, (user_id, ))
    data = cursor.fetchall()
    cur.close()
    conn.close()
    return data

# def get_orders_by_customerid(user_id):
#     sql_str = "SELECT * from ORDERS WHERE customer_id = %s ORDER BY create_date"
#     cursor.execute(sql_str, (user_id, ))
#     return cursor.fetchall()


def place_order(house_id, renter_id, customer_id):
    conn.connect()
    cur = conn.cursor()
    try:
        sql_str_order = "INSERT INTO ORDERS (house_id, landlord_id, customer_id, create_date) VALUES (%s, %s, %s, NOW())"
        cursor.execute(sql_str_order, (house_id, renter_id, customer_id))
        sql_str_listings = "UPDATE PENDING_REQUEST SET status = 1 WHERE house_id = %s"
        cursor.execute(sql_str_listings, (house_id, ))
        conn.commit()
    except:
        conn.rollback()
    cur.close()
    conn.close()

#message

def get_all_msg_by_id(role, user_id):
    conn.connect()
    cur = conn.cursor()
    sql_str = "SELECT * from MESSAGE WHERE {} = %s ORDER BY date".format(role)
    # print(sql_str, (user_id, ))
    cursor.execute(sql_str, (user_id,))
    data = cursor.fetchall()
    cur.close()
    conn.close()
    return data

def get_msg_detail(renter_id, customer_id):
    conn.connect()
    cur = conn.cursor()
    sql_str = "SELECT * from MESSAGE WHERE landlord_id = %s AND customer_id = %s ORDER BY date"
    cursor.execute(sql_str, (renter_id, customer_id))
    data = cursor.fetchall()
    cur.close()
    conn.close()
    return data

def send_msg(renter_id, customer_id, sender, msg):
    conn.connect()
    cur = conn.cursor()
    sql_str = "INSERT INTO MESSAGE (landlord_id, customer_id, sender, message, date) VALUES (%s, %s, %s, %s, NOW())"
    cursor.execute(sql_str, (renter_id, customer_id, sender, msg))
    conn.commit()


#admin
def approve_new_listing(house_id):
    conn.connect()
    cur = conn.cursor()
    sql_str = "UPDATE LISTINGS SET approved = 1 WHERE house_id = %s"
    cursor.execute(sql_str, (house_id, ))
    conn.commit()
    cur.close()
    conn.close()


def block_user(user_id):
    conn.connect()
    cur = conn.cursor()
    sql_str = "UPDATE USER SET isBanned = 1 WHERE user_id = %s"
    cursor.execute(sql_str, (user_id,))
    conn.commit()
    cur.close()
    conn.close()


def get_all_to_approve():
    conn.connect()
    cur = conn.cursor()
    sql_str = "SELECT * from LISTINGS WHERE approved = false ORDER BY create_date"
    cursor.execute(sql_str,)
    conn.commit()
    cur.close()
    conn.close()