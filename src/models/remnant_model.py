from .abstract_reference import *
from ..dto.step_dto import step_dto
from ..models.range_model import range_model
from ..models.unit_model import unit_model
from ..models.storage_model import storage_model
from ..dto.remnant_dto import remnant_dto
import datetime

class remnant_model(abstract_reference):
    """
    Class that contain data of step of receipt's instruction 

    step_description:str - info about step
    """
    __range:range_model
    __unit:unit_model
    __storage:storage_model
    __datetime:datetime.datetime
    __remnant_value:float
    def __init__(self,name:str="remnant"):
        super().__init__(name)

    @property
    def range(self):
        """
        Function that returns range
        """
        return self.__range
    
    @range.setter
    def range(self,value:range_model):
        """
        Function that set range
        value:range_model
        """
        model_validator.validate(value,range_model)
        self.__range=value

    @property
    def unit(self):
        """
        Function that returns unit
        """
        return self.__unit
    
    @unit.setter
    def unit(self,value:unit_model):
        """
        Function that set unit
        value:unit_model
        """
        model_validator.validate(value,unit_model)
        self.__unit=value
    
    @property
    def storage(self):
        """
        Function that returns storage
        """
        return self.__storage
    
    @storage.setter
    def storage(self,value:storage_model):
        """
        Function that set storage
        value:storage_model
        """
        model_validator.validate(value,storage_model)
        self.__storage=value
    
    @property
    def datetime(self):
        """
        Function that returns datetime
        """
        return self.__datetime
    
    @datetime.setter
    def datetime(self,value):
        """
        Function that set storage
        value:storage_model
        """
        model_validator.validate(value,datetime.datetime)
        self.__datetime=value
    
    @property
    def remnant_value(self):
        """
        Function that returns value
        """
        return self.__remnant_value
    
    @remnant_value.setter
    def remnant_value(self,value:float):
        """
        Function that set float
        value:float
        """
        model_validator.validate(value,float)
        self.__remnant_value=value

    def create(range_obj:range_model,storage_obj:storage_model,unit_obj:unit_model,value_obj:float,datetime):
        """
        Fabric method for remnant_model
        """
        obj=remnant_model()
        obj.datetime=datetime
        obj.storage=storage_obj
        obj.unit=unit_obj
        obj.range=range_obj
        obj.remnant_value=value_obj
        return obj

    @staticmethod
    def from_dto(remnant_dto_obj:remnant_dto,cache:dict):
        """
        Function for converting remnant_dto to remnant_model
        """
        model_validator.validate(remnant_dto_obj, remnant_dto)
        model_validator.validate(cache, dict)
        unit_obj =  cache[ remnant_dto_obj.unit_id ] if remnant_dto_obj.unit_id in cache else None
        range_obj= cache[ remnant_dto_obj.range_id ] if remnant_dto_obj.range_id in cache else None
        storage_obj= cache[ remnant_dto_obj.storage_id ] if remnant_dto_obj.storage_id in cache else None
        remnant_model_obj=remnant_model.create(range_obj,storage_obj,unit_obj,remnant_dto_obj.remnant_value,remnant_dto_obj.datetime)
        return remnant_model_obj


    def to_dto(self):
        """
        Function that convert instance to dto
        """
        item=remnant_dto()
        item.name=self.name
        item.uuid=self.uuid
        item.range_id=self.range.uuid
        item.unit_id=self.unit.uuid
        item.storage_id=self.storage.uuid
        item.remnant_value=self.remnant_value
        item.datetime=self.datetime
        return item