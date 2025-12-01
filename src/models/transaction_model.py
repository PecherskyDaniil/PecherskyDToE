
from ..core.abstract_reference import *
from datetime import datetime
from .range_model import range_model
from .storage_model import storage_model
from .unit_model import unit_model
from ..dto.transaction_dto import transaction_dto
from ..core.reposity_keys import reposity_keys
class transaction_model(abstract_reference):
    """
    Class for work with transactions. Inherited from abstract_reference
    """
    __datetime:datetime
    __range:range_model
    __storage:storage_model
    __amount:float
    __unit:unit_model

    def __init__(self):
        super().__init__(None)
    @property
    def datetime(self) -> datetime:
        """
        Function that returns property datetime
        """
        return self.__datetime

    @datetime.setter
    def datetime(self, value):
        """
        Function that sets property datetime
        value - datetime
        """
        self._prop_validator.validate(value,datetime)
        self.__datetime = value


    @property
    def range(self) -> range_model:
        """
        Function that returns property range
        """
        return self.__range

    @range.setter
    def range(self, value:range_model):
        """
        Function that sets property range
        value - range_model
        """
        model_validator.validate(value,range_model)
        self.__range = value

    

    @property
    def storage(self) -> storage_model:
        """
        Function that returns property storage
        """
        return self.__storage

    @storage.setter
    def storage(self, value:storage_model):
        """
        Function that sets property storage
        value - storage_model
        """
        model_validator.validate(value,storage_model)
        self.__storage = value

    @property
    def amount(self) -> float:
        """
        Function that returns property amount
        """
        return self.__amount

    @amount.setter
    def amount(self, value:float):
        """
        Function that sets property amount
        value - amount
        """
        self._prop_validator.validate(value,float)
        self.__amount = value

    @property
    def unit(self) -> unit_model:
        """
        Function that returns property unit
        """
        return self.__unit

    @unit.setter
    def unit(self, value:unit_model):
        """
        Function that sets property unit
        value - unit_model
        """
        self._prop_validator.validate(value,unit_model)
        self.__unit = value



    @staticmethod
    def create(name:str,range:range_model,storage:storage_model,amount:float,unit:unit_model):
        """
        Creates range 
        name:str
        range:range_model
        storage:storage_model
        amount:float
        unit:unit_model
        """
        item=transaction_model()
        item.name=name
        item.range=range
        item.storage=storage
        item.amount=amount
        item.unit=unit
        return item


    @staticmethod
    def from_dto(dto:transaction_dto, cache:dict):
        """
        Function that convert instance from dto
        """
        model_validator.validate(dto, transaction_dto)
        model_validator.validate(cache, dict)
        item=transaction_model()
        item.name=dto.name
        item.uuid=dto.uuid
        item.range=cache[reposity_keys.range_key()][ dto.range_id ] if dto.range_id in cache[reposity_keys.range_key()] else None
        item.storage=cache[reposity_keys.storage_key()][ dto.storage_id ] if dto.storage_id in cache[reposity_keys.storage_key()] else None
        item.amount=dto.amount
        item.unit=cache[reposity_keys.unit_key()][ dto.unit_id ] if dto.unit_id in cache[reposity_keys.unit_key()]  else None
        item.datetime=datetime.strptime(dto.datetime,"%Y-%m-%d %H:%M:%S")
        return item

    def to_dto(self):
        """
        Function that convert instance to dto
        """
        item=transaction_dto()
        item.name=self.name
        item.uuid=self.uuid
        item.range_id=self.range.uuid
        item.storage_id=self.storage.uuid
        item.amount=self.amount
        item.unit_id=self.unit.uuid
        if self.datetime is not None:
            item.datetime=self.datetime.strftime("%Y-%m-%d %H:%M:%S")
        else:
            item.datetime=None
        return item