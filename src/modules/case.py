'''
This script contains results for the /case and /limits module

Sample JSON output formats for the function returns
Case object return value: JSON formatted
{
    "name": "string",
    "period": 0,
    "tick": 0,
    "ticks_per_period": 0,
    "total_periods": 0,
    "status": "ACTIVE",
    "is_enforce_trading_limits": true
}
Limits object return values: JSON formatted
{
    "name": "string",
    "gross": 0,
    "net": 0,
    "gross_limit": 0,
    "net_limit": 0,
    "gross_fine": 0,
    "net_fine": 0
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
def get_case_response ( ses, url_end, param, all=0 ):
    response = ses.get( base_url + url_end )
    if response.ok:
        case = response.json()
        # returns all attributes of the case json response object
        if all == 1:
            return case
        return case[param]
    raise ApiException('Authorization Error: Please check API key.')

def get_name( ses ):
    return get_case_response( ses, '/case', 'name')

def get_status( ses ):
    return get_case_response( ses, '/case', 'status')

def get_tick( ses ):
    return get_case_response( ses, '/case', 'tick')

def get_period( ses ):
    return get_case_response( ses, '/case', 'period')

def get_total_periods( ses ):
    return get_case_response( ses, '/case', 'get_periods')

def get_ticks_per_period( ses ):
    return get_case_response( ses, '/case', 'ticks_per_period')

# returns json object containing full info on case
def get_case_all( ses ):
    return get_case_response( ses, '/case', '', 1 )

# functions for information on case limits
# checking if a trade_limit is actually enforced
def trade_lim_enforce_chk (ses):
    if get_case_response( ses, '/case', 'is_enforce_trading_limits') == True:
        return True
    return False

def get_gross( ses ):
    if trade_lim_enforce_chk(ses) == True:
        return get_case_response( ses, '/limits', 'gross')
    else:
        no_lim_msg = "No trading limits for the current case"
        return no_lim_msg

def get_set( ses ):
    if trade_lim_enforce_chk(ses) == True:
        return get_case_response( ses, '/limits', 'set')
    else:
        no_lim_msg = "No trading limits for the current case"
        return no_lim_msg

def get_gross_lim( ses ):
    if trade_lim_enforce_chk(ses) == True:
        return get_case_response( ses, '/limits', 'gross_limit')
    else:
        no_lim_msg = "No trading limits for the current case"
        return no_lim_msg

def get_set_limit( ses ):
    if trade_lim_enforce_chk(ses) == True:
        return get_case_response( ses, '/limits', 'set_limit')
    else:
        no_lim_msg = "No trading limits for the current case"
        return no_lim_msg

def get_gross_fine( ses ):
    if trade_lim_enforce_chk(ses) == True:
        return get_case_response( ses, '/limits', 'gross_fine')
    else:
        no_lim_msg = "No trading limits for the current case"
        return no_lim_msg

def get_set_fine( ses ):
    if trade_lim_enforce_chk(ses) == True:
        return get_case_response( ses, '/limits', 'set_fine')
    else:
        no_lim_msg = "No trading limits for the current case"
        return no_lim_msg

def get_limits_case_all( ses ):
    if trade_lim_enforce_chk(ses) == True:
        return get_case_response( ses, '/limits', None, all=1)
    else:
        no_lim_msg = "No trading limits for the current case"
        return no_lim_msg
