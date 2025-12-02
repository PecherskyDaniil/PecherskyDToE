from .core.reposity_keys import reposity_keys
from .logics.unit_service import unit_service
from .logics.range_service import range_service
from .logics.range_group_service import range_group_service
from .logics.receipt_service import receipt_service
from .logics.transaction_service import transaction_service
from .logics.storage_service import storage_service
from .logics.remnant_service import remnant_service
class reposity:
    """
    Class that contains data of all system
    data:dict - dict of all data
    """
    __data:dict={} 
    def __init__(self):
        unit_service()
        range_service()
        range_group_service()
        receipt_service()
        transaction_service()
        storage_service()
        remnant_service()
    @property
    def data(self):
        """
        Function that returns data
        """
        return self.__data
    @data.setter
    def data(self,data:dict):
        """
        Function that sets property data
        value:dict
        """
        self.__data=data