from unittest.mock import patch

from . import BaseTest, dummy_request
from ..views import home_view, quotes_view, chosen_quote_view, random_quote_view
from ..models import User


class TestViews(BaseTest):
    def setUp(self):
        super(TestViews, self).setUp()
        self.init_database()

    def test_home_view(self):
        response = home_view(dummy_request(self.session))
        assert(response.status_int == 200)

    @patch('quotes_challenge.views.get_quotes')
    def test_quotes_view(self, get_quotes):
        get_quotes.return_value = {'quotes': 'python -m this'.split()}
        response = quotes_view(dummy_request(self.session))
        assert('quotes' in response)
        assert(isinstance(response.get('quotes'), list))

    @patch('quotes_challenge.views.get_quote')
    def test_valid_chosen_quote_view(self, get_quote):
        get_quote.return_value = {'quotes': 'Fly with the zen of python'}
        response = chosen_quote_view(dummy_request(self.session))
        assert('quotes' in response)
        assert(isinstance(response.get('quotes'), str))

    @patch('quotes_challenge.views.get_quote')
    def test_invalid_chosen_quote_view(self, get_quote):
        get_quote.side_effect = ValueError('The quote was not found')
        response = chosen_quote_view(dummy_request(self.session))
        assert(response.status_code == 404)
        assert(str(response) == 'The quote was not found')

    def test_register_session(self):
        request = dummy_request(self.session)
        home_view(request)
        assert('id' in request.session)

    def test_create_user(self):
        request = dummy_request(self.session)
        home_view(request)
        query = request.dbsession.query(User).filter_by(uuid=request.session['id'])
        assert(query.count() == 1)

    def test_register_accesses(self):
        request = dummy_request(self.session)
        home_view(request)
        quotes_view(request)
        random_quote_view(request)
        user = request.dbsession.query(User).filter_by(uuid=request.session['id']).one()
        assert(len(user.accesses) == 3)
