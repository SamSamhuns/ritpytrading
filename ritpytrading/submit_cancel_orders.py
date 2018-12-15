# module to include different types of orders that can be submitted
# The API key can be found at lower right corner
# in the API section of the RIT client


# Make sure the RIT client uses the same 9999 port
host_url = 'http://localhost:9999'
base_path = '/v1'
base_url = host_url + base_path

# to print error messages and stop the program when needed


class ApiException(Exception):
    pass


'''
A requests.Session() object must be passed as the ses argument for each order
type function. The requests.Session() object should deal with registering
the API_KEY in the main function
'''

# submitting a market order
# side = BUY/SELL
# function requires a requests.Session() object as
# the ses argument with a loaded API_KEY


def market_order(ses, ticker, side, quantity):
    mkt_order_params = {'ticker': ticker, 'type': 'MARKET',
                        'quantity': quantity, 'action': side}
    response = ses.post(base_url + '/orders', params=mkt_order_params)
    if response.ok:
        mkt_order = response.json()
        orderId = mkt_order['order_id']
        print('%s %s Market order was submitted and has ID %d' %
              (side, quantity, orderId))
    if response.status_code == 429:
        print('Error: Orders submitted too frequently.')
    else:
        raise ApiException('Authorization Error: Please check API key.')

# function requires a requests.Session() object as the
# ses argument with a loaded API_KEY


def limit_order(ses, ticker, side, quantity, price):
    lim_order_params = {'ticker': ticker, 'type': 'LIMIT',
                        'quantity': quantity, 'price': price, 'action': side}
    response = ses.post(base_url + '/orders', params=lim_order_params)
    if response.ok:
        lim_order = response.json()
        orderId = lim_order['order_id']
        print("%s %s Limit order was submitted and has ID %d " %
              (side, quantity, orderId))
    elif response.status_code == 429:
        print('Error: Orders submitted too frequently.')
    else:
        raise ApiException('Authorization Error: Please check API key.')

# function requires a requests.Session() object as the
# ses argument with a loaded API_KEY


def cancel_order(ses, ticker, quantity, order_id):
    response = ses.delete((base_url + '/orders/{}').format(order_id))
    if response.ok:
        status = response.json()
        success = status['success']
        if success:
            print('Order ' + order_id + ' was successfully cancelled.')
        else:
            print('Order ' + order_id + ' was not successfully cancelled.')
    else:
        raise ApiException('Authorization Error: Please check API key.')


# if all_flag = 1 then all open orders are cancelled
# set all_flag = 0 to cancel only select orders
# By default all_flag is set to 0
# price_direc and volume_direc has a value of [ <, <=, >, >= or = ]


def cancel_order_bulk(
        ses, price_direc, price_lim, volume_direc, volume_lim, all_flag=0):
    # Volume < 0 for cancelling all open sell orders and Volume > 0
    # for cancelling all open buy orders
    # query_gen example 'Price < 20.0 AND Volume > 0'
    query_gen = 'Price ' + price_direc + ' ' + price_lim + \
        ' AND ' + ' Volume ' + ' ' + volume_direc + ' ' + volume_lim
    cancel_params = {'all': all_flag, 'query': query_gen}
    response = ses.post(base_url + '/commands/cancel', params=cancel_params)
    if response.ok:
        status = response.json()
        cancelled = status['cancelled_order_ids']
        print('Cancelled orders:', cancelled)
    else:
        raise ApiException('Authorization Error: Please check API key.')
