from random import randint

from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config
from pyramid.response import Response

from . import register_session
from ..quotes import get_quotes, get_quote


@view_config(route_name='home')
@register_session
def home(request):
    return Response('<h1>Desafio Web 1.0</h1>')


@view_config(route_name='quotes', renderer='templates/quotes.jinja2')
@register_session
def all_quotes(request):
    return get_quotes()


@view_config(route_name='chosen_quote', renderer='templates/quote.jinja2')
@register_session
def single_quote(request):
    quote_id = request.matchdict.get('choice')
    try:
        return get_quote(quote_id)
    except ValueError as value_error:
        return HTTPNotFound(value_error)


@view_config(route_name='random_quote', renderer='templates/quote.jinja2')
@register_session
def random(request):
    quotes = get_quotes().get('quotes')
    random = randint(0, len(quotes))
    return {'id': random, 'quote': quotes[random]}
