from pyramid.testing import DummyRequest
from unittest.mock import patch

from ..views import home_view, quotes_view


def test_home_view():
    response = home_view(DummyRequest())
    assert(response.status_int == 200)


@patch('quotes_challenge.views.get_quotes')
def test_quotes_view(get_quotes):
    get_quotes.return_value = {'quotes': 'python -m this'.split()}
    response = quotes_view(DummyRequest())
    assert('quotes' in response)
