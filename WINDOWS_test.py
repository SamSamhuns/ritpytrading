"""
WARNING: This test module will not guarantee success as all the modules will be
tested and Trading Cases might not have all different features activated
"""

import sys
import requests

# import unittest
import contextlib
from io import StringIO
from ritpytrading import news
from ritpytrading import cases
from ritpytrading import assets
from ritpytrading import orders
from ritpytrading import tenders
from ritpytrading import traders
from ritpytrading import securities
from ritpytrading import securities_book as sb
from ritpytrading import securities_history as sh
from ritpytrading import submit_cancel_orders as sco

# THIS TEST IS DESIGNED FOR THE Liability Trading 3 Case File
# use your RIT API key here
API_KEY = {"X-API-key": "TY0Y1KE9"}
# Make sure the RIT client uses the same 9999 port
host_url = "http://localhost:9999"
base_path = "/v1"
base_url = host_url + base_path


class ApiException(Exception):
    """to print error messages and stop the program when needed"""

    pass


@contextlib.contextmanager
def capture():
    """function to capture std out
        Example usage:
        with capture() as out:
            print ('hi')
    `   `"""
    oldout, olderr = sys.stdout, sys.stderr
    try:
        out = [StringIO(), StringIO()]
        sys.stdout, sys.stderr = out
        yield out
    finally:
        sys.stdout, sys.stderr = oldout, olderr
        out[0] = out[0].getvalue()
        out[1] = out[1].getvalue()


def test_assets(ses, ticker=None):
    response = ses.get(base_url + "/assets")
    if response.ok:
        assets_json = response.json()
        asset_list1 = assets.assets_list(ses)
        asset_list2 = assets_json
        if asset_list1 != asset_list2:
            raise AssertionError("Asset list not equal")
        if ticker is None:
            asset_dict1 = assets.assets_dict(ses)
            asset_dict2 = {
                assets.Asset(asset_obj).ticker: assets.Asset(asset_obj)
                for asset_obj in assets_json
            }

            if asset_dict1 != asset_dict2:
                raise AssertionError("Asset dicts not equal")

        # if ticker sumbol is given
        elif ticker is not None:
            asset_obj1 = assets.asset(ses, ticker)
            asset_obj2 = assets.Asset(assets_json[0])
            if asset_obj1.__dict__ != asset_obj2.__dict__:
                raise AssertionError("Assets objects not equal")
    else:
        raise ApiException("Authorization Error: Please check API key.")


def test_cases(ses):
    response = ses.get(base_url + "/case")
    if response.ok:
        case_obj1 = cases.case(ses)
        case_obj2 = cases.Case(response.json())
        if case_obj1.__dict__ != case_obj2.__dict__:
            raise AssertionError("Case objects not equal")

        case_json1 = cases.case_json(ses)
        case_json2 = response.json()
        if case_json1 != case_json2:
            raise AssertionError("Case JSONs not equal")

        enforce = cases.trade_lim_enforce_chk(ses)
    else:
        raise ApiException("Authorization Error: Please check API key.")

    response = ses.get(base_url + "/limits")
    if response.ok and enforce:
        limits_json = response.json()
        case_limit_obj1 = cases.case_limits(ses)
        case_limit_obj2 = cases.CaseLimits(limits_json[0])
        if case_limit_obj1.__dict__ != case_limit_obj2.__dict__:
            raise AssertionError("Case Lim obj not equal")

        case_lim_json1 = cases.case_limits_json(ses)
        case_lim_json2 = limits_json
        if case_lim_json1 != case_lim_json2:
            raise AssertionError("Case lim JSON not equal")
    else:
        raise ApiException("Authorization Error: Please check API key.")


def test_news(ses):
    response = ses.get(base_url + "/news")
    if response.ok:
        news_json = response.json()
        news_dict1 = news.news_dict(ses)
        news_dict2 = {
            news.News(news_obj).news_id: news.News(news_obj) for news_obj in news_json
        }
        if news_dict1 != news_dict2:
            raise AssertionError("News dict not equal")

        news_list1 = news.news_json(ses)
        news_list2 = news_json
        if news_list1 != news_list2:
            raise AssertionError("News list not equal")
    else:
        raise ApiException("Authorization Error: Please check API key.")


