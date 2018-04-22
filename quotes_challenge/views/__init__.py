from datetime import datetime
from uuid import uuid1

from ..models import User, Access


def register_session(view):
    '''A decorator for views to register accesses'''
    def wrapper(request, *args, **kwargs):
        session = request.session
        if 'id' not in session:
            user = User(uuid=str(uuid1()))
            session['id'] = user.uuid
            request.dbsession.add(user)
        else:
            user = request.dbsession.query(User).filter_by(uuid=request.session['id']).one()
        access = Access(page=request.path, datetime=datetime.now(), user=user)
        request.dbsession.add(access)
        return view(request, *args, **kwargs)
    return wrapper
