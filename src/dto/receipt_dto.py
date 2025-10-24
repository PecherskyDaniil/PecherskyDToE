from .abstract_dto import abstract_dto

class receipt_dto(abstract_dto):
    """
    Class for receipt dto
    """
    __steps:list[str] = []
    __ingridients:list[dict] = []
    __time:float = 0.0


    @property
    def steps(self) -> list:
        """
        Property steps
        """
        return self.__steps

    @steps.setter
    def steps(self, value:list):
        """
        Setter fo property steps
        """
        self.__steps = value
    
    @property
    def ingridients(self) -> list:
        """
        Property ingridients
        """
        return self.__ingridients

    @ingridients.setter
    def ingridients(self, value:list):
        """
        Setter fo property ingridients
        """
        self.__ingridients = value
    
    @property
    def time(self) -> float:
        """
        Property time
        """
        return self.__time

    @time.setter
    def time(self, value:float):
        """
        Setter fo property time
        """
        self.__time = value
    