def test_traders(ses):
    response = ses.get(base_url + "/trader")
    if response.ok:
        trader_json = response.json()
        trader_obj1 = traders.trader(ses)
        trader_obj2 = traders.Trader(trader_json)

        if trader_obj1.__dict__ != trader_obj2.__dict__:
            raise AssertionError("Trader obj not equal")
    else:
        raise ApiException("Authorization Error: Please check API key.")


def test_tenders(ses):
    response = ses.get(base_url + "/tenders")
    if response.ok:
        tenders_json = response.json()
        tenders_dict1 = tenders.tenders_dict(ses)
        tenders_dict2 = {
            tenders.Tender(tender_obj).tender_id: tenders.Tender(tender_obj)
            for tender_obj in tenders_json
        }
        if tenders_dict1 != tenders_dict2:
            raise AssertionError("Tenders dict not equal")

        tenders_list1 = tenders.tenders_json(ses)
        tenders_list2 = tenders_json
        if tenders_list1 != tenders_list2:
            raise AssertionError("Tenders list not equal")
    # IMPORTANT NEEDS ADDITIONAL TENDER ACCEPT TESTS
    else:
        raise ApiException("Authorization Error: Please check API key.")


def test_submit_cancel_orders(ses):
    ticker = "CRZY"
    side = "BUY"
    quantity = 100
    lim_price = 30

    # MARKET ORDER CHECK
    mkt_order_params = {
        "ticker": ticker,
        "type": "MARKET",
        "quantity": quantity,
        "action": side,
    }
    response = ses.post(base_url + "/orders", params=mkt_order_params)
    if response.ok:
        mkt_order = response.json()
        orderId = mkt_order["order_id"]
    else:
        raise ApiException("Authorization Error: Please check API key.")

    with capture() as market_msg1:
        sco.market_order(ses, ticker, side, quantity)
    market_msg2 = "%s %s Market order was submitted and has ID %d" % (
        side,
        quantity,
        orderId,
    )
    if market_msg1 != market_msg2:
        raise AssertionError("Market order msg not equal")

    # LIMIT ORDER CHECK
    lim_order_params = {
        "ticker": ticker,
        "type": "LIMIT",
        "quantity": quantity,
        "price": price,
        "action": side,
    }
    response = ses.post(base_url + "/orders", params=lim_order_params)
    if response.ok:
        lim_order = response.json()
        orderId = lim_order["order_id"]
    else:
        raise ApiException("Authorization Error: Please check API key.")

    with capture() as limit_msg1:
        sco.limit_order(ses, TICKER, side, qty, lim_price)
    limit_msg2 = "%s %s Limit order was submitted and has ID %d" % (
        side,
        quantity,
        orderId,
    )
    if limit_msg1 != limit_msg2:
        raise AssertionError("Limit order msg not equal")

    # Make sure there are unfufilled orders present in the book first
    # CANCEL ORDER TEST
    response = ses.get(base_url + "/orders")
    if response.ok:
        orders_dict = orders.orders_dict(ses)
        for ord_id in orders_dict:
            with capture() as cancel_msg1:
                sco.cancel_order(ses, ord_id)
            cancel_msg2 = "Order " + ord_id + " was successfully cancelled."
        if cancel_msg1 != cancel_msg2:
            raise AssertionError("Cancel order msg not equal")
    else:
        raise ApiException("Authorization Error: Please check API key.")


def test_orders(ses):
    response = ses.get(base_url + "/orders")
    if response.ok:
        order_json = response.json()
        orders_json1 = orders.orders_json(ses)
        orders_json2 = order_json
        if orders_json1 != orders_json2:
            raise AssertionError("Orders JSON not equal")

        orders_dict1 = orders.orders_dict(ses)
        orders_dict2 = {
            (orders.Order(ord)).order_id: orders.Order(ord) for ord in order_json
        }
        if orders_dict1 != orders_dict2:
            raise AssertionError("Orders dict not equal")

        for ord_id in orders_dict1:
            orders_obj1 = orders.order(ses, ord_id)
            orders_obj2 = orders.Order(order_json)
            if orders_obj1.__dict__ != orders_obj2.__dict__:
                raise AssertionError("Orders obj not equal")
    else:
        raise ApiException("Authorization Error: Please check API key.")


