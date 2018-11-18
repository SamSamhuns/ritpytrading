# module to include different types of orders that can be submitted
# The API key can be found at lower right corner in the API section of the RIT client
import requests
host_url = 'http://localhost:9999'          # Make sure the RIT client uses the same 9999 port
base_path = '/v1'


def market_order( ticker, side, quantity, API_KEY_entry ):
    API_KEY = { 'X-API-key': API_KEY_entry }
    with requests.Session() as ses:
        ses.headers.update(API_KEY)
        mkt_order_params = { 'ticker':ticker, 'type':'MARKET', 'quantity':quantity, 'action':side}
        response = ses.post( host_url+base_path+'/orders', params=mkt_order_params)
        if response.ok:
            mkt_order = response.json()
            id = mkt_order['order_id']
            print('%s %s Market order was submitted and has ID %d' % (side, quantity, id) )
        else:
            print('%s %s Market order was not submitted.' % (side, quantity))

def limit_order( ticker, side, quantity, price, API_KEY_entry ):
    API_KEY = { 'X-API-key': API_KEY_entry }
    with requests.Session() as ses:
        ses.headers.update(API_KEY)
        lim_order_params = { 'ticker':ticker, 'type':'LIMIT', 'quantity':quantity, 'price':price, 'action':side}
        response = ses.post( host_url+base_path+'/orders', params=lim_order_params)
        if response.ok:
            lim_order = response.json()
            id = lim_order['order_id']
            print("%s %s Limit order was submitted and has ID %d " % (side, quantity, id) )
        else:
            print('%s %s Limit order was not submitted.' % (side, quantity))

def cancel_order( ticker, quantity, order_id, API_KEY_entry ):
    API_KEY = { 'X-API-key': API_KEY_entry }
    with requests.Session() as ses:
        s.header.update(API_KEY)
        response = ses.delete( host_url+base_path+'/orders/{}'.format(order_id))
        if response.ok:
            status = response.json()
            success = status['success']
            print('Order '+order_id+' was successfully cancelled', success )
        else:
            print('Error in cancelling order %d' % (order_id))

def cancel_order_bulk( API_KEY_entry, side, price_lim, volume_lim ):
    cancel_direction = ''
    if side.upper().strip() = 'SELL':
        cancel_direction = '<'
    elif side.upper().strip() = 'BUY':
        cancel_direction - '>'
    with requests.Session() as ses:
        ses.headers.update(API_KEY_entry )
        cancel_params = {'all': 0, 'query': 'Price>20.10 AND Volume<0'} # cancel all open sell orders with a price over 20.10
        response = ses.post( host_url+base_path+'/commands/cancel',
        params=cancel_params)
        if response.ok:
            status = response.json()
            cancelled = status['cancelled_order_ids']
            print('Cancelled orders:', cancelled)
