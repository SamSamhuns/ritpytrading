# functions to handle response codes after
# making POST and GET requests with the RIT API


class ApiException(Exception):
    """ to print error messages and stop the program when needed """
    pass


def validate_response(response):
    status_code = response.status_code

    if status_code == 200:
        return True
    elif status_code == 401:
        raise ApiException('Authorization Error: Please check API key.')
    elif status_code == 403:
        raise ConnectionRefusedError('Connection refused by server: ' +
                                     'Please check if API and API order mode' +
                                     'is enabled in RIT Client')
    elif status_code == 429:
        print('Error submitting orders: Orders submitted too frequently.')
        return False

    raise ConnectionError()
