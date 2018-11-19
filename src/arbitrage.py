'''
Algorihmic Trading script for the ALGO1 case in RIT
The algorithm automatically trades based on arbitrage on a security
traded on two different exchanges
'''
import signal
import requests
import case.py as case_py                     # importing case related functions from case.py
from time import sleep

API_KEY = {'X-API-Key': 'H8KDL3Q6'}
shutdown = False
host_url = 'http://localhost:9999'          # Make sure the RIT client uses the same 9999 port
base_path = '/v1'
base_url = host_url + base_path

# to print error messages and stop the program when needed
class ApiException(Exception):
    pass

# signal-handler for graceful output when Ctrl C is pressed
def signal_handler( signum, frame ):
    global shutdown
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    shutdown = True
