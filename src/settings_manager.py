import os
import json

from .models.company_model import company_model
from .models.settings_model import settings_model
from .models.abstract_reference import *
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

    def load(self)->bool:
        if self.__config_filename.strip=="":
            raise operation_exception("config file not found")
        
        try:
            data=json.load(open(self.__config_filename,"r"))
            if "company" in data.keys():
                item=data["company"]
                self.__settings.company_settings.name=item["name"]
                self.__settings.company_settings.inn=item["inn"]
                self.__settings.company_settings.bic=item["bic"]
                self.__settings.company_settings.account=item["account"]
                self.__settings.company_settings.coraccount=item["coraccount"]
                self.__settings.company_settings.property_type=item["property_type"]
                return True
        except Exception as e:
            return False
    
    def convert(self,data:dir):
        if "company" in data.keys():
            try:
                item=data["company"]
                self.__settings.company_settings.name=item["name"]
                self.__settings.company_settings.inn=item["inn"]
                self.__settings.company_settings.bic=item["bic"]
                self.__settings.company_settings.account=item["account"]
                self.__settings.company_settings.coraccount=item["coraccount"]
                self.__settings.company_settings.property_type=item["property_type"]
                return True
            except Exception as e:
                return False
        return False

    def default(self):
        self.__settings=settings_model()
