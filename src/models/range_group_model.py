from .abstract_reference import *
from ..dto.range_group_dto import range_group_dto
class range_group_model(abstract_reference):
    """
    Class for work with range groups. Inherited from abstract_reference
    """

    def __init__(self,name:str=None):
        """
        Constructor of class
        name - str
        """
        super().__init__(name)

    @staticmethod
    def create(name):
        return range_group_model(name)

    @staticmethod
    def from_dto(dto:range_group_dto, cache:dict):
        """
        Function that creates instance from dto object
        """
        model_validator.validate(dto, range_group_dto)
        model_validator.validate(cache, dict)
        item  = range_group_model.create(dto.name)
        item.uuid=dto.uuid
        return item
    
    def to_dto(model:"range_group_model"):
        """
        Function that convert instance to dto
        """
        item=range_group_dto()
        item.name=model.name
        item.uuid=model.uuid
        return item
   
