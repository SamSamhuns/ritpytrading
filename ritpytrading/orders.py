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


# Make sure the RIT client uses the same 9999 port
host_url = 'http://localhost:9999'
base_path = '/v1'
base_url = host_url + base_path

# to print error messages and stop the program when needed


class ApiException(Exception):
    pass


class Order():
    # order_response is a json obj returned from the API get request
    def __init__(self, order_response):
        self.order_id = order_response["order_id"]
        self.period = order_response["period"]
        self.tick = order_response["tick"]
        self.trader_id = order_response["trader_id"]
        self.ticker = order_response["ticker"]
        self.type = order_response["type"]
        self.quantity = order_response["quantity"]
        self.action = order_response["action"]
        self.price = order_response["price"]
        self.quantity_filled = order_response["quantity_filled"]
        self.vwap = order_response["vwap"]
        self.status = order_response["status"]

    def __repr__(self):
        return (self.action + '_' + self.quantity + '_'
                + self.ticker + '_' + self.price + '__' + self.order_id)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

# function requires a requests.Session() object
# as the ses argument with a loaded API_KEY
# order status can be OPEN, TRANSACTED or CANCELLED
# Json return mode is set to 0/Off by default


def _get_orders_json(ses, url_end, order_status='OPEN', order_id=None):
    # to query all orders
    if url_end == '/orders':
        payload = {'status': order_status}
        response = ses.get((base_url + url_end), params=payload)
    # to query just one order
    elif url_end == '/orders/{}':
        response = ses.get((base_url + url_end).format(order_id))

    if response.ok:
        orders_json = response.json()
        # Return orders json output unformatted
        return orders_json
    raise ApiException('Authorization Error: Please check API key.')


def orders_response_handle(orders_json, url_end):
    if url_end == '/orders/{}':
        orders_obj = Order(orders_json)
        return orders_obj

    if url_end == '/orders':
        orders_dict = {(Order(ord)).order_id: Order(ord)
                       for ord in orders_json}
        return orders_dict


# status can be OPEN, TRANSACTED or CLOSED
# status OPEN by default
# returns a Order object of the order class given an order id
def order(ses, orderId, status='OPEN'):
    return orders_response_handle(_get_orders_json(
        ses, '/orders/{}', status, order_id=orderId), '/orders/{}')

# returns all the attribs of all orders in a json type list format


def orders_json(ses, status='OPEN'):
    return _get_orders_json(ses, '/orders', status, order_id=None)

# returns all the orders as a dict with the order_ids as key


def orders_dict(ses, status='OPEN'):
    return orders_response_handle(_get_orders_json(
        ses, '/orders', status, order_id=None), '/orders')
