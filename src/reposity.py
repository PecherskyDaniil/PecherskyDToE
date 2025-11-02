from .models.abstract_reference import abstract_reference
from .dto.receipt_dto import receipt_dto
from .dto.range_dto import range_dto
from .dto.unit_dto import unit_dto
from .dto.range_group_dto import range_group_dto
from .models.unit_model import unit_model
from .models.range_group_model import range_group_model
from .models.range_model import range_model
from .models.receipt_model import receipt_model
from .models.proportion import proportion
from .models.step import step

from .converters.convert_factory import convert_factory
class reposity:
    """
    Class that contains data of all system
    data:dict - dict of all data
    """
    __data:dict={}
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
    @staticmethod
    def unit_key():
        """
        Function that returns data key for units
        """
        return "unit_model"
    @staticmethod
    def range_group_key():
        """
        Function that returns data key for range_groups
        """
        return "range_group_model"
    @staticmethod
    def range_key():
        """
        Function that returns data key for ranges
        """
        return "range_model"
    @staticmethod
    def receipt_key():
        """
        Function that returns data key for receipts
        """
        return "receipt_model"
    
    @staticmethod
    def storage_key():
        """
        Function that returns data key for storages
        """
        return "storage_model"
    @staticmethod
    def transaction_key():
        """
        Function that returns data key for transactions
        """
        return "transaction_model"

    @staticmethod
    def unit_json_key():
        """
        Function that returns json key for units
        """
        return "units"
    
    @staticmethod
    def range_group_json_key():
        """
        Function that returns json key for range_groups
        """
        return "range_groups"
    @staticmethod
    def range_json_key():
        """
        Function that returns json key for ranges
        """
        return "ranges"
    @staticmethod
    def receipt_json_key():
        """
        Function that returns json key for receipts
        """
        return "receipts"

    @staticmethod
    def storage_json_key():
        """
        Function that returns data key for storages
        """
        return "storages"
    @staticmethod
    def transcation_json_key():
        """
        Function that returns data key for transactions
        """
        return "transactions"

    def __class_to_json(self,key:str):
        return convert_factory().convert(self.data[key])
    
    def to_json(self):
        """
        Function that convert reposity data to json
        """
        data={}
        data[reposity.receipt_json_key()]=self.__class_to_json(reposity.receipt_key())
        data[reposity.range_json_key()]=self.__class_to_json(reposity.range_key())
        data[reposity.unit_json_key()]=self.__class_to_json(reposity.unit_key())
        data[reposity.range_group_json_key()]=self.__class_to_json(reposity.range_group_key())
        data[reposity.storage_json_key()]=self.__class_to_json(reposity.storage_key())
        data[reposity.transcation_json_key()]=self.__class_to_json(reposity.transaction_key())
        return data