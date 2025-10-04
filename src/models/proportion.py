from .abstract_reference import *
from .range_model import range_model

class proportion():
    """
    Class that contains info about proportion
    range:range_model - range of proportion
    proportion_value:float - value of range proportion  
    """
    __range:range_model
    __proportion_value:float

    def __init__(self,range:range_model=None,proportion_value:float=1.0):
        """
        Constructor of class
        range:range_model
        proportion_value:float
        """
        self.range=range
        self.proportion_value=proportion_value


    @property
    def range(self):
        """
        Function that returns range
        """
        return self.__range
    
    @range.setter
    def range(self,value:range_model):
        """
        Function that sets property range
        value:range_model
        """
        if model_validator.check_type(value,range_model):
            self.__range=value
        else:
            raise argument_exception("range should be range_model type")
        
    @property
    def proportion_value(self):
        """
        Function that returns proportion_value
        """
        return self.__proportion_value
    
    @proportion_value.setter
    def proportion_value(self,value:float):
        """
        Function that sets property proportion_value
        value:float
        """
        if model_validator.check_type(value,float):
            self.__proportion_value=value
        else:
            raise argument_exception("proportion_value should be float type")
