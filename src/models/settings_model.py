from .abstract_reference import *
from .company_model import company_model
from ..logics.factory_entities import factory_entities

class settings_model(abstract_reference):
    """
    Class for work with company settings. Inherited from abstract_reference
    company - company_model : company
    """
    __company:company_model=None
    __fe_instance:factory_entities=None
    __format:str
    def __init__(self,name:str="settings"):
        """
        Constructor of class
        name - str ="settings
        """
        super().__init__(name)
        self.default()

    
    @property
    def company_settings(self)->company_model:
        """
        Function that returns property company_settings
        """
        return self.__company
    @property
    def format(self)->str:
        """
        Function that returns property format
        """
        return self.__format

    @property
    def factory_entity(self)->str:
        """
        Function that returns property factory entities
        """
        return self.__fe_instance

    @format.setter
    def format(self,value):
        """
        Format property
        """
        self.__fe_instance.default_value=value
        self.__format=value

    def default(self):
        """
        Function that creates company_model and sets it to property company
        """
        self.__fe_instance=factory_entities()
        self.__company=company_model()