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


# Make sure the RIT client uses the same 9999 port
host_url = 'http://localhost:9999'
base_path = '/v1'
base_url = host_url + base_path

# to print error messages and stop the program when needed


class ApiException(Exception):
    pass

# Security class takes a security_response object ( a list of json objects )
# as its initializing paramenter to extract all relevant information


class Security():
    # security_response is a json obj returned from the API get request
    def __init__(self, security_response):
        self.ticker = security_response["ticker"]
        self.type = security_response["type"]
        self.size = security_response["size"]
        self.position = security_response["position"]
        self.vwap = security_response["vwap"]
        self.nlv = security_response["nlv"]
        self.last = security_response["last"]
        self.bid = security_response["bid"]
        self.bid_size = security_response["bid_size"]
        self.ask = security_response["ask"]
        self.ask_size = security_response["ask_size"]
        self.volume = security_response["volume"]
        self.unrealized = security_response["unrealized"]
        self.realized = security_response["realized"]
        self.currency = security_response["currency"]
        self.total_volume = security_response["total_volume"]
        self.limits = security_response["limits"]
        self.interest_rate = security_response["interest_rate"]
        self.is_tradeable = security_response["is_tradeable"]
        self.is_shortable = security_response["is_shortable"]
        self.start_period = security_response["start_period"]
        self.stop_period = security_response["stop_period"]

    def __repr__(self):
        return self.ticker

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

# gets the list of all available securities or of a particular
# security if its ticker is supplied


def _get_security_json(ses, ticker):
    if ticker is not None:
        payload = {'ticker': ticker}
        response = ses.get(base_url + '/securities', params=payload)
    else:
        response = ses.get(base_url + '/securities')

    if response.ok:
        # this sets a list of all available securities in a JSON format
        return response.json()
    raise ApiException('Authorization Error: Please check API key.')

# return a order_dict dict of Security class objects


def security_response_handle(sec_info_json):
    order_dict = {(Security(order)).ticker: Security(order)
                  for order in sec_info_json}
    # returns a dict of security obj of the security class
    # with ticker ticker names as keys
    return order_dict

# By default no specific ticker_sym is None
# returns the list of available securities as a
# dict of security objects with ticker name as keys


def security_dict(ses, ticker_sym=None):
    return security_response_handle(_get_security_json(ses, ticker_sym))

# returns the list of available securities with all info in a json format


def security_json(ses, ticker_sym=None):
    return _get_security_json(ses, ticker_sym)
