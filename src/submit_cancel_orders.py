# module to include different types of orders that can be submitted
# The API key can be found at lower right corner in the API section of the RIT client
import requests

host_url = 'http://localhost:9999'          # Make sure the RIT client uses the same 9999 port
base_path = '/v1'
base_url = host_url + base_path

# to print error messages and stop the program when needed
class ApiException(Exception):
    pass

'''
A requests.Session() object must be passed as the ses argument for each order type function
The requests.Session() object should deal with registering the API_KEY in the main function
'''

# submitting a market order
# side = BUY/SELL
def market_order( ses, ticker, side, quantity, API_KEY_entry ):
    ses.headers.update(API_KEY)
    mkt_order_params = { 'ticker':ticker, 'type':'MARKET', 'quantity':quantity, 'action':side}
    response = ses.post( base_url+'/orders', params=mkt_order_params)
    if response.ok:
        mkt_order = response.json()
        id = mkt_order['order_id']
        print('%s %s Market order was submitted and has ID %d' % (side, quantity, id) )
    else:
        print('%s %s Market order was not submitted.' % (side, quantity))

def limit_order( ses, ticker, side, quantity, price, API_KEY_entry ):
    ses.headers.update(API_KEY)
    lim_order_params = { 'ticker':ticker, 'type':'LIMIT', 'quantity':quantity, 'price':price, 'action':side}
    response = ses.post( base_url+'/orders', params=lim_order_params)
    if response.ok:
        lim_order = response.json()
        id = lim_order['order_id']
        print("%s %s Limit order was submitted and has ID %d " % (side, quantity, id) )
    else:
        print('%s %s Limit order was not submitted.' % (side, quantity))

def cancel_order( ses, ticker, quantity, order_id, API_KEY_entry ):
    ses.header.update(API_KEY)
    response = ses.delete( base_url+'/orders/{}'.format(order_id))
    if response.ok:
        status = response.json()
        success = status['success']
        print('Order '+order_id+' was successfully cancelled', success )
    else:
        print('Error in cancelling order %d' % (order_id))

# if all_flag = 1 then all open orders are cancelled
# set all_flag = 0 to cancel only select orders
# price_direc and volume_direc has a value of [ <, <=, >, >= or = ]
def cancel_order_bulk( ses, all_flag, API_KEY_entry, price_direc, price_lim, volume_direc, volume_lim ):
    ses.headers.update(API_KEY)
    # Volume < 0 for cancelling all open sell orders and Volume > 0for cancelling all open buy orders
    query_gen = 'Price' + price_direc + price_lim +'AND'+'Volume' + volume_direc + volume_lim
    cancel_params = {'all': all_flag, 'query': query_gen }
    response = ses.post( base_url+'/commands/cancel',
    params=cancel_params)
    if response.ok:
        status = response.json()
        cancelled = status['cancelled_order_ids']
        print('Cancelled orders:', cancelled)