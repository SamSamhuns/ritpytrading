'''
order return object attributes
param possible order attributes: JSON formatted
i.e. get_order_response( ses, url_end, param="order_id" )
{
    "order_id": 1221,
    "period": 1,
    "tick": 10,
    "trader_id": "trader49",
    "ticker": "CRZY",
    "type": "LIMIT",
    "quantity": 100,
    "action": "BUY",
    "price": 14.21,
    "quantity_filled": 10,
    "vwap": 14.21,
    "status": "OPEN"
}
'''

import requests

# Make sure the RIT client uses the same 9999 port
host_url = 'http://localhost:9999'
base_path = '/v1'
base_url = host_url + base_path

# to print error messages and stop the program when needed


class ApiException(Exception):
    pass


class Order():
    def __init__(self, order_response):
        self.order_id = zz["order_id"]
        self.period = zz["period"]
        self.tick = zz["tick"]
        self.trader_id = zz["trader_id"]
        self.ticker = zz["ticker"]
        self.type = zz["type"]
        self.quantity = zz["quantity"]
        self.action = zz["action"]
        self.price = zz["price"]
        self.quantity_filled = ["quantity_filled"]
        self.vwap = ["vwap"]
        self.status = ["status"]

    def __repr__(self)
    return self.action + '_' + self.quantity + '_' + self.ticker + '_' + self.price + '__' + self.order_id


# function requires a requests.Session() object as the ses argument with a loaded API_KEY
# order status can be OPEN, TRANSACTED or CANCELLED
# Json return mode is set to 0/Off by default

def get_order_response(ses, url_end, order_status='OPEN', order_id=None, json=0):
    # to query all orders
    if url_end == '/orders':
        payload = {'status': order_status}
        response = ses.get((base_url + url_end), params=payload)
    # to query just one order
    elif url_end == '/orders/{}':
        response = ses.get((base_url + url_end).format(order_id))

    if response.ok:
        orders = response.json()
        # if the json flag is set to 1, return orders json output unformatted
        if json == 1:
            return orders

        if url_end == '/orders/{}':
            orders_obj = Order(orders)
            return orders_obj

        if url_end == '/orders':
            orders_dict = {(Order(ord)).order_id: Order(ord)
                           for ord in orders}
            return orders_list
    raise ApiException('Authorization Error: Please check API key.')


# status can be OPEN, TRANSACTED or CLOSED
# status OPEN by default
# returns a Order object of the order class given an order id

def order(ses, id, status='OPEN'):
    return get_order_response(ses, '/orders/{}', status, order_id=id)

# returns all the attribs of all orders in a json type list format


def orders_json(ses, status='OPEN'):
    return get_order_response(ses, '/orders', status, order_id=None, json=1)


# returns all the orders as a dict with the order_ids as key

def orders_dict(ses, status='OPEN'):
    return get_order_response(ses, '/orders', status, order_id=None)
