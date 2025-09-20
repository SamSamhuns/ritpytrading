# Sample JSON output formats for the function returns
# trader object return value: JSON formatted
# {
#   "trader_id": "string",
#   "first_name": "string",
#   "last_name": "string",
#   "nlv": 0
# }

from ._response_validation import _validate_response

# Make sure the RIT client uses the same 9999 port
host_url = "http://localhost:9999"
base_path = "/v1"
base_url = host_url + base_path


class ApiException(Exception):
    """to print error messages and stop the program when needed"""

    pass


class Trader:
    """Trader class takes a trader_response object which is a json obj
    to extract all relevant information.
    trader_response is a json obj returned from the API get request
    """

    def __init__(self, trader_response):
        self.trader_id = trader_response["trader_id"]
        self.first_name = trader_response["first_name"]
        self.last_name = trader_response["last_name"]
        self.nlv = trader_response["nlv"]

    def __repr__(self):
        return self.first_name + "_" + self.last_name + "_" + self.trader_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


def _get_trader_json(ses):
    """function requires a requests.Session() object
    as the ses argument with a loaded API_KEY
    """
    response = ses.get(base_url + "/trader")

    _validate_response(response)
    trader_json = response.json()
    return trader_json


def _trader_response_handle(trader_json):
    """function to return a Trader class obj"""
    return Trader(trader_json)


def trader(ses):
    return _trader_response_handle(_get_trader_json(ses))
