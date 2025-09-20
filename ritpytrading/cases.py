# This script contains results for the /case and /limits module
#
# Sample JSON output formats for the function returns
# Case object return value: JSON formatted
# {
#     "name": "string",
#     "period": 0,
#     "tick": 0,
#     "ticks_per_period": 0,
#     "total_periods": 0,
#     "status": "ACTIVE",
#     "is_enforce_trading_limits": True
# }
# Limits object return values: JSON formatted
# Returned as a list containing a JSON object
# [
#     {
#         "name": "string",
#         "gross": 0,
#         "net": 0,
#         "gross_limit": 0,
#         "net_limit": 0,
#         "gross_fine": 0,
#         "net_fine": 0
#     }
# ]

from ._response_validation import _validate_response

# Make sure the RIT client uses the same 9999 port
host_url = "http://localhost:9999"
base_path = "/v1"
base_url = host_url + base_path


class Case:
    """case_response is a json obj returned from the API get request"""

    def __init__(self, case_response):
        self.name = case_response["name"]
        self.period = case_response["period"]
        self.tick = case_response["tick"]
        self.ticks_per_period = case_response["ticks_per_period"]
        self.total_periods = case_response["total_periods"]
        self.status = case_response["status"]
        self.is_enforce_trading_limits = case_response["is_enforce_trading_limits"]

    def __repr__(self):
        return self.name + "_" + self.status

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class CaseLimits:
    """limit_response is a json obj returned from the API get request"""

    def __init__(self, limit_response):
        self.name = limit_response["name"]
        self.gross = limit_response["gross"]
        self.net = limit_response["net"]
        self.gross_limit = limit_response["gross_limit"]
        self.net_limit = limit_response["net_limit"]
        self.gross_fine = limit_response["gross_fine"]
        self.net_fine = limit_response["net_fine"]

    def __repr__(self):
        return self.name + "_case_limit"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


def _get_case_json(ses, url_end):
    """function requires a requests.Session() object
    as the ses argument with a loaded API_KEY
    """
    response = ses.get(base_url + url_end)
    _validate_response(response)
    case_json = response.json()

    # returns all attributes of the case json response object
    return case_json


def _case_response_handle(case_json, url_end):
    if url_end == "/limits":
        return CaseLimits(case_json[0])
    # elif url_end == '/case':
    return Case(case_json)


def case(ses):
    """function that returns the case object"""
    return _case_response_handle(_get_case_json(ses, "/case"), "/case")


def case_json(ses):
    """returns a list of JSON formatted output for case object"""
    return _get_case_json(ses, "/case")


def trade_lim_enforce_chk(ses):
    """functions for information on case limits
    checking if a trade_limit is actually enforced
    """
    current_case = case(ses)  # calling the case func not the class instance
    if current_case.is_enforce_trading_limits:
        return True
    return False


def case_limits(ses):
    """returns  a CaseLimits obj from the CaseLimits class"""
    if trade_lim_enforce_chk(ses):
        return _case_response_handle(_get_case_json(ses, "/limits"), "/limits")
    else:
        msg = "Case has no trading limits"
        print(msg)
        return msg


def case_limits_json(ses):
    """returns a list of JSON fomratted output for case limits"""
    if trade_lim_enforce_chk(ses):
        return _get_case_json(ses, "/limits")
    else:
        msg = "Case has no trading limits"
        print(msg)
        return msg
