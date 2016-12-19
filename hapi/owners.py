from base import BaseClient
import logging_helper


class OwnersClient(BaseClient):
    '''The Owners Client uses the _make_request method to call the Hubspot API
    for data. It returns a python object translated from the json return '''
    def __init__(self, *args, **kwargs):
        super(OwnersClient, self).__init__(*args, **kwargs)
        self.log = logging_helper.get_log('hapi.owners')

    def _get_path(self, subpath):
        return 'owners/v2/%s' % subpath

    def get_all_owners(self, **options):
        '''Get list of all owners (users) '''
        return self._call('owners/', method='GET', **options)



