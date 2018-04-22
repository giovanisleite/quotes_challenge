from cornice import Service
from cornice.resource import resource

from ..models import Session


@resource(collection_path='/sessions', path='/sessions/{uuid}')
class SessionView:

    def __init__(self, request, *args, **kwargs):
        self.request = request

    def collection_get(self):
        return {'sessions': [session.uuid for session in self.request.dbsession.query(Session)]}

    def collection_post(self):
        session = Session.from_json(self.request.json)
        self.request.dbsession.add(session)
        return {'session': session}

    def get(self):
        session = self.request.dbsession.query(Session).get(self.request.matchdict.get('uuid'))
        if not session:
            self.request.response.status = 400
            return {'error': 'Not found'}
        return {'session': session}

    def put(self):
        self.request.dbsession.query(Session) \
            .filter_by(uuid=self.request.matchdict.get('uuid')) \
            .update(self.request.json)

        return {'sessions': [session.uuid for session in self.request.dbsession.query(Session)]}

    def delete(self):
        session = self.request.dbsession.query(Session).get(self.request.matchdict.get('uuid'))
        if not session:
            self.request.response.status = 400
            return {'error': 'Not found'}
        self.request.dbsession.delete(session)
        return {'session': session}
