from ..core.abstract_reference import *
from ..core.log_levels import log_levels
from .company_model import company_model
from ..logics.abstract_response import abstract_response
import datetime

class settings_model(abstract_reference):
    """
    Class for work with company settings. Inherited from abstract_reference
    company - company_model : company
    """
    __company:company_model=None
    __response_format:str
    __first_start:bool=None
    __block_datetime:datetime.datetime=None
    __log_level:str=None
    __log_dir:str=None
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


    @property
    def block_datetime(self)->str:
        """
        Function that returns property block_datetime
        """
        return self.__block_datetime
    @block_datetime.setter
    def block_datetime(self,value:datetime.datetime):
        """
        Setter for property block_datetime
        """
        self.__block_datetime=value

    @property
    def log_level(self)->str:
        """
        Function that returns property log_level
        """
        return self.__log_level
    @log_level.setter
    def log_level(self,value:str):
        """
        Setter for property log_level
        """
        if value not in log_levels.LEVELS_RANK().keys():
            raise argument_exception(f"Wrong log level {value}")
        self.__log_level=value


    @property
    def log_dir(self)->str:
        """
        Function that returns property log_file
        """
        return self.__log_dir
    @log_dir.setter
    def log_dir(self,value:str):
        """
        Setter for property log_file
        """
        self.__log_dir=value

    def default(self):
        """
        Function that creates company_model and sets it to property company
        """
        self.__company=company_model()