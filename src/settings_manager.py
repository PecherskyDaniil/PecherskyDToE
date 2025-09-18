import os
import json

from src.models.models import company_model

class settings_manager:#добавить settings_model как прослойку между settings manager и company models. У класа settings_model будет лишь одно свойство - company. Отдельная ветка step
    __config_filename:str=""
    __company:company_model=None

    def __init__(self,config_filename:str):
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
        return self.__company
    
    @config_filename.setter
    def config_filename(self,value:str):
        if value.strip()!="":
            if os.path.exists(value):
                self.__config_filename=value.strip()

    def load(self)->bool:
        if self.__config_filename.strip=="":
            raise SyntaxError("config file not found")
        
        try:
            data=json.load(open(self.__config_filename,"r"))
            if "company" in data.keys():
                item=data["company"]
                self.__company.name=item["name"]
                return True
        except:
            return False
    
    def default(self):
        self.__company=company_model()
        self.__company.name="company"
