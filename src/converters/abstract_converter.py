from abc import ABC,abstractmethod
class abstract_converter(ABC):
    """
    Abstract class for converters
    """
    @abstractmethod
    def __init__(self):
        """
        Constructor of class
        """
        pass

    @abstractmethod
    def convert(self,obj:any):
        """
        Function that converts object data to dict
        """
        pass
