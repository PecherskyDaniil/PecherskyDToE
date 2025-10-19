from .abstract_dto import abstract_dto


class unit_dto(abstract_dto):
    """
    Class for unit dto
    """
    __base_id:str = None
    __coef:int = 1

    @property
    def base_id(self) -> str:
        """
        Property base id
        """
        return self.__base_id    
    
    @base_id.setter
    def base_id(self, value):
        """
        Setter for property base id
        """
        self.__base_id = value

    @property
    def coef(self) -> int:
        """
        Property coef
        """
        return self.__coef    
    
    @coef.setter
    def coef(self, value):
        """
        Setter for property coef
        """
        self.__coef = value
    