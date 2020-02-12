import logging

from netsuitesdk.internal.utils import PaginatedSearch

from .base import ApiBase
from typing import List
from collections import OrderedDict

logger = logging.getLogger(__name__)

class Expenses(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='ExpenseReport')
    
    def get_all_generator(self):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='ExpenseReport', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction', recordType=record_type_search_field)
        paginated_search = PaginatedSearch(client=self.ns_client,
                                        type_name='Transaction',
                                        basic_search=basic_search,
                                        pageSize=20)
        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        assert data['externalId'], 'missing external id'
        vb = self.ns_client.Expenses(externalId=data['externalId'])
        res = self.ns_client.upsert(vb)
        return self._serialize(res)