# This program demonstrates the use of the RIT API
# without using the ritpytrading module

import requests

API_KEY = {"X-API-key": "TY0Y1KE9"}  # use your RIT API key here


# Make sure the RIT client uses the same 9999 port
# url is 'http://localhost:9999/v1'


def main():
    with requests.Session() as ses:
        ses.headers.update(API_KEY)
        response = ses.get("http://localhost:9999/v1/case")
        if response.ok:
            case = response.json()
            tick = case["tick"]
            print("The case is on tick", tick)


if __name__ == "__main__":
    main()
