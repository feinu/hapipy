from base import BaseClient
import logging_helper


COMPANIES_API_VERSION = '2'


class CompaniesClient(BaseClient):
    '''
    The hapipy Companies client uses the _make_request method to call the API
    for data.  It returns a python object translated from the json return
    '''

    def __init__(self, *args, **kwargs):
        super(CompaniesClient, self).__init__(*args, **kwargs)
        self.log = logging_helper.get_log('hapi.companies')

    def _get_path(self, subpath):
        return 'companies/v%s/%s' % (self.options.get('version') or
                                     COMPANIES_API_VERSION, subpath)

    def create(self, data=None, **options):
        data = data or {}
        return self._call('companies/', data=data, method='POST', **options)

    def update(self, key, data=None, **options):
        data = data or {}
        return self._call('companies/%s' % key, data=data,
                          method='PUT', **options)
