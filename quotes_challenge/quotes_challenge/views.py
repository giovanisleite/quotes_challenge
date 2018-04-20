from pyramid.view import view_config
from pyramid.response import Response
from pyramid.view import notfound_view_config


@view_config(route_name='home')
def home_view(request):
    return Response('<h1>Desafio Web 1.0</h1>')


@notfound_view_config(renderer='../templates/404.jinja2')
def notfound_view(request):
    request.response.status = 404
    return {}
