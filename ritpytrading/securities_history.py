'''
The /securities/history module gets the OHLC history for a security.

functions related to the history of a security
securities_history object attribute values: JSON formatted
[
  {
    "tick": 11,
    "open": 4.12,
    "high": 4.21,
    "low": 4.1,
    "close": 4.15
  }
]

Parameters for the securities_history GET HTTP request

- ticker* required string   (query)
- period number             (query)
Period to retrieve data from. Defaults to the current period.
- limit number              (query)
Result set limit, counting backwards from the most recent tick.
Defaults to retrieving the entire period.
'''


# Make sure the RIT client uses the same 9999 port
host_url = 'http://localhost:9999'
base_path = '/v1'
base_url = host_url + base_path

# to print error messages and stop the program when needed


class ApiException(Exception):
    pass


class Security_History():
    # sec_history is a json obj returned from the API get request
    def __init__(self, sec_history):
        self.tick = sec_history["tick"]
        self.open = sec_history["open"]
        self.high = sec_history["high"]
        self.low = sec_history["low"]
        self.close = sec_history["close"]

    def __repr__(self):
        return self.tick

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


# period_num is the period to retrive data from. Defaults to current period.
# lim_num = Result set limit, counting backwards from the most recent tick.
# Defaults to retrieving the entire period.
def _get_sec_history_json(ses, ticker_sym, period_num=None, lim_num=None):
    # checking for optional paramaters
    payload = {}
    if period_num is None and lim_num is None:
        payload = {'ticker': ticker_sym}
    elif lim_num is None:
        payload = {'ticker': ticker_sym, 'period number': period_num}
    elif period_num is None:
        payload = {'ticker': ticker_sym, 'limit number': lim_num}
    else:
        payload = {'ticker': ticker_sym,
                   'limit number': lim_num, 'period number': period_num}

    response = ses.get(base_url + '/securities/history', params=payload)
    if response.ok:
        # return all parameters in a JSON format
        # sec_history_json
        return response.json()


# function to return a sec_history_dict dict
# with Security_History obj as values
def sec_history_response_handle(sec_history_json):
    sec_history_dict = {Security_History(sec_hist).tick: Security_History(
        sec_hist) for sec_hist in sec_history_json}

    return sec_history_dict


# function to get values of different parameters
def security_history_dict(ses, ticker_sym, period_numb=None, lim_numb=None):
    return sec_history_response_handle(_get_sec_history_json(
        ses, ticker_sym, period_num=period_numb, lim_num=lim_numb))


# get all full JSON response for the securities history get request
def security_history_json(ses, ticker_sym, period_numb=None, lim_numb=None):
    return _get_sec_history_json(
        ses, ticker_sym, period_num=period_numb, lim_num=lim_numb)
