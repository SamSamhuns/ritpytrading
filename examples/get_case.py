import requests
# importing case related functions from case.py
from ritpytrading import cases
# import submit_cancel_orders to submit orders

API_KEY = {'X-API-key': 'TY0Y1KE9'}           # use your RIT API key here
# Make sure the RIT client uses the same 9999 port
# url is 'http://localhost:9999/v1'


def main():
    with requests.Session() as ses:
        ses.headers.update(API_KEY)

        current_case = cases.case(ses)
        current_case_json = cases.case_json(ses)
        current_case_lim = cases.case_limits(ses)
        tick = current_case.tick
        print(current_case_json)


if __name__ == "__main__":
    main()
