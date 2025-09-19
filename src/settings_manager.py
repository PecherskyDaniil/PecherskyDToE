import os
import json

from src.models.models import company_model,settings_model

class settings_manager:#добавить settings_model как прослойку между settings manager и company models. У класа settings_model будет лишь одно свойство - company. Отдельная ветка step
    __config_filename:str=""
    __settings:settings_model=None

    def __init__(self,config_filename:str=""):
        self.config_filename=config_filename
        self.default()
    
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'instance'):
            cls.instance=super(settings_manager,cls).__new__(cls)
        return cls.instance

    @property
    def config_filename(self)->str:
        return self.__config_filename
    
    @property
    def company_settings(self)->company_model:
        return self.__settings.company_settings
    
    @config_filename.setter
    def config_filename(self,value:str):
        if value.strip()!="":
            if os.path.exists(value):
                self.__config_filename=value.strip()
    
    def _data_company_parse(self,data):
        item=data["company"]
        if len(item["inn"])!=12:
            return False
        if len(item["bic"])!=9:
            return False
        if len(item["account"])!=11:
            return False
        if len(item["cor_account"])!=11:
            return False
        if len(item["property_type"])=5:
            return False
        return True

    def load(self)->bool:
        if self.__config_filename.strip=="":
            raise SyntaxError("config file not found")
        
        try:
            data=json.load(open(self.__config_filename,"r"))
            if "company" in data.keys():
                
                if self._data_company_parse(data):
                    item=data["company"]
                    self.__settings.company_settings.name=item["name"]
                    self.__settings.company_settings.inn=item["inn"]
                    self.__settings.company_settings.bic=item["bic"]
                    self.__settings.company_settings.account=item["account"]
                    self.__settings.company_settings.coraccount=item["cor_account"]
                    self.__settings.company_settings.property_type=item["property_type"]
                    return True
                else:
                    return False
        except:
            return False
    
    def convert(self,data:dir):
        if "company" in data.keys():
            if self._data_company_parse(data):
                item=data["company"]
                self.__settings.company_settings.name=item["name"]
                self.__settings.company_settings.inn=item["inn"]
                self.__settings.company_settings.bic=item["bic"]
                self.__settings.company_settings.account=item["account"]
                self.__settings.company_settings.coraccount=item["cor_account"]
                self.__settings.company_settings.property_type=item["property_type"]
                return True
        return False

    def default(self):
        self.__settings=settings_model()
