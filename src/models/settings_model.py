from .abstract_reference import *
from .company_model import company_model

class settings_model(abstract_reference):
    """
    Class for work with company settings. Inherited from abstract_reference
    company - company_model : company
    """
    __company:company_model=None

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

    
    def default(self):
        """
        Function that creates company_model and sets it to property company
        """
        self.__company=company_model()
