from datetime import datetime
from uuid import uuid1

from ..models import Session, Access


def register_session(view):
    '''A decorator for views to register accesses'''
    def wrapper(request, *args, **kwargs):
        if 'id' not in request.session:
            session = Session(uuid=str(uuid1()))
            request.session['id'] = session.uuid
            request.dbsession.add(session)
        else:
            session = request.dbsession.query(Session).get(request.session['id'])
        access = Access(page=request.path, datetime=datetime.now(), session=session)
        request.dbsession.add(access)
        return view(request, *args, **kwargs)
    return wrapper
