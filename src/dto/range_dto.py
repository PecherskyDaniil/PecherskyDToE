from .abstract_dto import abstract_dto

class range_dto(abstract_dto):
    """
    Class for range dto
    """
    __full_name:str=""
    __unit_id:str = ""
    __group_id:str = ""

    @property
    def full_name(self):
        """
        Property full name
        """
        return self.__full_name
    
    @full_name.setter
    def full_name(self,value):
        """
        Setter for property full name
        """
        self.__full_name=value

    @property
    def unit_id(self) -> str:
        """
        Property unit id
        """
        return self.__unit_id

    @unit_id.setter
    def unit_id(self, value):
        """
        Setter for property unit id
        """
        self.__unit_id = value

    @property
    def group_id(self) -> str:
        """
        Property group id
        """
        return self.__group_id

    @group_id.setter
    def group_id(self, value):
        """
        Setter for property group id
        """
        self.__group_id = value

