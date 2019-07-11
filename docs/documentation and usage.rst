Documentation and Usage
=======================

To use ritpytrading in a project:

::

   import ritpytrading

Documentation for each sub-package inside ritpytrading
------------------------------------------------------

-  `Getting Started <#getting-started>`__

-  `assets <#assets>`__

-  `cases <#cases>`__

-  `news <#news>`__

-  `orders <#orders>`__

-  `securities_book <#securities_book>`__

-  `securities_history <#securities_history>`__

-  `securities <#securities>`__

-  `submit_cancel_orders <#submit_cancel_orders>`__

-  `tenders <#tenders>`__

-  `traders <#traders>`__

Getting Started
~~~~~~~~~~~~~~~

The ``requests`` library must be imported at the begininng for each
session. Then the proper RIT REST API key must be set in a python
dictionary. The base URL should also be set to the localhost.

::

    import requests
    import ritpytrading

    API_KEY = {'X-API-key': 'TY0Y1KE9'}    # use your RIT API key here
    host_url = 'http://localhost:9999'     # Make sure the RIT client uses the same port
    base_path = '/v1'
    base_url = host_url + base_path

Then each ritpytrading library package call must be done inside a
Session context handler as follows:

::

   with requests.Session() as ses:
       ses.headers.update(API_KEY)                 # set the API key for the session
       current_case = ritpytrading.case.case(ses)  # create a CASE object as an example

Note: All JSON formats for the objects created by each of the following
modules are provided `here. <#all-json-formats>`__

assets
~~~~~~

::

   assets.asset(ses, ticker_symbol)
   assets.assets_list(ses)
   assets.assets_dict(ses)

Creates single assets objects, list or dictionary of asset objects. Full
``assets object`` JSON format `here <#cases-object>`__.

Import with:

::

   from ritpytrading import assets
   with requests.Session() as ses:
       ses.headers.update(API_KEY)

-  To create a single asset object:

   ::

      apple_asset = assets.asset(ses, 'AAPL')
      print(apple_asset.start_period)         # prints the APPL asset start period

-  To create a dictionary of asset objects with the ticker symbol as
   keys: (Assuming ``APPL`` and ``HOG`` assets exist in the current RIT
   server session):

   ::

      asset_dict = assets.assets_dict(ses)
      print(asset_dict)                      # prints a dict of all avialable assets
      print(asset_dict['AAPL'].start_period) # prints the APPL asset start period
      print(asset_dict['HOG'].start_period)  # prints the HOG asset start period

-  To create a python list of asset objects: (Assuming the first and
   second assets exits in the current RIT server session):

   ::

      asset_list = assets.assets_list(ses)
      print(asset_list)                  # prints a list of all avialable assets
      print(asset_list[0].start_period)  # prints the first asset start period
      print(asset_list[1].start_period)  # prints the second asset start period

cases
~~~~~

