import json


class company_model:
    __name:str = ""
    __inn:str = ""
    __account=""
    __coraccount=""
    __bic=""
    __property_type=""

    @property
    def name(self)->str:
        return self.__name
    
    @name.setter
    def name(self,value:str):
        if value.strip()!="":
            self.__name=value.strip()
    
    @property
    def inn(self)->str:
        return self.__inn
    
    @inn.setter
    def inn(self,value:str):
        if value.strip()!="":
            if len(value)!=12:
                raise SyntaxError("not valid length")
            self.__inn=value.strip()
    
    @property
    def account(self)->str:
        return self.__account
    
    @account.setter
    def account(self,value:str):
        if value.strip()!="":
            if len(value)!=11:
                raise SyntaxError("not valid length")
            self.__account=value.strip()

    @property
    def coraccount(self)->str:
        return self.__coraccount
    
    @coraccount.setter
    def coraccount(self,value:str):
        if value.strip()!="":
            if len(value)!=11:
                raise SyntaxError("not valid length")
            self.__coraccount=value.strip()
    
    @property
    def bic(self)->str:
        return self.__bic
    
    @bic.setter
    def bic(self,value:str):
        if value.strip()!="":
            if len(value)!=9:
                raise SyntaxError("not valid length")
            self.__bic=value.strip()
    
    @property
    def property_type(self)->str:
        return self.__property_type
    
    @property_type.setter
    def property_type(self,value:str):
        if len(value)!=5:
                raise SyntaxError("not valid length")
        if value.strip()!="":
            self.__property_type=value.strip()





class settings_model:
    __company:company_model=None

    def __init__(self):
        self.default()

    
    @property
    def company_settings(self)->company_model:
        return self.__company

    
    def default(self):
        self.__company=company_model()
        #self.__company.name="company"



