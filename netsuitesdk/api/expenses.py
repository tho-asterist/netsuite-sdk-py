from .base import ApiBase
import logging

logger = logging.getLogger(__name__)

class Expenses(ApiBase):
    """
    Expenses are not directly searchable - only via as transactions
    """
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Expenses')
    