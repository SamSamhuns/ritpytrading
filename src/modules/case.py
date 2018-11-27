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
Returned as a list containing a JSON object
[
    {
        "name": "string",
        "gross": 0,
        "net": 0,
        "gross_limit": 0,
        "net_limit": 0,
        "gross_fine": 0,
        "net_fine": 0
    }
]
'''

import requests

# Make sure the RIT client uses the same 9999 port
host_url = 'http://localhost:9999'
base_path = '/v1'
base_url = host_url + base_path

# to print error messages and stop the program when needed


class ApiException(Exception):
    pass

class Case():
    def _init__(self, case_response):
        self.name = case_response["name"]
        self.period = case_response["period"]
        self.tick = case_response["tick"]
        self.ticks_per_period = case_response["ticks_per_period"]
        self.total_periods = case_response["total_periods"]
        self.status = case_response["status"]
        self.is_enforce_trading_limits = case_response["is_enforce_trading_limits"]

    def __repr__(self):
        return self.name + '_' + self.status

class CaseLimits():
    def __init__(self, limit_response):
        self.name = limit_response["name"]
        self.gross = limit_response['gross']
        self.net = limit_response['net']
        self.gross_limit = limit_response['gross_limit']
        self.net_limit = limit_response['net_limit']
        self.gross_fine = limit_response['gross_fine']
        self.net_fine =  limit_response['net_fine']

    def __repr__(self):
        pass

# function requires a requests.Session() object as the ses argument with a loaded API_KEY


def get_case_response(ses, url_end, param, all=0):
    response = ses.get(base_url + url_end)
    if response.ok:
        case = response.json()
        # returns all attributes of the case json response object
        if all == 1:
            return case
        if url_end == '/limits':
            return case[0][param]
        # elif url_end == '/case':
        return case[param]
    raise ApiException('Authorization Error: Please check API key.')

# function that returns the case object
def case(ses):
    return get_case_response(ses, '/case')


# functions for information on case limits
# checking if a trade_limit is actually enforced


def trade_lim_enforce_chk(ses):
    if get_case_response(ses, '/case', 'is_enforce_trading_limits') == True:
        return True
    return False


def get_gross(ses):
    if trade_lim_enforce_chk(ses) == True:
        return get_case_response(ses, '/limits', 'gross')
    else:
        no_lim_msg = "No trading limits for the current case"
        return no_lim_msg


def get_set(ses):
    if trade_lim_enforce_chk(ses) == True:
        return get_case_response(ses, '/limits', 'set')
    else:
        no_lim_msg = "No trading limits for the current case"
        return no_lim_msg


def get_gross_lim(ses):
    if trade_lim_enforce_chk(ses) == True:
        return get_case_response(ses, '/limits', 'gross_limit')
    else:
        no_lim_msg = "No trading limits for the current case"
        return no_lim_msg


def get_set_limit(ses):
    if trade_lim_enforce_chk(ses) == True:
        return get_case_response(ses, '/limits', 'set_limit')
    else:
        no_lim_msg = "No trading limits for the current case"
        return no_lim_msg


def get_gross_fine(ses):
    if trade_lim_enforce_chk(ses) == True:
        return get_case_response(ses, '/limits', 'gross_fine')
    else:
        no_lim_msg = "No trading limits for the current case"
        return no_lim_msg


def get_set_fine(ses):
    if trade_lim_enforce_chk(ses) == True:
        return get_case_response(ses, '/limits', 'set_fine')
    else:
        no_lim_msg = "No trading limits for the current case"
        return no_lim_msg


def get_limits_case_all(ses):
    if trade_lim_enforce_chk(ses) == True:
        return get_case_response(ses, '/limits', None, all=1)
    else:
        no_lim_msg = "No trading limits for the current case"
        return no_lim_msg
