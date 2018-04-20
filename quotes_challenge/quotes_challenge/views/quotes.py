from pyramid.view import view_config
from pyramid.response import Response


@view_config(route_name='home')
def home_view(request):
    return Response('<h1>Desafio Web 1.0</h1>')