::

   cases.case(ses), cases.case_json(ses
   cases.trade_lim_enforce_chk(ses)
   cases.case_limits(ses)
   case_limits_json(ses)

Creates case and case_limit objects and checks if the current case has
case limits. Full cases object JSON format `here <#cases-object>`__.

Import with:

::

   from ritpytrading import cases
   with requests.Session() as ses:
       ses.headers.update(API_KEY)

-  To create a case object of the given trading session:

   ::

      current_case = cases.case(ses)
      print(current_case.name)         # prints name of current case

-  To create a case JSON object of the given trading session:

   ::

      current_case_json = cases.case_json(ses)
      print(current_case_json['name']) # prints name of current case

-  To check if there is enforcement of the trading limits:

   ::

      hasTradeLim = cases.trade_lim_enforce_chk(ses) # returns a boolean

-  To create a case limits object of the given trading session: (Given
   that a trading limit exists in the first place)

   ::

      current_case_limit = cases.case_limits(ses)
      print(current_case_limit.gross_limit)          # prints the gross limit for the current case

-  To create a case limits JSON object of the given trading session:
   (Given that a trading limit exists in the first place)

   ::

      current_case_limit_json = cases.case_limits_json(ses)
      print(current_case_limit[0]['gross_limit'])     # prints the gross limit for the current case

news
~~~~

::

   news.news_dict(ses, since_id=None, limit_itm=None)
   news.news_json(ses, since_id=None, limit_itm=None)

   # since = Retrieves only news items after a particular news id.
   # limit = Result set limit, counts backwards from the most recent news item.
   # Defaults to 20.

Creates a python dictionary or a list of json objects of the all the
news events in the given trading session. Full news object JSON
available `here <#news-object>`__.

Import with:

::

   from ritpytrading import news
   with requests.Session() as ses:
       ses.headers.update(API_KEY)

-  To create a dictionary of news objects with the news_ids as the
   dictionary keys:

   ::

      all_news_dict = news.news_dict(ses)
      print(all_news_dict)        # prints all the news objects repr by their ids
      print(all_news_dict['24'])  # prints the id number and headline of the news object with id 24

-  To create a list of json news objects:

   ::

      all_news_list = news.news_json(ses)
      print(all_news_list[0]['news_id'])  # prints the news id of the 0th element in the list of json objects

orders
~~~~~~

::

   orders.order(ses, orderId, status='OPEN')
   orders.orders_json(ses, status='OPEN')
   orders.orders_dict(ses, status='OPEN')

   # status can be OPEN, TRANSACTED or CLOSED
   # status OPEN by default

Creates a submitted OPEN/CLOSED order object given its orderID. Creates
a dictionary or a list of JSON objects of all OPEN/CLOSED orders. Full
orders object JSON available `here <#orders-object>`__.

Import with:

::

   from ritpytrading import orders
   with requests.Session() as ses:
       ses.headers.update(API_KEY)

-  To create an OPEN/CLOSED order object given its orderID:

   ::

      order_1 = orders.order(ses, orderID, 'OPEN')
      print(order_1.quantity)       # prints quantity of order with ID orderID

-  To create a list of all JSON formatted order objects in the given
   session:

   ::

      all_orders_json = orders.orders_json(ses, 'CLOSED')
      print(all_orders_json[0])     # prints qty, price, order id information of the first closed order in this session

-  To create a dictionary of all order objects with the order ids as
   keys in the given session:

   ::

      all_orders_dict = orders.orders_dict(ses, 'OPEN')
      print(all_orders_dict[orderID]) # prints qty, price, order id information of the order with ID orderID in this session

securities_book
~~~~~~~~~~~~~~~

::

   get_security_info(ses, ticker_sym, side, param)
   get_best_bid(ses, ticker_sym)
   get_best_ask(ses, ticker_sym)
   get_bbo(ses, ticker_sym)
   get_all_bids(ses, ticker_sym)
   get_all_asks(ses, ticker_sym)
   get_all_bids_asks(ses, ticker_sym)

   # All responses will be JSON objects or list of JSON objects as provided [here](#securities_book-object).

Gets the bets bid, ask prices and creates bid/ask price objects. Full
securities_book object JSON available
`here <#securities_book-object>`__.

Import with:

::

   from ritpytrading import securities_book
   with requests.Session() as ses:
       ses.headers.update(API_KEY)

-  To get information (i.e. quantity, price, status) on a particular
   security.

   ``side = bids / asks``

   All possible values for the ``param`` parameter are listed in the
   JSON information list for securities_book
   `here <#securities_book-object>`__. i.e. param = “trader_id”

   ::

      # returns the quantity filled of AAPL asset on the buy/bid side
      apple_info = securities_book.get_security_info(ses, "AAPL", "bids", "quantity_filled")

-  To get the best bid price on a security given the ticker symbol:

   ::

      best_bid_aapl = securities_book.get_best_bid(ses, 'AAPL')
      print(best_bid_aapl['vwap'])     # prints vwap of AAPL's best bid

-  To get the best ask price on a security given the ticker symbol:

   ::

      best_ask_aapl = securities_book.get_best_ask(ses, 'AAPL')
      print(best_ask_aapl['quantity']) # prints the quantity being offered to be sold for APPL's best ask

-  To get the best bid and ask price in dict format for given the ticker
   symbol:

   ::

      hog_bbo = securities_book.get_bbo(ses, 'HOG')
      print(hog_bbo['best_bid']['quantity'])        # prints the quantity of the HOG best bid
      print(hog_bbo['best_ask']['quantity_filled']) # prints the filled quantiy of the HOG best ask

-  To get all the bid objects as a list of JSON objects for a security
   given the ticker symbol: (Note;

   ::

      all_aapl_bids = securities_book.get_all_bids(ses, 'AAPL')
      print(all_aapl_bids[0]['quantiy'])            # prints the quantity of the 0th AAPL bid in the bid list

-  To get all the ask objects as a list of JSON objects for a security
   given the ticker symbol:

   ::

      all_aapl_asks = securities_book.get_all_asks(ses, 'AAPL')
      print(all_aapl_asks[0]['quantiy'])            # prints the quantity of the 0th AAPL ask in the ask list

-  To get all the bid and ask objects as a JSON format present
   `here <#securities_book-object>`__, given the ticker symbol:

   ::

      all_aapl_bid_ask = securities_book.get_all_bids_asks(ses, 'AAPL')
      print(all_aapl_bid_ask['bids'][0]['type'])    # prints the type(LIMIT/MARKET) of the 0th bid order in the bids list for AAPL
      print(all_aapl_bid_ask['asks'][1]['price'])   # prints the price of the 1st ask order in the asks list for AAPL

securities_history
~~~~~~~~~~~~~~~~~~

::

   security_history_dict(ses, ticker_sym, period_numb=None, lim_numb=None)
   security_history_json(ses, ticker_sym, period_numb=None, lim_numb=None)

   # period_num is the period to retrive data from. Defaults to current period.
   # lim_num = Result set limit, counting backwards from the most recent tick. Defaults to retrieving the entire period.

Creates a dictionary of security history objects or a list of JSON
security history objects. Full securities_history object JSON available
`here <#securities_history-object>`__.

Import with:

::

   from ritpytrading import securities_history
   with requests.Session() as ses:
       ses.headers.update(API_KEY)

-  To create a dictionary of security history objects with the security
   ``ticks`` as their keys.

   ::

      aapl_hist_dict = securities_history.security_history_dict(ses, 'AAPL')
      print(aapl_hist_dict['22'].open)       # prints the open price for the APPL security at the time tick 22

-  To create a list fo JSON security history objects

   ::

      aapl_hist_json_list =securities_history.security_history_json(ses, 'AAPL')
      print(aapl_hist_json_list[0]['close']) # prints the close price for the 0th AAPL security history object

securities
~~~~~~~~~~

::

   security_dict(ses, ticker_sym=None) # By default no specific ticker_sym is None returns the list of available securities as a dict of security objects with ticker name as keys
   security_json(ses, ticker_sym=None) # returns the list of available securities with all info in a json format

Creates a dictionary of security objects or a list of JSON security
objects. Full securities object JSON available
`here <#securities-object>`__.

Import with:

::

   from ritpytrading import securities
   with requests.Session() as ses:
       ses.headers.update(API_KEY)

-  To create a security object if the ticker symbol is given or return a
   dict with all the available securities with the ticker symbol as the
   keys:

   ::

      aapl_sec_dict = securities.security_dict(ses, 'AAPL')  # returns the AAPL security object
      all_sec_dict = securities.security_dict(ses)           # returns a dict of all security objects
      print(aapl_sec_dict.currency)                          # prints currency of AAPL security in given session
      print(all_sec_dict['HOG'].total_volume)                # prints total trading volume of HOG security given that it is present in the given server session

-  To create a list of security objects in a JSON format as given
   `here <#securities-object>`__.

   ::

      aapl_sec_json =  security_json(ses, ticker_sym='AAPL') # returns a JSON AAPL security object
      all_sec_json = security_json(ses)                      # returns all securities as a list of JSON objects
      print(aapl_sec_json['ask_size'])                       # prints the ask_size of AAPL security in given session
      print(all_sec_json[0]['total_volume'])                 # prints the total volume of the 0th security in the security json list in the given session

submit_cancel_orders
~~~~~~~~~~~~~~~~~~~~

::

   market_order(ses, ticker, side, quantity)
   limit_order(ses, ticker, side, quantity, price)
   cancel_order(ses, order_id)
   cancel_order_bulk(ses, price_direc, price_lim, volume_direc, volume_lim, all_flag=0)

Creates a market or a limit order given the ticker, side, quantity
and/or price. Cancels an order given the orderID. Cancels orders in
bulk.

For function call ``cancel_order_bulk(...)``: Volume < 0 for cancelling
all open sell orders and Volume > 0 for cancelling all open buy orders.
Query example ‘Price < 20.0 AND Volume > 0’ equivalent to
``submit_cancel_orders.cancel_order_bulk(ses, '<', 20.0, '>', 0)``.

Import with:

::

   from ritpytrading import submit_cancel_orders
   with requests.Session() as ses:
       ses.headers.update(API_KEY)

-  To make a market_order:

   ::

      submit_cancel_orders.market_order(ses, 'AAPL', 'BUY', 400) # market order for buying 400 AAPL shares
      submit_cancel_orders.market_order(ses, 'HOG', 'SELL', 300) # market order for selling 300 HOG shares

-  To make a limit_order:

   ::

      submit_cancel_orders.limit_order(ses, 'GOOGL', 'BUY', 500, 900)   # limit order for buying 500 GOOGL shares limit 900 per share
      submit_cancel_orders.limit_order(ses, 'GOOGL', 'SELL', 200, 1000) # limit order for selling 200 GOOGL shares limit 1000 per share

-  To cancel a given order:

   ::

      submit_cancel_orders.cancel_order(ses, '6') # Cancel the order with ID 6

-  To cancel orders in bulk:

   ::

      # cancel_order_bulk(ses, price_direc, price_lim, volume_direc, volume_lim, all_flag=0)
      # if all_flag = 1 then all open orders are cancelled
      # set all_flag = 0 to cancel only select orders
      # By default all_flag is set to 0
      # Volume < 0 for cancelling all open sell orders and Volume > 0
      # for cancelling all open buy orders
      # Query generation example 'Price < 20.0 AND Volume > 0'

      submit_cancel_orders.cancel_order_bulk(ses, '<', 20.0, '>', 0) # cancel all orders less than 20.0 in price and greater than 0 in volume
      submit_cancel_orders.cancel_all_open_orders(ses)               # cancels all open orders

tenders
~~~~~~~

::

   tenders_dict(ses)
   tenders_json(ses)
   is_tender_fixed_bid(ses, tender_iden)
   accept_tender(ses, tender_iden, price_tender=None)
   decline_tender(ses, tender_iden)

Creates a dictionary of Tender objects or a list of JSON Tender objects.
Can call functions to accept or decline tenders based on the tender ID.
Full tenders object JSON available `here <#tenders-object>`__.

Import with:

::

   from ritpytrading import tenders
   with requests.Session() as ses:
       ses.headers.update(API_KEY)

-  To create a dictionary of Tender objects with the Tender IDs as the
   keys in the current session:

   ::

      cur_tender_dict = tenders.tenders_dict(ses)
      print(cur_tender_dict['5'].caption)    # prints the caption of the Tender with Tender ID 5

-  To create a list of JSON formatted tender objects in the current
   session:

   ::

      cur_tender_json = tenders.tenders_json(ses)
      print(cur_tender_json[0]['price'])                 # gets the price of the 0th Tender in the Tender list

-  To check if a Tender is fixed bid given its Tender ID:

   ::

      is_5_fixed = tenders.is_tender_fixed_bid(ses, '5') # Checks if the tender with ID 5 is fixed bid

-  To accept a Tender with its Tender ID: (If the Tender is not fixed
   bid, a price_tender must be specified)

   ::

      tenders.accept_tender(ses, '5') if is_5_fixed else print("Tender is not fixed bid")   # accept the tender with ID 5 given the Tender is fixed bid
      tenders.accept_tender(ses, '7', 5000)                                                 # attempt to accept the tender with ID 7 with a bid of 5000

-  To decline a Tender with its Tender ID

   ::

      tenders.decline_tender(ses, '3')                   # decline the tender with ID 3

traders
~~~~~~~

::

   traders.trader(ses)

Creates a Trader object. Full traders object JSON available
`here <#traders-object>`__.

Import with:

::

   from ritpytrading import traders
   with requests.Session() as ses:
       ses.headers.update(API_KEY)

-  To create the trader object for the current session:

   ::

      cur_trader = traders.trader(ses)
      print(cur_trader.trader_id)       # prints the trader id of the current trader

All JSON formats
^^^^^^^^^^^^^^^^

``assets object``
'''''''''''''''''

::

   Asset object return value: JSON formatted
   {
       "ticker": "string",
       "type": "CONTAINER",
       "description": "string",
       "total_quantity": 0,
       "available_quantity": 0,
       "lease_price": 0,
       "convert_from": [
           {
               "ticker": "string",
               "quantity": 0
           }
       ],
       "convert_to": [
           {
               "ticker": "string",
               "quantity": 0
           }
       ],
       "containment": {
           "ticker": "string",
           "quantity": 0
       },
       "ticks_per_conversion": 0,
       "ticks_per_lease": 0,
       "is_available": true,
       "start_period": 0,
       "stop_period": 0
   }

``cases object``
''''''''''''''''

::

   Case object return value: JSON formatted
   {
       "name": "string",
       "period": 0,
       "tick": 0,
       "ticks_per_period": 0,
       "total_periods": 0,
       "status": "ACTIVE",
       "is_enforce_trading_limits": True
   }
   Limits object return values: JSON formatted
   Returned as a list containing a JSON object
   [
       {
           "name": "string",
           "gross": 0,
           "net": 0,
           "gross_limit": 0,
           "net_limit": 0,
           "gross_fine": 0,
           "net_fine": 0
       }
   ]

``news object``
'''''''''''''''

::

   Sample JSON output formats for the function returns
   News object return value: JSON formatted
   [
     {
       "news_id": 0,
       "period": 0,
       "tick": 0,
       "ticker": "string",
       "headline": "string",
       "body": "string"
     }
   ]

``orders object``
'''''''''''''''''

::

   Order object return value: JSON formatted
   param possible order attributes: JSON formatted
   i.e. get_order_response( ses, url_end, param="order_id" )
   {
       "order_id": 1221,
       "period": 1,
       "tick": 10,
       "trader_id": "trader49",
       "ticker": "CRZY",
       "type": "LIMIT",
       "quantity": 100,
       "action": "BUY",
       "price": 14.21,
       "quantity_filled": 10,
       "vwap": 14.21,
       "status": "OPEN"
   }

``securities_book object``
''''''''''''''''''''''''''

::

   securities_book object attribute values: JSON formatted
   {
     "bids": [
       {
         "order_id": 1221,
         "period": 1,
         "tick": 10,
         "trader_id": "trader49",
         "ticker": "CRZY",
         "type": "LIMIT",
         "quantity": 100,
         "action": "BUY",
         "price": 14.21,
         "quantity_filled": 10,
         "vwap": 14.21,
         "status": "OPEN"
       }
     ],
     "asks": [
       {
         "order_id": 1221,
         "period": 1,
         "tick": 10,
         "trader_id": "trader49",
         "ticker": "CRZY",
         "type": "LIMIT",
         "quantity": 100,
         "action": "BUY",
         "price": 14.21,
         "quantity_filled": 10,
         "vwap": 14.21,
         "status": "OPEN"
       }
     ]
   }

``securities_history object``
'''''''''''''''''''''''''''''

::

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

``securities object``
'''''''''''''''''''''

::

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

``submit_cancel_orders object``
'''''''''''''''''''''''''''''''

::

   No JSON format present

``tenders object``
''''''''''''''''''

::

   Tender object return value: JSON formatted
   [
     {
       "tender_id": 0,
       "period": 0,
       "tick": 0,
       "expires": 0,
       "caption": "string",
       "quantity": 0,
       "action": "BUY",
       "is_fixed_bid": true,
       "price": 0
     }
   ]

``traders object``
''''''''''''''''''

::

   trader object return value: JSON formatted
   {
     "trader_id": "string",
     "first_name": "string",
     "last_name": "string",
     "nlv": 0
   }
