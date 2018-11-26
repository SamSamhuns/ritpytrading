import requests

# Make sure the RIT client uses the same 9999 port
host_url = 'http://localhost:9999'
base_path = '/v1'
base_url = host_url + base_path

# to print error messages and stop the program when needed


class ApiException(Exception):
    pass

# function requires a requests.Session() object as the ses argument with a loaded API_KEY
# order status can be OPEN, TRANSACTED or CANCELLED


def get_order_response(ses, url_end, param, order_status='OPEN', order_id=None, all=0):
    # to query all orders
    if url_end == '/orders':
        order_params = {'status': order_status}
        response = ses.get((base_url + url_end), params=order_params)
    # to query just one order
    elif url_end == '/orders/{}':
        response = ses.get((base_url + url_end).format(order_id))

    if response.ok:
        orders = response.json()
        if all == 1:
            return orders               # returns a json obj with all order info
        if url_end == '/orders/{}':
            return orders[param]
        elif url_end == '/orders':
            orders_list = []
            for ord in orders:
                order_dict = {}
                order_dict['order_id'] = orders['order_id']
                order_dict[param] = orders[param]
                orders_list.append(order_dict)
            return orders_list
    raise ApiException('Authorization Error: Please check API key.')


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
# status can be OPEN, TRANSACTED or CLOSED
# status OPEN by default
# returns one attribute of an order with entered id or of all orders


def get_order_attribute(ses, param, id=None, status='OPEN'):
    if id == None:
        return get_order_response(ses, '/orders', param, status)
    elif id != None:
        return get_order_response(ses, '/orders/{}', param, order_id=id, status)

# returns all the attribs of all orders in a json format


def get_all_orders(ses, status='OPEN'):
    return get_order_response(ses, '/orders', None, status, None, all=1)
