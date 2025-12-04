import os
import json

from .models.company_model import company_model
from .models.settings_model import settings_model
from .core.abstract_reference import *
from .logics.factory_entities import factory_entities
from .core.abstract_logic import abstract_logic
from .core.observe_service import observe_service
from .core.event_type import event_type
from .core.abstract_reference import model_validator
import datetime
class settings_manager(abstract_logic):
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
        super().__init__()
        observe_service.add(self)
        self.config_filename=config_filename
        self.default()
    
    def __new__(cls,*args,**kwargs):
        """
        Magic function for singeltone
        """
        if not hasattr(cls,'instance'):
            cls.instance=super(settings_manager,cls).__new__(cls)
        return cls.instance

    """
    Обработка событий
    """
    def handle(self, event:str, params:datetime.datetime):
        super().handle(event, params)  
        
        if event==event_type.changed_block_datetime():
            model_validator.validate(params,datetime.datetime)
            data=json.load(open(self.__config_filename,"r"))
            data["block_datetime"]=params.strftime("%Y-%m-%dT%H:%M:%S")
            with open(self.config_filename,"w") as f:
                f.write(json.dumps(data))

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
            if "first_start" in data.keys():
                self.__settings.first_start=data["first_start"]
            else:
                return False
            if "block_datetime" in data.keys():
                self.__settings.block_datetime=datetime.datetime.strptime(data["block_datetime"],"%Y-%m-%dT%H:%M:%S")
            if "log_level" in data.keys():
                self.__settings.log_level=data["log_level"]
            
            if "log_dir" in data.keys():
                self.__settings.log_dir=data["log_dir"]
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
