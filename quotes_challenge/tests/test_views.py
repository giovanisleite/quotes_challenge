from pyramid.testing import DummyRequest
from ..views import home_view


def test_home():
    response = home_view(DummyRequest())
    assert(response.status_int == 200)
