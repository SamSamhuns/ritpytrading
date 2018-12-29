import sys
import requests
import unittest
import contextlib
from io import StringIO
@contextlib.contextmanager
from ritpytrading import news
from ritpytrading import cases
from ritpytrading import assets
from ritpytrading import orders
from ritpytrading import tenders
from ritpytrading import traders
from ritpytrading import securities
from ritpytrading import securities_book
from ritpytrading import securities_history as sh
from ritpytrading import submit_cancel_orders as sco

# THIS TEST IS DESIGNED FOR THE Liability Trading 3 Case File
API_KEY = {'X-API-key': 'TY0Y1KE9'}           # use your RIT API key here
# Make sure the RIT client uses the same 9999 port
# host_url = 'http://localhost:9999'
# base_path = '/v1'
# base_url = host_url + base_path

class ApiException(Exception):
    """ to print error messages and stop the program when needed """
    pass

def capture():
    oldout,olderr = sys.stdout, sys.stderr
    try:
        out=[StringIO(), StringIO()]
        sys.stdout,sys.stderr = out
        yield out
    finally:
        sys.stdout,sys.stderr = oldout, olderr
        out[0] = out[0].getvalue()
        out[1] = out[1].getvalue()

# Example usage
# with capture() as out:
#     print ('hi')

def test_assets(ses, ticker=None):
    response = ses.get('http://localhost:9999/v1/assets')
    if response.ok:
        assets_json = response.json()
        asset_list1 = assets.assets_list(ses)
        asset_list2 = assets_json
        if ticker is None:
            asset_dict1 = assets.assets_dict(ses)
            asset_dict2 = {
                assets.Asset(asset_obj).ticker: assets.Asset(asset_obj)
                           for asset_obj in assets_json}
        # if ticker sumbol is given
        elif ticker is not None:
            asset_obj1 = assets.asset(ses, ticker)
            asset_obj2 = assets.Asset(assets_json[0])
        # ASSERT EQUAL HERE

def test_cases(ses):
    response = ses.get('http://localhost:9999/v1/case')
    if response.ok:
        case_obj1 = cases.case(ses)
        case_json1 = cases.case_json(ses)

        case_obj2 = cases.Case(response.json())
        case_json2 = response.json()

        enforce = cases.trade_lim_enforce_chk(ses)
        # ASSERT EQUAL HERE

    response = ses.get('http://localhost:9999/v1/limits')
    if response.ok and enforce:
        limits_json = response.json()
        case_limit_obj1 = cases.case_limits(ses)
        case_limit_obj2 = cases.CaseLimits(limits_json[0])

        case_limit_json1 = cases.case_limits_json(ses)
        case_limit_json2 = limits_json
        # ASSERT EQUAL HERE

def test_news(ses):
    response = ses.get('http://localhost:9999/v1/news')
    if response.ok:
        news_json = response.json()
        news_dict1 = news.news_dict(ses)
        news_dict2 = {news.News(news_obj).news_id: news.News(news_obj)
                     for news_obj in news_json}

        news_list1 = news.news_json(ses)
        news_list2 = news_json
        # ASSERT EQUAL HERE

def test_traders(ses):
    response = ses.get('http://localhost:9999/v1/trader')
    if response.ok:
        trader_json = response.json()
        trader_obj1 = traders.trader(ses)
        trader_obj2 = traders.Trader(trader_json)
        # ASSERT EQUAL HERE

def test_tenders(ses):
    response = ses.get('http://localhost:9999/v1/tenders')
    if response.ok:
        tenders_json = response.json()
        tenders_dict1 = tenders.tenders_dict(ses)
        tenders_dict2 = {tenders.Tender(tender_obj).tender_id:
            tenders.Tender(tender_obj) for tender_obj in tenders_json}
        tenders_list1 = tenders.tenders_json(ses)
        tenders_list2 = tenders_json
        # ASSERT EQUAL HERE
    ### IMPORTANT NEEDS ADDITIONAL TENDER ACCEPT TESTS

