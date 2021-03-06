from .base import BaseClient
from . import logging_helper


ENGAGEMENTS_API_VERSION = '1'


class EngagementsClient(BaseClient):
    '''
    The hapipy Engagements client uses the _make_request method to call the API
    for data.  It returns a python object translated from the json return
    '''

    def __init__(self, *args, **kwargs):
        super(EngagementsClient, self).__init__(*args, **kwargs)
        self.log = logging_helper.get_log('hapi.engagements')

    def _get_path(self, subpath):
        return 'engagements/v%s/%s' % (self.options.get('version') or
                                       ENGAGEMENTS_API_VERSION, subpath)

    def create(self, data=None, **options):
        data = data or {}
        return self._call('engagements', data=data, method='POST', **options)

    def update(self, key, data=None, **options):
        data = data or {}
        return self._call('engagements/%s' % key, data=data,
                          method='PUT', **options)

    def get_all(self, **options):
        finished = False
        output = []
        querylimit = 250  # Max value according to docs
        offset = 0
        while not finished:
            batch = self._call(
                'engagements/paged', method='GET',
                params={'limit': querylimit, 'offset': offset}, **options
            )
            output.extend(batch['results'])
            finished = not batch['hasMore']
            offset = batch['offset']

        return output
