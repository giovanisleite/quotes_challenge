from pyramid.view import view_config
from pyramid.response import Response
from pyramid.view import notfound_view_config

from .quotes import get_quotes, get_quote


@view_config(route_name='home')
def home_view(request):
    return Response('<h1>Desafio Web 1.0</h1>')


@view_config(route_name='quotes', renderer='templates/quotes.jinja2')
def quotes_view(request):
    return get_quotes()


@view_config(route_name='chosen_quote', renderer='templates/quote.jinja2')
def chosen_quote_view(request):
    quote_id = request.matchdict.get('choice')
    return get_quote(quote_id)


@notfound_view_config(renderer='templates/404.jinja2')
def notfound_view(request):
    request.response.status = 404
    return {}
