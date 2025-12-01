from ..core.abstract_reference import *


class company_model(abstract_reference):
    """
    Class for work with company. Inherited from abstract_reference
    inn - int : inn number
    account - str : account
    coraccount - str : correspondent account
    bic - int : bic number
    property_type - str : property type
    """
    __inn:int
    __account:str
    __coraccount:str
    __bic:int
    __property_type:str
    
    def __init__(self,*args,**kwargs):
        """
        Constructor of class
        First set ofparams:
        name - str
        inn - int
        account - str
        coraccount - str 
        bic - int
        property_type - str

        Second set of params:
        company_model_settings - company_model
        """
        self._prop_validator=model_validator(self.__class__._prop_validator.limits+ # inherit old limits
                                             [limit_model("inn",Operator.EQ,12),    # add length inn = 12
                                             limit_model("account",Operator.EQ,11), # add length account =11
                                             limit_model("coraccount",Operator.EQ,11), # add length coraccount =11
                                             limit_model("bic",Operator.EQ,9),      # add length bic = 9
                                             limit_model("property_type",Operator.EQ,5)]) #add length property_type=5
        if len(args) == 1 and isinstance(args[0], company_model): # if length of args = 1 it should be company_model_settings
            settings = args[0] #sets args
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
                    raise argument_exception("wrong amount of arguments")
            except:
                raise argument_exception("company model init accepts only 'company_model' object, or all 6 params")
    
    def __copy_from_settings_manager(self,settings_instance):
        """
        Function that copy params from company_model
        settings_instance - company_model
        """
        if not isinstance(settings_instance,company_model):
            raise argument_exception("company model can accept only company_model")
        self.__init_from_params(settings_instance.name,
                                settings_instance.inn,
                                settings_instance.account,
                                settings_instance.coraccount,
                                settings_instance.bic,
                                settings_instance.property_type)

    def __init_from_params(self,name:str,inn:str,account:str,coraccount:str,bic:str,property_type:str):
        """
        Function that sets params of class
        name - str
        inn - int
        account - str
        coraccount - str 
        bic - int
        property_type - str
        """
        super().__init__(name)
        self.inn=inn
        self.account=account
        self.coraccount=coraccount
        self.bic=bic
        self.property_type=property_type
    
    @property
    def inn(self)->int:
        """
        Function that returns property inn
        """
        return self.__inn
    
    @inn.setter
    def inn(self,value:int):
        """
        Function that sets property inn
        value - int
        """
        if self._prop_validator.valid_property("inn",str(value)):
            try:
                self.__inn=int(value)
            except:
                raise argument_exception("inn can be only integer or string that can be converted in integer")
        else:
            raise argument_exception("wrong length of inn")
    
    @property
    def account(self)->str:
        """
        Function that returns property account
        """
        return self.__account
    
    @account.setter
    def account(self,value:str):
        """
        Function that sets property account
        value - str
        """
        if self._prop_validator.valid_property("account",value):
            self.__account=value.strip()
        else:
            raise argument_exception("wrong length of account")

    @property
    def coraccount(self)->str:
        """
        Function that returns property coraccount
        """
        return self.__coraccount
    
    @coraccount.setter
    def coraccount(self,value:str):
        """
        Function that sets property coraccount
        value - str
        """
        if self._prop_validator.valid_property("coraccount",value):
            self.__coraccount=value.strip()
        else:
            raise argument_exception("wrong length of correspodent account")
    
    @property
    def bic(self)->str:
        """
        Function that returns property bic
        """
        return self.__bic
    
    @bic.setter
    def bic(self,value:int):
        """
        Function that sets property bic
        value - int
        """
        if self._prop_validator.valid_property("bic",str(value)):
            try:
                self.__bic=int(value)
            except:
                raise argument_exception("inn can be only integer or string that can be converted in integer")
        else:
            raise argument_exception("wrong length of bic")
    
    @property
    def property_type(self)->str:
        """
        Function that returns property property_type
        """
        return self.__property_type
    
    @property_type.setter
    def property_type(self,value:str):
        """
        Function that sets property property_type
        value - str
        """
        if self._prop_validator.valid_property("property_type",value):
            self.__property_type=value.strip()
        else:
            raise argument_exception("wrong length of property type")
