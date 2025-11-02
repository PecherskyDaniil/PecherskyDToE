from .abstract_dto import abstract_dto
class storage_dto(abstract_dto):
    """
    Class for storage dto
    """
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
