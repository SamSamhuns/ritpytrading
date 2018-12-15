'''
This script contains results for the /assets module

Sample JSON output formats for the function returns
News object return value: JSON formatted
[
  {
    "ticker": "string",
    "type": "CONTAINER",
    "description": "string",
    "total_quantity": 0,
    "available_quantity": 0,
    "lease_price": 0,
    "convert_from": [
      {
        "ticker": "string",
        "quantity": 0
      }
    ],
    "convert_to": [
      {
        "ticker": "string",
        "quantity": 0
      }
    ],
    "containment": {
      "ticker": "string",
      "quantity": 0
    },
    "ticks_per_conversion": 0,
    "ticks_per_lease": 0,
    "is_available": true,
    "start_period": 0,
    "stop_period": 0
  }
]
Parameters for the news GET HTTP request
- ticker    string        (query)

'''


# Make sure the RIT client uses the same 9999 port
host_url = 'http://localhost:9999'
base_path = '/v1'
base_url = host_url + base_path

# to print error messages and stop the program when needed


class ApiException(Exception):
    pass


class Asset():
    # case_response is a json obj returned from the API get request
    def __init__(self, asset_response):
        self.ticker = asset_response["ticker"]
        self.type = asset_response["type"]
        self.description = asset_response["description"]
        self.total_quantity = asset_response["total_quantity"]
        self.available_quantity = asset_response["available_quantity"]
        self.lease_price = asset_response["lease_price"]
        self.convert_from = asset_response["convert_from"]
        self.convert_to = asset_response["convert_to"]
        self.containment = asset_response["containment"]
        self.ticks_per_conversion = asset_response["ticks_per_conversion"]
        self.ticks_per_lease = asset_response["ticks_per_lease"]
        self.is_available = asset_response["is_available"]
        self.start_period = asset_response["start_period"]
        self.stop_period = asset_response["stop_period"]

    def __repr__(self):
        return self.ticker + ' ' + self.type + ' Asset'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

# function requires a requests.Session() object
# as the ses argument with a loaded API_KEY
# ticker = ticker sumbol
# returns a JSON obj with params given at the top


def _get_assets_json(ses, ticker=None):
    payload = {}
    if ticker is not None:
        payload = {'ticker': ticker}

    response = ses.get(base_url + "/assets", params=payload)
    if response.ok:
        assets_json = response.json()
        return assets_json
    raise ApiException('Authorization Error: Please check API key.')


def assets_response_handle(assets_json, ticker=None):
    # if no ticker is given, return a dict of asset objects
    if ticker is None:
        assets_dict = {Asset(asset_obj).ticker: Asset(asset_obj)
                       for asset_obj in assets_json}
    # if ticker sumbol is given
    elif ticker is not None:
        assets_dict = Asset(assets_json[0])

    return assets_dict


# function that returns a single asset object given for a given ticker
def asset(ses, ticker_sym):
    return assets_response_handle(_get_assets_json(
        ses, ticker=ticker_sym), ticker=ticker_sym)

# function that returns a dictionary of the assets object


def assets_dict(ses):
    return assets_response_handle(_get_assets_json(ses))

# returns a list of JSON fomratted output for assets object


def assets_list(ses):
    return _get_assets_json(ses)
