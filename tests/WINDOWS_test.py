import requests
import unittest
from ritpytrading import news
from ritpytrading import cases
from ritpytrading import assets
from ritpytrading import orders
from ritpytrading import tenders
from ritpytrading import traders
from ritpytrading import securities
from ritpytrading import securities_book
from ritpytrading import securities_history
from ritpytrading import submit_cancel_orders

# THIS TEST IS DESIGNED FOR THE Liability Trading 3 Case File
API_KEY = {'X-API-key': 'TY0Y1KE9'}           # use your RIT API key here
# Make sure the RIT client uses the same 9999 port
# host_url = 'http://localhost:9999'
# base_path = '/v1'
# base_url = host_url + base_path

def test_assets(ses, ticker=None):
    response = ses.get('http://localhost:9999/v1/assets')
    if response.ok:
        assets_json = response.json()
        asset_list1 = assets.assets_list(ses)
        asset_list2 = assets_json
        if ticker is None:
            asset_dict1 = assets.assets_dict(ses)
            asset_dict2 = {assets.Asset(asset_obj).ticker: assets.Asset(asset_obj)
                           for asset_obj in assets_json}
        # if ticker sumbol is given
        elif ticker is not None:
            asset_obj1 = assets.asset(ses, ticker)
            asset_obj2 = assets.Asset(assets_json[0])

def test_cases(ses):
    response = ses.get('http://localhost:9999/v1/case')
    if response.ok:
        case_obj1 = cases.case(ses)
        case_json1 = cases.case_json(ses)

        case_obj2 = cases.Case(response.json())
        case_json2 = response.json()

        enforce = cases.trade_lim_enforce_chk(ses)

    response = ses.get('http://localhost:9999/v1/limits')
    if response.ok and enforce:
        limits_json = response.json()
        case_limit_obj1 = cases.case_limits(ses)
        case_limit_obj2 = cases.CaseLimits(limits_json[0])

        case_limit_json1 = cases.case_limits_json(ses)
        case_limit_json2 = limits_json

def test_news(ses):
    response = ses.get('http://localhost:9999/v1/news')
    if response.ok:
        news_json = response.json()
        news_dict1 = news.news_dict(ses)
        news_dict2 = {news.News(news_obj).news_id: news.News(news_obj)
                     for news_obj in news_json}

        news_list1 = news.news_json(ses)
        news_list2 = news_json

def test_traders(ses):
    response = ses.get('http://localhost:9999/v1/trader')
    if response.ok:
        trader_json = response.json()
        trader_obj1 = traders.trader(ses)
        trader_obj2 = traders.Trader(trader_json)

def test_tenders(ses):
    response = ses.get('http://localhost:9999/v1/tenders')
    if response.ok:
        pass
        
def main():
    with requests.Session() as ses:
        ses.headers.update(API_KEY)

        cobj = cases.case(ses)
        print(cobj.status)
        print(cobj.tick)

        response = ses.get('http://localhost:9999/v1/case')
        if response.ok:
            case = response.json()
            tick = case['tick']
            print('The case is on tick', tick)

if __name__ == "__main__":
    main()
