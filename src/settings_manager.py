import os
import json

from .models.company_model import company_model
from .models.settings_model import settings_model
from .models.abstract_reference import *
from .logics.factory_entities import factory_entities
class settings_manager:
    """
    Class for work all setting of system. Singletone
    config_filename - str : filepath to config file
    settings - settings_model : setting of system
    """
    __config_filename:str=""
    __settings:settings_model=None
    
    def __init__(self,config_filename:str=""):
        """
        Constructor of class
        config_filename - str
        """
        self.config_filename=config_filename
        self.default()
    
    def __new__(cls,*args,**kwargs):
        """
        Magic function for singeltone
        """
        if not hasattr(cls,'instance'):
            cls.instance=super(settings_manager,cls).__new__(cls)
        return cls.instance

    @property
    def config_filename(self)->str:
        """
        Function that returns property config_filename
        """
        return self.__config_filename
    
    

    @property
    def settings(self)->settings_model:
        """
        Function that returns settings
        """
        return self.__settings

    

    @property
    def company_settings(self)->company_model:
        """
        Function that returns company settings
        """
        return self.__settings.company_settings
    
    @config_filename.setter
    def config_filename(self,value:str):
        """
        Function that sets property config filename
        value - str
        """
        if value.strip()!="":
            if os.path.exists(value):
                self.__config_filename=value.strip()

    def load(self)->bool:
        """
        Function that loads config params from config file into company_settings
        """
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
            else:
                return False
            if "api" in data.keys():
                self.__settings.response_format=data["api"]["default_response_format"]
            else:
                return False
            return True
        except Exception as e:
            
            return False
    
    def convert(self,data:dict):
        """
        Function that convert dict to config params and loads it into company_settings
        data - dict
        """
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
        """
        Function that creates and sets settings
        """
        self.__settings=settings_model()
