from .abstract_reference import *


class company_model(abstract_reference):
    __inn= ""
    __account=""
    __coraccount=""
    __bic=""
    __property_type=""
    
    def __init__(self,*args,**kwargs):#name:str,inn:str,account:str,coraccount:str,bic:str,property_type:str):
        self._prop_validator=model_validator(self.__class__._prop_validator.limits+[limit_model("inn",OperatorType.EQ,12),
                                       limit_model("account",OperatorType.EQ,11),
                                       limit_model("coraccount",OperatorType.EQ,11),
                                       limit_model("bic",OperatorType.EQ,9),
                                       limit_model("property_type",OperatorType.EQ,5)])
        if len(args) == 1 and isinstance(args[0], company_model):
            settings = args[0]
            self.__copy_from_settings_manager(settings)
        elif kwargs and all(key in kwargs for key in ['name', 'inn', 'account', 'coraccount', 'bic', 'property_type']):
            self.__init_from_params(**kwargs)
        else:
            try:
                if len(args) == 6:
                    self.__init_from_params(*args)
                elif len(args)==0:
                    super().__init__("")
                else:
                    raise argument_exception("Неверное количество параметров")
            except:
                raise argument_exception("Необходимо передать либо settings_manager, либо все 6 параметров")
    
    def __copy_from_settings_manager(self,settings_instance):
        self.__init_from_params(settings_instance.name,
                                settings_instance.inn,
                                settings_instance.account,
                                settings_instance.coraccount,
                                settings_instance.bic,
                                settings_instance.property_type)

    def __init_from_params(self,name:str,inn:str,account:str,coraccount:str,bic:str,property_type:str):
        super().__init__(name)
        self.inn=inn
        self.account=account
        self.coraccount=coraccount
        self.bic=bic
        self.property_type=property_type
    
    @property
    def inn(self)->str:
        return self.__inn
    
    @inn.setter
    def inn(self,value:str):
        self.__inn=int(self._prop_validator.valid_property("inn",value))
    
    @property
    def account(self)->str:
        return self.__account
    
    @account.setter
    def account(self,value:str):
        self.__account=self._prop_validator.valid_property("account",value)

    @property
    def coraccount(self)->str:
        return self.__coraccount
    
    @coraccount.setter
    def coraccount(self,value:str):
        self.__coraccount=self._prop_validator.valid_property("coraccount",value)
    
    @property
    def bic(self)->str:
        return self.__bic
    
    @bic.setter
    def bic(self,value:str):
        self.__bic=int(self._prop_validator.valid_property("bic",value))
    
    @property
    def property_type(self)->str:
        return self.__property_type
    
    @property_type.setter
    def property_type(self,value:str):
        self.__property_type=self._prop_validator.valid_property("property_type",value)
