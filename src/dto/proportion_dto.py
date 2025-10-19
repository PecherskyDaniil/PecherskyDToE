from .abstract_dto import abstract_dto
class proportion_dto(abstract_dto):
    """
    Class for proportion dto
    """
    __range_id:str = ""
    __proportion_value:float=1.0

    @property
    def range_id(self) -> str:
        """
        Property range id
        """
        return self.__range_id

    @range_id.setter
    def range_id(self, value):
        """
        Setter for property range id
        """
        self.__range_id = value

    @property
    def proportion_value(self) -> int:
        """
        Property proportion value
        """
        return self.__proportion_value

    @proportion_value.setter
    def proportion_value(self, value):
        """
        Setter for property proportion value
        """
        self.__proportion_value = value

