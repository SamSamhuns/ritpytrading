# This program demonstrates the use of the RIT API
# without using the ritpytrading module

import requests
API_KEY = {'X-API-key': 'TY0Y1KE9'}

def main():
    with requests.Session() as s:
        s.headers.update(API_KEY)
        mkt_buy_params = {'ticker': 'CRZY', 'type': 'MARKET', 'quantity': 1000,
        'action': 'BUY'}
        resp = s.post('http://localhost:9999/v1/orders', params=mkt_buy_params)
        if resp.ok:
            mkt_order = resp.json()
            id = mkt_order['order_id']
            print('The market buy order was submitted and has ID', id)
        else:
            print(resp)
            print('The order was not successfully submitted!')

if __name__ == "__main__":
    main()
