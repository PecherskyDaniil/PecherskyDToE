from .abstract_reference import *
from .company_model import company_model
from ..logics.abstract_response import abstract_response

class settings_model(abstract_reference):
    """
    Class for work with company settings. Inherited from abstract_reference
    company - company_model : company
    """
    __company:company_model=None
    __response_format:str
    __first_start:bool=None
    def __init__(self,name:str="settings"):
        """
        Constructor of class
        name - str ="settings
        """
        super().__init__(name)
        self.default()

    @property
    def response_format(self)->str:
        """
        Function that returns property response_format
        """
        return self.__response_format
    @response_format.setter
    def response_format(self,value:str):
        """
        Setter for property response_format
        """
        self.__response_format=value
    
    @property
    def first_start(self)->str:
        """
        Function that returns property first_start
        """
        return self.__first_start
    @first_start.setter
    def first_start(self,value:str):
        """
        Setter for property response_format
        """
        self.__first_start=value

    @property
    def company_settings(self)->company_model:
        """
        Function that returns property company_settings
        """
        return self.__company


    def default(self):
        """
        Function that creates company_model and sets it to property company
        """
        self.__company=company_model()