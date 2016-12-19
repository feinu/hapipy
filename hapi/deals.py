from base import BaseClient
import logging_helper


DEALS_API_VERSION = '1'


class DealsClient(BaseClient):
    '''
    The hapipy Deals client uses the _make_request method to call the API
    for data.  It returns a python object translated from the json return
    '''

    def __init__(self, *args, **kwargs):
        super(DealsClient, self).__init__(*args, **kwargs)
        self.log = logging_helper.get_log('hapi.deals')

    def _get_path(self, subpath):
        return 'deals/v%s/%s' % (self.options.get('version') or
                                 DEALS_API_VERSION, subpath)

    def create(self, data=None, **options):
        data = data or {}
        return self._call('deal/', data=data, method='POST', **options)

    def update(self, key, data=None, **options):
        data = data or {}
        return self._call('deal/%s' % key, data=data,
                          method='PUT', **options)
