from .abstract_dto import abstract_dto
from datetime import datetime 
class remnant_dto(abstract_dto):
    """
    Class for remnant dto
    """
    __range_id:str=""
    __unit_id:str=""
    __storage_id:str=""
    __datetime:datetime
    __remnant_value:float
    __name:str = ""
    __uuid:str = ""

    @property
    def name(self) ->str:
        """
        Property name
        """
        return self.__name
    
    @name.setter
    def name(self, value):
        """
        Setter for property name
        """
        self.__name = value

    @property
    def uuid(self) -> str:
        """
        Property id
        """
        return self.__uuid

    @uuid.setter
    def uuid(self, value):
        """
        Setter for property id
        """
        self.__uuid = value  
    @property
    def range_id(self):
        """
        Getter for range_id
        """
        return self.__range_id
    
    @range_id.setter
    def range_id(self,value:str):
        """
        Setter for range_id
        """
        self.__range_id=value

    @property
    def unit_id(self):
        """
        Getter for unit_id
        """
        return self.__unit_id
    
    @unit_id.setter
    def unit_id(self,value:str):
        """
        Setter for unit_id
        """
        self.__unit_id=value
    
    @property
    def storage_id(self):
        """
        Getter for unit_id
        """
        return self.__storage_id
    
    @storage_id.setter
    def storage_id(self,value:str):
        """
        Setter for unit_id
        """
        self.__storage_id=value
    
    @property
    def datetime(self):
        """
        Getter for datetime
        """
        return self.__datetime
    
    @datetime.setter
    def datetime(self,value):
        """
        Setter for datetime
        """
        self.__datetime=value
    
    @property
    def remnant_value(self):
        """
        Getter for remnant_value
        """
        return self.__remnant_value
    
    @remnant_value.setter
    def remnant_value(self,value:float):
        """
        Setter for datetime
        """
        self.__remnant_value=value
    


