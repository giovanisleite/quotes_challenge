from pyramid.testing import DummyRequest
from unittest.mock import patch

from ..views import home_view, quotes_view, chosen_quote_view


def test_home_view():
    response = home_view(DummyRequest())
    assert(response.status_int == 200)


@patch('quotes_challenge.views.get_quotes')
def test_quotes_view(get_quotes):
    get_quotes.return_value = {'quotes': 'python -m this'.split()}
    response = quotes_view(DummyRequest())
    assert('quotes' in response)
    assert(isinstance(response.get('quotes'), list))


@patch('quotes_challenge.views.get_quote')
def test_valid_chosen_quote_view(get_quote):
    get_quote.return_value = {'quotes': 'Fly with the zen of python'}
    response = chosen_quote_view(DummyRequest())
    assert('quotes' in response)
    assert(isinstance(response.get('quotes'), str))


@patch('quotes_challenge.views.get_quote')
def test_invalid_chosen_quote_view(get_quote):
    get_quote.side_effect = ValueError('The quote was not found')
    response = chosen_quote_view(DummyRequest())
    assert(response.status_code == 404)
    assert(str(response) == 'The quote was not found')


def test_session():
    request = DummyRequest()
    home_view(request)
    assert('id' in request.session)
