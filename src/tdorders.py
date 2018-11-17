# module to include different types of orders that can be submitted
import requests

def market_order ( ticker, side, quantity, API_KEY_entry ):
    API_KEY = { 'X-API-key': API_KEY_entry }
    with requests.Session() as ses:
        ses.headers.update(API_KEY)
        mkt_order_params = { 'ticker':ticker, 'type':'MARKET', 'quantity':quantity, 'action':side}
        response = ses.post('http://localhost:9999/v1/orders', params=mkt_order_params)
        if response.ok:
            mkt_order = response.json()
            id = mkt_order['order_id']
            print('%s %s Market order was submitted and has ID %d' % (side, quantity, id) )
        else:
            print('%s %s Market order was not submitted.' % (side, quantity))

def limit_order( ticker, side, quantity, API_KEY_entry ):
    API_KEY = { 'X-API-key': API_KEY_entry }
    with requests.Session() as ses:
        ses.headers.update(API_KEY)
        lim_order_params = { 'ticker':ticker, 'type':'LIMIT', 'quantity':quantity, 'action':side}
        response = ses.post('http://localhost:9999/v1/orders', params=lim_order_params)
        if response.ok:
            lim_order = response.json()
            id = lim_order['order_id']
            print("%s %s Limit order was submitted and has ID %d " % (side, quantity, id) )
        else:
            print('%s %s Limit order was not submitted.' % (side, quantity))

def cancel_order( )
