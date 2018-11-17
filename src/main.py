import requests
API_KEY = {'X-API-key':'H8KDL3Q6'}

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
