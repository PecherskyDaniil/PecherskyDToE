
from .abstract_reference import *
from .unit_model import unit_model
from .range_group_model import range_group_model
class range_model(abstract_reference):
    """
    Class for work with range. Inherited from abstract_reference
    full_name - str : full name
    unit - unit_model: unit of range
    group - range_group_model : group of range
    """
    __full_name:str=""
    __unit:unit_model=None
    __group:range_group_model=None
    def __init__(self,name:str,full_name:str,unit:unit_model,group:range_group_model):
        """
        Constructor of class
        name - str
        full_name - str
        unit - unit_model
        group - range_group_model
        """
        super().__init__(name)
        self._prop_validator=model_validator(self.__class__._prop_validator.limits+[limit_model("full_name",Operator.LE,255)])
        self.full_name=full_name
        self.unit=unit
        self.group=group

    #Наименование
    @property
    def full_name(self) -> str:
        """
        Function that returns property full_name
        """
        return self.__full_name

    @full_name.setter
    def full_name(self, value:str):
        """
        Function that sets property full_name
        value - str
        """
        if self._prop_validator.valid_property("full_name",value):
            self.__full_name = value.strip()
        else:
            raise argument_exception("wrong length of full_name")


    @property
    def unit(self) -> str:
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
        if self._prop_validator.check_type(value,unit_model):
            self.__unit = value
        else:
            raise argument_exception("unit should be unit_model")
    

    @property
    def group(self) -> str:
        """
        Function that returns property group
        """
        return self.__group

    @group.setter
    def group(self, value:range_group_model):
        """
        Function that sets property group
        value - range_group_model
        """
        if self._prop_validator.check_type(value,range_group_model):
            self.__group = value
        else:
            raise argument_exception("group should be range_group_model")
