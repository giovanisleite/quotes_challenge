import requests


API_URL = 'https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes/'


def get_quotes():
    response = requests.get(API_URL)
    return response.json()


def get_quote(quote_number):
    response = requests.get(f'{API_URL}{quote_number}')
    return response.json()
