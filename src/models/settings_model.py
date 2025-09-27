from .abstract_reference import *
from .company_model import company_model

class settings_model(abstract_reference):
    __company:company_model=None

    def __init__(self,name="settings"):
        super().__init__(name)
        self.default()

    
    @property
    def company_settings(self)->company_model:
        return self.__company

    
    def default(self):
        self.__company=company_model()
        #self.__company.name="company"
