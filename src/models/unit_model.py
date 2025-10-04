from .abstract_reference import *

from functools import lru_cache
class unit_model(abstract_reference):
    """
    Class for work with unit. Inherited from abstract_reference
    base_unit - None|unit_model: base unit of this unit
    coef - float : coef to count base unit
    """
    __base_unit=None
    __coef:float

    def __init__(self,name:str=None,base_unit=None,coef:float=1.0):
        """
        Constructor of class
        name - str
        base_unit - None|unit_model
        coef- float
        """
        super().__init__(name)
        self.base_unit=base_unit
        self.coef=coef

    @property
    def base_unit(self) -> str:
        """
        Function that returns property base_unit
        """
        return self.__base_unit

    @base_unit.setter
    def base_unit(self, value):
        """
        Function that sets property base_unit
        value - None|unit_model
        """
        if value is not None and not(self._prop_validator.check_type(value,unit_model)):
            raise argument_exception("base unit can be only None or unit_model")
        else:
            self.__base_unit = value

    @property
    def coef(self) -> str:
        """
        Function that returns property coef
        """
        return self.__coef

    @coef.setter
    def coef(self, value:float):
        """
        Function that sets property coef
        value - float
        """
        if self._prop_validator.check_type(value,float):
            self.__coef = value
        else:
            raise argument_exception("coef value can be only float")
    

    def __str__(self):
        """
        Magic function that return string type of object
        """
        return self.name
    
    def print_eq_coef(self):
        """
        Function that return string recount of unit
        """
        return f"1 {self.name} = {self.coef} {self.base_unit if self.base_unit is not None else '' }"
    
    @staticmethod
    @singleton_result
    def create_killogramm():
        """
        Creates default unit killogramm
        """
        inner_gramm=unit_model.create_gramm()
        item=unit_model.create("килограмм",inner_gramm,1000.0)
        return item
    
    @staticmethod
    @singleton_result
    def create_gramm():
        """
        Creates default unit gramm
        """
        item=unit_model.create("грамм",None,1.0)
        return item
    
    @staticmethod
    @singleton_result
    def create_litr():
        """
        Creates default unit litr
        """
        item=unit_model.create("литр",None,1.0)
        return item

    @staticmethod
    @singleton_result
    def create_millilitr():
        """
        Creates default unit millilitr
        """
        item=unit_model.create("миллилитр",unit_model.create_litr(),0.001)
        return item
    
    @staticmethod
    @singleton_result
    def create_item():
        """
        Creates default unit item
        """
        item=unit_model.create("штука",None,1.0)
        return item

    @staticmethod
    def create(name:str,base,coef:float):
        """
        Creates unit 
        name:str
        base:unit_model|None
        coef:float
        """
        item=unit_model(name,base,coef)
        return item