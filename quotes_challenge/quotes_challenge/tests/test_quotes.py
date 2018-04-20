from requests_mock import mock

from ..quotes import API_URL, get_quotes, get_quote


def test_get_quotes():
    with mock() as m:
        data = {'quotes': ['zen'] * 19}
        m.get(API_URL, json=data)
        quotes = get_quotes()
    assert('quotes' in quotes)
    assert(len(quotes['quotes']) == len(data['quotes']))


def test_get_quote():
    with mock() as m:
        data = {'quote': 'Simple is better than complex'}
        m.get(f'{API_URL}2', json=data)
        quote = get_quote(2)
    assert(quote['quote'] == data['quote'])
