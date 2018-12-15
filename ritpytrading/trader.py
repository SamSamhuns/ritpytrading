'''
Sample JSON output formats for the function returns
trader object return value: JSON formatted
{
  "trader_id": "string",
  "first_name": "string",
  "last_name": "string",
  "nlv": 0
}
'''


# Make sure the RIT client uses the same 9999 port
host_url = 'http://localhost:9999'
base_path = '/v1'
base_url = host_url + base_path

# to print error messages and stop the program when needed


class ApiException(Exception):
    pass

# Trader class takes a trader_response object which is a json obj
# to extract all relevant information


class Trader():
    # trader_response is a json obj returned from the API get request
    def __init__(self, trader_response):
        self.trader_id = trader_response['trader_id']
        self.first_name = trader_response['first_name']
        self.last_name = trader_response['last_name']
        self.nlv = trader_response['nlv']

    def __repr__(self):
        return self.first_name + '_' + self.last_name + '_' + self.trader_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

# function requires a requests.Session() object
# as the ses argument with a loaded API_KEY


def _get_trader_json(ses):
    response = ses.get(base_url + '/trader')
    if response.ok:
        trader_json = response.json()
        return trader_json
    raise ApiException('Authorization Error: Please check API key.')

# function to return a Trader class obj


def trader_response_handle(trader_json):
    return Trader(trader_json)


def trader(ses):
    return trader_response_handle(_get_trader_json(ses))
