'''
Algorihmic Trading script for the ALGO1 case in RIT
The algorithm automatically trades based on arbitrage on a security
traded on two different exchanges
'''
import sys
import signal
import requests
from time import sleep
# importing case related functions from case.py
from modules import case
# importing securities_book to get bis ask values
from modules import securities_book as book
# import submit_cancel_orders to submit orders
from modules import submit_cancel_orders as order


# use your unique API key here
API_KEY = {'X-API-Key': 'H8KDL3Q6'}
shutdown = False

# Make sure the RIT client uses the same 9999 port
host_url = 'http://localhost:9999'
base_path = '/v1'
base_url = host_url + base_path

# to print error messages and stop the program when needed


class ApiException(Exception):
    pass

# signal-handler for graceful output when Ctrl C is pressed


def signal_handler(signum, frame):
    global shutdown
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    shutdown = True


def main():

    arbitrage_qty = 1000  # arbitrage qunatity for one order by default 1000

    # checking for correct number of arguments entered
    if len(sys.argv) != 3:
        print('Usage arbitrage.py SEC_A SEC_B')
        sys.exit()
    # loading the two security names
    sec1_a = (sys.argv[1]).upper()
    sec1_b = (sys.argv[2]).upper()

    with requests.Session() as ses:
        ses.headers.update(API_KEY)
        current_case = case.case(ses)
        current_case_lim = case.case_limits(ses)
        tick = current_case.tick
        # the order submission limits are a max of 10000 units per order
        max_arbitrage_qty = min(10000, current_case_lim.gross_limit )
        while tick > 5 and tick < 295 and not shutdown:
            # get best bid and ask for security in both exchanges
            sec1_a_bid = book.get_security_info(ses, sec1_a, 'bids', 'price')
            sec1_a_ask = book.get_security_info(ses, sec1_a, 'asks', 'price')
            sec1_b_bid = book.get_security_info(ses, sec1_b, 'bids', 'price')
            sec1_b_ask = book.get_security_info(ses, sec1_b, 'asks', 'price')

            # checking for crossed markets and arbitraging
            if sec1_a_bid > sec1_b_ask:             # if a_bid is higher than b_ask then buy at the lower b_ask and sell at the higher a_bid
                # checking for the minumum qty between the two crossed orders not to prevent non-zero positions
                sec1_b_qty = book.get_security_info(
                    ses, sec1_b, 'bids', 'quantity')
                sec1_a_qty = book.get_security_info(
                    ses, sec1_a, 'asks', 'quantity')
                arbitrage_qty = min(sec1_a_qty, sec1_b_qty) % max_arbitrage_qty
                order.market_order(ses, sec1_b, 'BUY', arbitrage_qty)
                order.market_order(ses, sec1_a, 'SELL', arbitrage_qty)
                sleep(1)
            if sec1_b_bid > sec1_a_ask:             # if b_bid is higher than a_ask then buy at the lower a_ask and sell at the higher b_bid
                # checking for the minumum qty between the two crossed orders not to prevent non-zero positions
                sec1_b_qty = book.get_security_info(
                    ses, sec1_b, 'asks', 'quantity')
                sec1_a_qty = book.get_security_info(
                    ses, sec1_a, 'bids', 'quantity')
                arbitrage_qty = min(sec1_a_qty, sec1_b_qty) % max_arbitrage_qty
                order.market_order(ses, sec1_a, 'BUY', arbitrage_qty)
                order.market_order(ses, sec1_b, 'SELL', arbitrage_qty)
                sleep(1)

            # updating ticks to make sure the session is active
            current_case = case.case(ses)
            tick = current_case.tick


if __name__ == '__main__':
    # registering the custom signal handler
    signal.signal(signal.SIGINT, signal_handler)
    main()
