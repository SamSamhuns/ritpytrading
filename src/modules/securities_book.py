'''
functions related to the order book of a security
securities_book object attribute values: JSON formatted
{
  "bid": [
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
  ],
  "ask": [
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
  ]
}
'''

import requests

host_url = 'http://localhost:9999'          # Make sure the RIT client uses the same 9999 port
base_path = '/v1'
base_url = host_url + base_path

# to print error messages and stop the program when needed
class ApiException(Exception):
    pass

# function requires a requests.Session() object as the ses argument with a loaded API_KEY
# returns the best bid or ask on the market based on the side entered
# side = bids/asks
# the all flag set in four tiers
# all = 0   securities_book[side][0][param] return one parameter of best bid/ask
# all = 1   securities_book[side][0]        return all params of best bid/ask
# all = 2   securities_book[side]           return all orders in the bid/ask side
# all = 3   securities_book                 return all orders from both sides

def get_sec_book_response ( ses, ticker_sym, side, param, all=0 ):
    payload = {'ticker': ticker_sym }
    response = ses.get( base_url+'/securities/book', params=payload )
    if response.ok:
        securities_book = response.json()
        if all == 1:
            return securities_book[side][0]
        if all == 2:
            return securities_book[side]
        if all == 3:
            return securities_book
        # this returns only one attrb of the best bid/ask offer i.e. 'quantity'
        return securities_book[side][0][param]
    raise ApiException('Authorization Error: Please check API key.')

# All possible values for the param parameter are listed at the top
def get_security_info ( ses, ticker_sym, side, param ):
    return get_sec_book_response( ses, ticker_sym, side, param )

def get_best_bid ( ses, ticker_sym ):
    return get_sec_book_response( ses, ticker_sym, 'bids', None, all=1 )

def get_best_ask ( ses, ticker_sym ):
    return get_sec_book_response( ses, ticker_sym, 'asks', None, all=1 )

def get_bbo ( ses, ticker_sym ):
    best_bid = get_best_bid ( ses, ticker_sym )
    best_ask = get_best_ask ( ses, ticker_sym )
    return {'best_bid':best_bid, 'best_ask':best_ask}

def get_all_bids ( ses, ticker_sym ):
    return get_sec_book_response( ses, ticker_sym, 'bids', None, all=2 )

def get_all_asks ( ses, ticker_sym ):
    return get_sec_book_response( ses, ticker_sym, 'asks', None, all=2 )

def get_all_bids_asks ( ses, ticker_sym ):
    return get_sec_book_response( ses, ticker_sym, None, None, all=3 )