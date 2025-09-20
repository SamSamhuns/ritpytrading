# The  /securities/book HTTP module gets the order book of a security
#
# securities_book object attribute values: JSON formatted
# {
#   "bids": [
#     {
#       "order_id": 1221,
#       "period": 1,
#       "tick": 10,
#       "trader_id": "trader49",
#       "ticker": "CRZY",
#       "type": "LIMIT",
#       "quantity": 100,
#       "action": "BUY",
#       "price": 14.21,
#       "quantity_filled": 10,
#       "vwap": 14.21,
#       "status": "OPEN"
#     }
#   ],
#   "asks": [
#     {
#       "order_id": 1221,
#       "period": 1,
#       "tick": 10,
#       "trader_id": "trader49",
#       "ticker": "CRZY",
#       "type": "LIMIT",
#       "quantity": 100,
#       "action": "BUY",
#       "price": 14.21,
#       "quantity_filled": 10,
#       "vwap": 14.21,
#       "status": "OPEN"
#     }
#   ]
# }
#
# Parameters for the securities_book GET HTTP request
# - ticker* required string   (query)
# - period number             (query)

from ._response_validation import _validate_response

# Make sure the RIT client uses the same 9999 port
host_url = "http://localhost:9999"
base_path = "/v1"
base_url = host_url + base_path


def _get_sec_book_response(ses, ticker_sym, side, param, all_flag=0):
    """function requires a requests.Session() object
    as the ses argument with a loaded API_KEY
    returns the best bid or ask on the market based on the side entered
    side = bids/asks
    the all_flag flag set in four tiers
    all = 0 sec_book[side][0][param] return one params of best bid/ask
    all = 1 sec_book[side][0]        return all params of best bid/ask
    all = 2 sec_book[side]           return all orders in the bid/ask side
    all = 3 sec_book                 return all orders from both sides
    """
    payload = {"ticker": ticker_sym}
    response = ses.get(base_url + "/securities/book", params=payload)
    _validate_response(response)

    sec_book = response.json()
    if all_flag == 1:
        return sec_book[side][0]
    if all_flag == 2:
        return sec_book[side]
    if all_flag == 3:
        return sec_book
    # this returns only one attrb of the best bid/ask offer i.e. 'quantity'
    return sec_book[side][0][param]


def get_security_info(ses, ticker_sym, side, param):
    """All possible values for the param parameter are listed at the top
    i.e. param = "trader_id"

    Returns the value of the param for the given ticker from the given side
    side = bids / asks
    """
    return _get_sec_book_response(ses, ticker_sym, side, param)


def get_best_bid(ses, ticker_sym):
    return _get_sec_book_response(ses, ticker_sym, "bids", None, all_flag=1)


def get_best_ask(ses, ticker_sym):
    return _get_sec_book_response(ses, ticker_sym, "asks", None, all_flag=1)


def get_bbo(ses, ticker_sym):
    best_bid = get_best_bid(ses, ticker_sym)
    best_ask = get_best_ask(ses, ticker_sym)
    return {"best_bid": best_bid, "best_ask": best_ask}


def get_all_bids(ses, ticker_sym):
    """Returns a list of all JSON objects in bid side of the order"""
    return _get_sec_book_response(ses, ticker_sym, "bids", None, all_flag=2)


def get_all_asks(ses, ticker_sym):
    """Returns a list of all JSON objects in ask side of the order"""
    return _get_sec_book_response(ses, ticker_sym, "asks", None, all_flag=2)


def get_all_bids_asks(ses, ticker_sym):
    """Returns a list of JSON objects representing all_flag the orders in the
    Bid and Ask side of the book
    """
    return _get_sec_book_response(ses, ticker_sym, None, None, all_flag=3)
