'''
The securities HTTP module gets a list of available securities
and associated positions.

securities object attribute values: JSON formatted
[
  {
    "ticker": "string",
    "type": "SPOT",
    "size": 0,
    "position": 0,
    "vwap": 0,
    "nlv": 0,
    "last": 0,
    "bid": 0,
    "bid_size": 0,
    "ask": 0,
    "ask_size": 0,
    "volume": 0,
    "unrealized": 0,
    "realized": 0,
    "currency": "string",
    "total_volume": 0,
    "limits": [
      {
        "name": "string",
        "units": 0
      }
    ],
    "interest_rate": 0,
    "is_tradeable": true,
    "is_shortable": true,
    "start_period": 0,
    "stop_period": 0
  }
]


Parameters for the securities GET HTTP request
- ticker* required string   (query)

'''

import requests

# Make sure the RIT client uses the same 9999 port
host_url = 'http://localhost:9999'
base_path = '/v1'
base_url = host_url + base_path

# to print error messages and stop the program when needed


class ApiException(Exception):
    pass


class Security():
    def __self__(self, security_response_obj):
        self.ticker = security_response_obj["ticker"]
        self.type = security_response_obj["type"]
        self.size = security_response_obj["size"]
        self.position = security_response_obj["position"]
        self.vwap = security_response_obj["vwap"]
        self.nlv = security_response_obj["nlv"]
        self.last = security_response_obj["last"]
        self.bid = security_response_obj["bid"]
        self.bid_size = security_response_obj["bid_size"]
        self.ask = security_response_obj["ask"]
        self.ask_size = security_response_obj["ask_size"]
        self.volume = security_response_obj["volume"]
        self.unrealized = security_response_obj["unrealized"]
        self.realized = security_response_obj["realized"]
        self.currency = security_response_obj["currency"]
        self.total_volume = security_response_obj["total_volume"]
        self.limits = security_response_obj["limits"]
        self.interest_rate = security_response_obj["interest_rate"]
        self.is_tradeable = security_response_obj["is_tradeable"]
        self.is_shortable = security_response_obj["is_shortable"]
        self.start_period = security_response_obj["start_period"]
        self.stop_period = security_response_obj["stop_period"]

    def __repr__(self):
        return self.ticker

# gets the list of all available securities or of a particular
# security if its ticker is supplied


def get_security_response(ses, ticker, json=0):
    if ticker != None:
        payload = {'ticker': ticker}
        response = ses.get(base_url + '/securities', params=payload)
    else:
        response = ses.get(base_url + '/securities')

    if response.ok:
        # this sets a list of all available securities in a JSON format
        sec_info = response.json()
        if json == 1:
            return sec_info

        order_list = {(Security(order)).ticker: Security(order)
                      for order in sec_info}
        # returns a dict of security obj of the security class with ticker ticker names as keys
        return order_list

# By default no specific ticker_sym is None

# returns the list of available securities as a dict of security objects with ticker name as keys


def securities_dict(ses, ticker_sym=None):
    return get_security_response(ses, ticker_sym)

# returns the list of available securities with all info in a json format


def securities_json(ses, ticker_sym=None):
    return get_security_response(ses, ticker_sym, json=1)
