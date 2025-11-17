from ..models.abstract_reference import model_validator
from ..dto.filter_dto import filter_dto
from abc import ABC,abstractmethod
class prototype():
    """
    Class for prototype
    """
    __data:list=[]

    #@abstractmethod
    def __init__(self,data:list):
        """
        Constructor of class
        """
        self.data=data
    
    @property
    def data(self)->list:
        """
        Getter of data
        """
        return self.__data
    
    @data.setter
    def data(self,value:list):
        """
        Setter of data
        """
        model_validator.validate(value,list)
        self.__data=value
    
    def clone(self,data:list=None)->"prototype":
        """
        Function for clonning prototype data
        """
        inner_data=None
        if data is None:
            inner_data=self.data.copy()
        else:
            inner_data=data.copy()
        instance=prototype(inner_data)
        return instance

    def filter(prototype_obj:"prototype",filters:list[filter_dto]):
        """
        Function for filtering prototype data
        """
        model_validator.validate(prototype_obj,prototype)
        model_validator.validate(filters,list)
        result=[]
        for item in prototype_obj.data:
            is_valid=True
            for filter_obj in filters:
                model_validator.validate(filter_obj,filter_dto)
                if not(filter_obj.validate(item)):
                    is_valid=False
                    break
            if is_valid:
                result.append(item)
        return prototype_obj.clone(result)
    