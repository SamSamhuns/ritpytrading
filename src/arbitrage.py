'''
Algorihmic Trading script for the ALGO1 case in RIT
The algorithm automatically trades based on arbitrage on a security
traded on two different exchanges
'''
import sys
import signal
import requests
import modules.case as case                    # importing case related functions from case.py
import modules.securities_book as book         # importing securities_book to get bis ask values
import modules.submit_cancel_orders as order   # import submit_cancel_orders to submit orders
from time import sleep

API_KEY = {'X-API-Key': 'H8KDL3Q6'}            # use your unique API key here
shutdown = False

host_url = 'http://localhost:9999'             # Make sure the RIT client uses the same 9999 port
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

# get_tick
# get bid ask

def main():

    arbitrage_qty = 1000 # arbitrage qunatity for one order

    # checking for correct number of arguments entered
    if len(sys.argv) != 3:
        print('Usage arbitrage.py SEC_A SEC_B')
        sys.exit()
    # loading the two security names
    sec1_a = (sys.argv[1]).upper()
    sec1_b = (sys.argv[2]).upper()

    with requests.Session() as ses:
        ses.headers.update(API_KEY)
        tick = case.get_tick(ses)
        while tick > 5 and tick < 295 and not shutdown:
            # get best bid and ask for security in both exchanges
            sec1_a_bid = book.get_security_info( ses, sec1_a, 'bids', 'price' )
            sec1_a_ask = book.get_security_info( ses, sec1_a, 'asks', 'price' )
            sec1_b_bid = book.get_security_info( ses, sec1_b, 'bids', 'price' )
            sec1_b_ask = book.get_security_info( ses, sec1_b, 'asks', 'price' )

            # checking for crossed markets and arbitraging
            if sec1_a_bid > sec1_b_ask:
            # if a_bid is higher than b_ask then buy at the lower b_ask and sell at the higher a_bid
                order.market_order( ses, sec1_b, 'BUY', arbitrage_qty )
                order.market_order( ses, sec1_a, 'SELL', arbitrage_qty )
                sleep(1)
            if sec1_b_bid > sec1_a_ask:
            # if b_bid is higher than a_ask then buy at the lower a_ask and sell at the higher b_bid
                order.market_order( ses, sec1_a, 'BUY', arbitrage_qty )
                order.market_order( ses, sec1_b, 'SELL', arbitrage_qty )
                sleep(1)

            # updating ticks to make sure the session is active
            tick = case.get_tick(ses)

if __name__ == '__main__':
    # registering the custom signal handler
    signal.signal( signal.SIGINT, signal_handler )
    main()
