# This script contains results for the /news module
#
# Sample JSON output formats for the function returns
# News object return value: JSON formatted
# [
#   {
#     "news_id": 0,
#     "period": 0,
#     "tick": 0,
#     "ticker": "string",
#     "headline": "string",
#     "body": "string"
#   }
# ]
# Parameters for the news GET HTTP request
# - since     number        (query)
# - limit     number        (query)

from ._response_validation import _validate_response

# Make sure the RIT client uses the same 9999 port
host_url = "http://localhost:9999"
base_path = "/v1"
base_url = host_url + base_path


class News:
    """case_response is a json obj returned from the API get request"""

    def __init__(self, news_response):
        self.news_id = news_response["news_id"]
        self.period = news_response["period"]
        self.tick = news_response["tick"]
        self.ticker = news_response["ticker"]
        self.headline = news_response["headline"]
        self.body = news_response["body"]

    def __repr__(self):
        return self.news_id + " " + self.headline

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


def _get_news_json(ses, since=None, limit=None):
    """function requires a requests.Session() object
    as the ses argument with a loaded API_KEY
    since = Retrieves only news items after a particular news id.
    limit = Result set limit, counts backwards from the most recent news item.
    Defaults to 20.
    """
    payload = {}
    if since is not None and limit is not None:
        payload = {"since": since, "limit": limit}
    elif since is not None:
        payload = {"since": since}
    elif limit is not None:
        payload = {"limit": limit}

    response = ses.get(base_url + "/news", params=payload)
    _validate_response(response)
    news_json = response.json()

    # returns all attributes of the news json response object
    return news_json


def _news_response_handle(news_json):
    news_dict = {News(news_obj).news_id: News(news_obj) for news_obj in news_json}

    return news_dict


def news_dict(ses, since_id=None, limit_itm=None):
    """function that returns the news object"""
    return _news_response_handle(_get_news_json(ses, since=since_id, limit=limit_itm))


def news_json(ses, since_id=None, limit_itm=None):
    """returns a list of JSON fomratted output for news object"""
    return _get_news_json(ses, since=since_id, limit=limit_itm)
