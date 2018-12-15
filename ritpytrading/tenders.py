'''
This script contains results for the /tenders module

Sample JSON output formats for the function returns
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
'''


# Make sure the RIT client uses the same 9999 port
host_url = 'http://localhost:9999'
base_path = '/v1'
base_url = host_url + base_path

# to print error messages and stop the program when needed


class ApiException(Exception):
    pass


class Tender():
    # case_response is a json obj returned from the API get request
    def __init__(self, tender_response):
        self.tender_id = tender_response["tender_id"]
        self.period = tender_response["period"]
        self.tick = tender_response["tick"]
        self.expires = tender_response["expires"]
        self.caption = tender_response["caption"]
        self.quantity = tender_response["quantity"]
        self.action = tender_response["action"]
        self.is_fixed_bid = tender_response["is_fixed_bid"]
        self.price = tender_response["price"]

    def __repr__(self):
        return self.tender_id + ' ' + self.caption

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

# function requires a requests.Session() object
# as the ses argument with a loaded API_KEY


def _get_tender_json(ses):

    response = ses.get(base_url + "/tenders")
    if response.ok:
        tenders_json = response.json()

        # returns all attributes of the news json response object
        return tenders_json
    raise ApiException('Authorization Error: Please check API key.')

# function to return a tenders_dict dict with Tender objects as values


def tender_response_handle(tenders_json):
    tenders_dict = {Tender(tender_obj).tender_id: Tender(tender_obj)
                    for tender_obj in tenders_json}

    return tenders_dict


# function requires a requests.Session() object
# as the ses argument with a loaded API_KEY
# price Required if the tender is not fixed-bid.

def _post_tender_response(ses, tender_id, price=None):
    payload = {}
    tender_id_parm = tender_id

    if price is not None:
        payload = {"price": price}

    response = ses.post(base_url + "/tenders/" +
                        str(tender_id_parm), params=payload)
    if response.ok:
        tenders_json = response.json()
        tenders_return = tenders_json["success"]
        if tenders_return:
            print("Tender was successfully accepted.")
        else:
            print("Tender was not accepted.")
    else:
        raise ApiException('Authorization Error: Please check API key.')

# function requires a requests.Session() object
# as the ses argument with a loaded API_KEY


def _delete_tender_response(ses, tender_id):

    tender_id_parm = tender_id

    response = ses.delete(base_url + "/tenders/{}").format(tender_id_parm)
    if response.ok:
        tenders_json = response.json()
        tenders_return = tenders_json["success"]
        if tenders_return:
            print("Tender was successfully declined.")
        else:
            print("Tender was not declined.")
    else:
        raise ApiException('Authorization Error: Please check API key.')


# function that returns the tender object
def tenders_dict(ses):
    return tender_response_handle(_get_tender_json(ses))

# returns a list of JSON fomratted output for tender object


def tenders_json(ses):
    return _get_tender_json(ses)


def accept_tender(ses, tender_iden, price_tender=None):
    tender_dict = tenders_dict(ses)
    if tender_dict[tender_iden].is_fixed_bid:
        _post_tender_response(ses, tender_iden, price=price_tender)
    # if the tender is not fixed bid, price must be supplied
    else:
        if price_tender is None:
            print("Price is required since tender is not fixed bid.")
        else:
            _post_tender_response(ses, tender_iden, price=price_tender)


def decline_tender(ses, tender_iden):
    _delete_tender_response(ses, tender_iden)
