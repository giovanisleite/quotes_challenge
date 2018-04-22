from unittest.mock import patch

from . import BaseTest, dummy_request
from ..views.quotes import home, all_quotes, single_quote, random
from ..models import User


class TestViews(BaseTest):
    def setUp(self):
        super(TestViews, self).setUp()
        self.init_database()

    def test_home(self):
        response = home(dummy_request(self.session))
        assert(response.status_int == 200)

    @patch('quotes_challenge.views.quotes.get_quotes')
    def test_all_quotes(self, get_quotes):
        get_quotes.return_value = {'quotes': 'python -m this'.split()}
        response = all_quotes(dummy_request(self.session))
        assert('quotes' in response)
        assert(isinstance(response.get('quotes'), list))

    @patch('quotes_challenge.views.quotes.get_quote')
    def test_valid_single_quote(self, get_quote):
        get_quote.return_value = {'quotes': 'Fly with the zen of python'}
        response = single_quote(dummy_request(self.session))
        assert('quotes' in response)
        assert(isinstance(response.get('quotes'), str))

    @patch('quotes_challenge.views.quotes.get_quote')
    def test_invalid_single_quote(self, get_quote):
        get_quote.side_effect = ValueError('The quote was not found')
        response = single_quote(dummy_request(self.session))
        assert(response.status_code == 404)
        assert(str(response) == 'The quote was not found')

    def test_register_session(self):
        request = dummy_request(self.session)
        home(request)
        assert('id' in request.session)

    def test_create_user(self):
        request = dummy_request(self.session)
        home(request)
        query = request.dbsession.query(User).filter_by(uuid=request.session['id'])
        assert(query.count() == 1)

    def test_register_accesses(self):
        request = dummy_request(self.session)
        paths = ['/', '/quotes', '/quotes/random']
        views = [home, all_quotes, random]
        for path, view in zip(paths, views):
            request.path = path
            view(request)

        user = request.dbsession.query(User).filter_by(uuid=request.session['id']).one()
        assert(len(user.accesses) == 3)
        assert(paths == [access.page for access in user.accesses])
