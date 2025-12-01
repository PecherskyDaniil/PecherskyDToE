from .abstract_dto import abstract_dto


class unit_dto(abstract_dto):
    """
    Class for unit dto
    """
    __base_id:str = None
    __coef:int = 1
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
    