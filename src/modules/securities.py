'''
The securities HTTP module gets a list of available securities
and associated positions.

securities object attribute values: JSON formatted
[
  {
    "ticker": "string",
    "type": "SPOT",
    "size": 0,
    "position": 0,
    "vwap": 0,
    "nlv": 0,
    "last": 0,
    "bid": 0,
    "bid_size": 0,
    "ask": 0,
    "ask_size": 0,
    "volume": 0,
    "unrealized": 0,
    "realized": 0,
    "currency": "string",
    "total_volume": 0,
    "limits": [
      {
        "name": "string",
        "units": 0
      }
    ],
    "interest_rate": 0,
    "is_tradeable": true,
    "is_shortable": true,
    "start_period": 0,
    "stop_period": 0
  }
]


Parameters for the securities GET HTTP request
- ticker* required string   (query)
- period number             (query)

'''

import requests

# Make sure the RIT client uses the same 9999 port
host_url = 'http://localhost:9999'
base_path = '/v1'
base_url = host_url + base_path

# to print error messages and stop the program when needed


class ApiException(Exception):
    pass
