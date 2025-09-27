from .abstract_reference import *
class unit_model(abstract_reference):
    __base_unit=None
    __coef=1


    def __init__(self,name:str,base_unit,coef:float):
        super().__init__(name)
        self.__base_unit=base_unit
        self.coef=coef

    @property
    def base_unit(self) -> str:
        return self.__base_unit

    @base_unit.setter
    def base_unit(self, value):
        self.__base_unit = value

    @property
    def coef(self) -> str:
        return self.__coef

    @coef.setter
    def coef(self, value:float):
        self.__coef = self._prop_validator.check_type(value,int)
    

    def __str__(self):
        return self.name
    def print_eq_coef(self):
        return f"1 {self.name} = {self.coef} {self.base_unit if self.base_unit is not None else '' }"