def test_submit_cancel_orders(ses):
    ticker = 'CRZY'
    side = 'BUY'
    quantity = 100
    lim_price = 30

    # MARKET ORDER CHECK
    mkt_order_params = {'ticker': ticker, 'type': 'MARKET',
                        'quantity': quantity, 'action': side}
    response = ses.post(base_url + '/orders', params=mkt_order_params)
    if response.ok:
        mkt_order = response.json()
        orderId = mkt_order['order_id']
    else:
        raise ApiException('Authorization Error: Please check API key.')

    with capture() as market_msg1:
        sco.market_order(ses, ticker, side, quantity)
    market_msg2 = ('%s %s Market order was submitted and has ID %d' %
          (side, quantity, orderId))
    # ASSERT EQUAL HERE


    # LIMIT ORDER CHECK
    lim_order_params = {'ticker': ticker, 'type': 'LIMIT',
                        'quantity': quantity, 'price': price, 'action': side}
    response = ses.post(base_url + '/orders', params=lim_order_params)
    if response.ok:
        lim_order = response.json()
        orderId = lim_order['order_id']
    else:
        raise ApiException('Authorization Error: Please check API key.')

    with capture() as limit_msg1:
        sco.limit_order(ses, TICKER, side, qty, lim_price)
    limit_msg2 = ("%s %s Limit order was submitted and has ID %d" %
                  (side, quantity, orderId))
    # ASSERT EQUAL HERE

    #Make sure there are unfufilled orders present in the book first
    #CANCEL ORDER TEST
    response = ses.get('http://localhost:9999/v1/orders')
    if response.ok:
        orders_dict = orders.orders_dict(ses)
        for ord_id in orders_dict:
            with capture() as cancel_msg1:
                sco.cancel_order(ses, ord_id)
            cancel_msg2 = (
                'Order ' + ord_id + ' was successfully cancelled.')
        # ASSERT EQUAL HERE


def test_orders(ses):
    response = ses.get('http://localhost:9999/v1/orders')
    if response.ok:
        order_json = response.json()
        orders_json1 = orders.orders_json(ses)
        orders_json2 = order_json

        orders_dict1 = orders.orders_dict(ses)
        orders_dict2 = {(orders.Order(ord)).order_id: orders.Order(ord)
                       for ord in order_json}
        # ASSERT EQUAL HERE

        for ord_id in orders_dict1:
            orders_obj1 = orders.order(ses, ord_id)
            orders_obj2 = orders.Order(order_json)
            # ASSERT EQUAL HERE

def test_securities_history(ses):
    response = ses.get('http://localhost:9999/v1/orders')
    ticker_sym = ''
    if response.ok:
        orders_dict1 = orders.orders_dict(ses)
        for ord_id in orders_dict1:
            ticker_sym = orders_dict1[ord_id].ticker
            break

    payload = {'ticker': ticker_sym}
    response = ses.get(
        'http://localhost:9999/v1/securities/history', params=payload)
    if response.ok:
        sec_history_json = response.json()
        sec_history_json1 = sh.security_history_json(ses, ticker_sym)
        sec_history_json2 = sec_history

        sec_history_dict1 = sh.security_history_dict(ses, ticker_sym)
        sec_history_dict2 = {
            sh.Security_History(sec_hist).tick: sh.Security_History(
                sec_hist) for sec_hist in sec_history_json}
        # ASSERT EQUAL HERE

def test_securites(ses):
    response = ses.get('http://localhost:9999/v1/securities')
    if response.ok:
        sec_info_json = response.json()
        sec_json1 = securities.security_json(ses)
        sec_json2 = sec_info_json

        sec_dict1 = securities.security_dict(ses)
        sec_dict2 = {
            (securites.Security(order)).ticker: securities.Security(order)
                      for order in sec_info_json}
        # ASSERT EQUAL HERE

def main():
    with requests.Session() as ses:
        ses.headers.update(API_KEY)


        response = ses.get('http://localhost:9999/v1/case')
        if response.ok:
            case = response.json()
            tick = case['tick']
            print('The case is on tick', tick)

if __name__ == "__main__":
    main()
