import requests

host_url = 'http://localhost:9999'          # Make sure the RIT client uses the same 9999 port
base_path = '/v1'
base_url = host_url + base_path

# to print error messages and stop the program when needed
class ApiException(Exception):
    pass

# function requires a requests.Session() object as the ses argument with a loaded API_KEY
def get_trader_response( ses, param, full=0 ):
    response = ses.get(base_url+ '/trader')
    if response.ok:
        trader = response.json()
        if full == 1:
            return trader
        return trader[param]
    raise ApiException('Authorization Error: Please check API key.')

def get_trader_id( ses ):
    get_trader_response( ses, 'trader_id' )

def get_trader_fname( ses ):
    get_trader_response( ses, 'first_name')

def get_trader_lname( ses ):
    get_trader_response( ses, 'last_name')

def get_trader_nlv( ses ):
    get_trader_response( ses, 'nlv')

def get_trader_all( ses ):
    get_trader_response( ses, '', 1)
