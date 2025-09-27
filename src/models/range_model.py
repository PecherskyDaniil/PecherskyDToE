
from .abstract_reference import *
from .unit_model import unit_model
from .range_group_model import range_group_model
class range_model(abstract_reference):
    __full_name:str=""
    __unit:unit_model=None
    __group:range_group_model=None
    def __init__(self,name:str,full_name:str,unit:unit_model,group:range_group_model):
        super().__init__(name)
        self._prop_validator=model_validator(self.__class__._prop_validator.limits+[limit_model("full_name",OperatorType.LE,255)])
        self.full_name=full_name
        self.unit=unit
        self.group=group

    #Наименование
    @property
    def full_name(self) -> str:
        return self.__full_name

    @full_name.setter
    def full_name(self, value:str):
        if value.strip()!="":
            self.__full_name = self._prop_validator.valid_property("full_name",value.strip())


    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, value:str):
        self.__unit = self._prop_validator.check_type(value,unit_model)
    

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, value:str):
        self.__group = self._prop_validator.check_type(value,range_group_model)
