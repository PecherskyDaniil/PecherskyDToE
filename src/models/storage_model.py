
from .abstract_reference import *
from ..dto.storage_dto import storage_dto
class storage_model(abstract_reference):
    """
    Class for work with storage. Inherited from abstract_reference
    """
    def __init__(self,name:str=None):
        """
        Constructor of class
        name - str
        """
        super().__init__(name)
    
    @staticmethod
    def from_dto(dto:storage_dto, cache:dict):
        """
        Function that convert instance from dto
        """
        model_validator.validate(dto, storage_dto)
        model_validator.validate(cache, dict)
        item=storage_model()
        item.uuid=dto.uuid
        item.name=dto.name
        return item

    def to_dto(self):
        """
        Function that convert instance to dto
        """
        item=storage_dto()
        item.name=self.name
        item.uuid=self.uuid
        return item