def test_securities_history(ses):
    response = ses.get(base_url + "/orders")
    ticker_sym = ""
    if response.ok:
        orders_dict1 = orders.orders_dict(ses)
        for ord_id in orders_dict1:
            ticker_sym = orders_dict1[ord_id].ticker
            break
    else:
        raise ApiException("Authorization Error: Please check API key.")

    payload = {"ticker": ticker_sym}
    response = ses.get(base_url + "/history", params=payload)
    if response.ok:
        sec_history_json = response.json()
        sec_history_json1 = sh.security_history_json(ses, ticker_sym)
        sec_history_json2 = sec_history
        if sec_history_json1 != sec_history_json2:
            raise AssertionError("Sec hist json not eq")

        sec_history_dict1 = sh.security_history_dict(ses, ticker_sym)
        sec_history_dict2 = {
            sh.Security_History(sec_hist).tick: sh.Security_History(sec_hist)
            for sec_hist in sec_history_json
        }
        if sec_history_dict1 != sec_history_dict2:
            raise AssertionError("Sec hist dict not eq")
    else:
        raise ApiException("Authorization Error: Please check API key.")


def test_securites(ses):
    response = ses.get(base_url + "/securities")
    if response.ok:
        sec_info_json = response.json()
        sec_json1 = securities.security_json(ses)
        sec_json2 = sec_info_json
        if sec_json1 != sec_json2:
            raise AssertionError("Security JSON not equal")

        sec_dict1 = securities.security_dict(ses)
        sec_dict2 = {
            (securities.Security(order)).ticker: securities.Security(order)
            for order in sec_info_json
        }
        if sec_dict1 != sec_dict2:
            raise AssertionError("Security dict not equal")
    else:
        raise ApiException("Authorization Error: Please check API key.")


def test_securities_book(ses):
    response = ses.get(base_url + "/orders")
    ticker_sym = ""
    if response.ok:
        orders_dict1 = orders.orders_dict(ses)
        for ord_id in orders_dict1:
            ticker_sym = orders_dict1[ord_id].ticker
            break
    else:
        raise ApiException("Authorization Error: Please check API key.")

    payload = {"ticker": ticker_sym}
    response = ses.get(base_url + "/securities/book", params=payload)
    if response.ok:
        sec_book = response.json()
        _side = "bids"
        _param = "price"
        sec_info1 = sb.get_security_info(ses, ticker_sym, _side, _param)
        sec_info2 = sec_book[_side][0][_param]
        if sec_info1 != sec_info2:
            raise AssertionError("Security info not equal")

        best_bid1 = sb.get_best_bid(ses, ticker_sym)
        best_bid2 = sec_book["bids"][0]
        if best_bid1 != best_bid2:
            raise AssertionError("Best bids not equal")

        best_ask1 = sb.get_best_ask(ses, ticker_sym)
        best_ask2 = sec_book["asks"][0]
        if best_ask1 != best_ask2:
            raise AssertionError("Best asks not equal")

        bbo1 = sb.get_bbo(ses, ticker_sym)
        bbo2 = {"best_bid": best_bid1, "best_ask": best_ask1}
        if bbo1 != bbo2:
            raise AssertionError("Best bid and offer not equal")

        all_bids1 = sb.get_all_bids(ses, ticker_sym)
        all_bids2 = sec_book["bids"]
        if all_bids1 != all_bids2:
            raise AssertionError("All bids not equal")

        all_asks1 = sb.get_all_asks(ses, ticker_sym)
        all_asks2 = sec_book["asks"]
        if all_asks1 != all_asks2:
            raise AssertionError("All asks not equal")

        all_ba1 = sb.get_all_bids_asks(ses, ticker_sym)
        all_ba2 = sec_book
        if all_ba1 != all_ba2:
            raise AssertionError("All bids/asks not equal")
    else:
        raise ApiException("Authorization Error: Please check API key.")


def main():
    with requests.Session() as ses:
        ses.headers.update(API_KEY)

        test_news(ses)
        test_assets(ses)
        test_orders(ses)
        test_traders(ses)
        test_tenders(ses)
        test_securites(ses)
        test_securities_book(ses)
        test_securities_history(ses)
        test_submit_cancel_orders(ses)


if __name__ == "__main__":
    main()
