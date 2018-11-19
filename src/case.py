import requests

host_url = 'http://localhost:9999'          # Make sure the RIT client uses the same 9999 port
base_path = '/v1'

# to print error messages and stop the program when needed
class ApiException(Exception):
    pass

# function requires a requests.Session() object as the ses argument with a loaded API_KEY
def get_case_response ( ses, param, full=0 ):
    response = ses.get( host_url + base_path + '/case')
    if response.ok:
        case = response.json()
        if full == 1:
            return case
        return case[param]
    raise ApiException('Authorization Error: Please check API key.')

def get_name( ses ):
    get_case_response( ses, 'name')

def get_status( ses ):
    get_case_response( ses, 'status')

def get_tick( ses ):
    get_case_response( ses, 'tick')

def get_period( ses ):
    get_case_response( ses, 'period')

def get_total_periods( ses ):
    get_case_response( ses, 'get_periods')

def get_ticks_per_period( ses ):
    get_case_response( ses, 'ticks_per_period')

def get_full_response( ses ):
    get_case_response( ses, '', 1 )
