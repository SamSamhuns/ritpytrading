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
Result set limit, counting backwards from the most recent tick. Defaults to retrieving the entire period.
'''

import requests

host_url = 'http://localhost:9999'          # Make sure the RIT client uses the same 9999 port
base_path = '/v1'
base_url = host_url + base_path

# to print error messages and stop the program when needed
class ApiException(Exception):
    pass

def get_sec_history_response( ses, ticker_sym, param, all=0, period_num = None, lim_num = None ):
    # checking for optional paramaters
    payload = {}
    if period_num == None and  lim_num = None:
        payload = { 'ticker':ticker_sym }
    elif lim_num == None:
        payload = { 'ticker':ticker_sym, 'period number':period_num }
    elif period_num == None:
        payload = { 'ticker':ticker_sym, 'limit number':lim_num }
    else:
        payload = { 'ticker':ticker_sym, 'limit number':lim_num, 'period number':period_num }

    response = ses.get( base_url + '/securities/history', params=payload )
    if response.ok:
        securities_history = response.json()
        # if the all flag is set to 1 return all parameters in a JSON format
        if all == 1:
            return securities_history
        return securities_history[0][param]

# function to get values of different parameters
def get_hist_tick ( ses, ticker_sym, period_numb = None, lim_numb = None ):
    return get_sec_history_response( ses, ticker_sym, 'tick', period_num = period_numb, lim_num = lim_numb )

def get_hist_open ( ses, ticker_sym, period_numb = None, lim_numb = None ):
    return get_sec_history_response( ses, ticker_sym, 'open', period_num = period_numb, lim_num = lim_numb )

def get_hist_high ( ses, ticker_sym, period_numb = None, lim_numb = None ):
    return get_sec_history_response( ses, ticker_sym, 'high', period_num = period_numb, lim_num = lim_numb )

def get_hist_low ( ses, ticker_sym, period_numb = None, lim_numb = None ):
    return get_sec_history_response( ses, ticker_sym, 'low', period_num = period_numb, lim_num = lim_numb )

def get_hist_close ( ses, ticker_sym, period_numb = None, lim_numb = None ):
    return get_sec_history_response( ses, ticker_sym, 'close', period_num = period_numb, lim_num = lim_numb )

# get all full JSON response for the securities history get request
def get_sec_hist_all ( ses, ticker_sym, period_numb = None, lim_numb = None ):
    return get_sec_history_response( ses, ticker_sym, all=1, period_num = period_numb, lim_num = lim_numb )
