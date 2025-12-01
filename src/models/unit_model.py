from ..core.abstract_reference import *
from ..dto.unit_dto import unit_dto
from ..core.reposity_keys import reposity_keys
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

    def get_base(self)->tuple:
        if self.base_unit is None:
            return (self.uuid,self.coef)
        else:
            base=self.base_unit.get_base()
            return (base[0],self.coef*base[1])

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
    
    @staticmethod
    def from_dto(dto:unit_dto, cache:dict):
        """
        Function that creates instance from dto object
        """
        model_validator.validate(dto, unit_dto)
        model_validator.validate(cache, dict)
        base_unit =  cache[reposity_keys.unit_key()][ dto.base_id ] if dto.base_id in cache[reposity_keys.unit_key()] else None
        item  = unit_model.create(dto.name, base_unit, dto.coef)
        item.uuid=dto.uuid
        return item
    
    def to_dto(self):
        """
        Function that convert instance to dto
        """
        item=unit_dto()
        item.name=self.name
        item.uuid=self.uuid
        if self.base_unit is not None:
            item.base_id=self.base_unit.uuid
        else:
            item.base_id=self.base_unit
        item.coef=self.coef
        return item