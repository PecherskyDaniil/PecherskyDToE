
from .abstract_reference import *
from .unit_model import unit_model
from .range_group_model import range_group_model
from functools import lru_cache
class range_model(abstract_reference):
    """
    Class for work with range. Inherited from abstract_reference
    full_name - str : full name
    unit - unit_model: unit of range
    group - range_group_model : group of range
    """
    __full_name:str=""
    __unit:unit_model=None
    __group:range_group_model=None

    __values:dict={}
    def __init__(self,name:str,full_name:str,unit:unit_model,group:range_group_model):
        """
        Constructor of class
        name - str
        full_name - str
        unit - unit_model
        group - range_group_model
        """
        super().__init__(name)
        self._prop_validator=model_validator(self.__class__._prop_validator.limits+[limit_model("full_name",Operator.LE,255)])
        self.full_name=full_name
        self.unit=unit
        self.group=group

    #Наименование
    @property
    def full_name(self) -> str:
        """
        Function that returns property full_name
        """
        return self.__full_name

    @full_name.setter
    def full_name(self, value:str):
        """
        Function that sets property full_name
        value - str
        """
        if self._prop_validator.valid_property("full_name",value):
            self.__full_name = value.strip()
        else:
            raise argument_exception("wrong length of full_name")


    @property
    def unit(self) -> str:
        """
        Function that returns property unit
        """
        return self.__unit

    @unit.setter
    def unit(self, value:unit_model):
        """
        Function that sets property unit
        value - unit_model
        """
        if self._prop_validator.check_type(value,unit_model):
            self.__unit = value
        else:
            raise argument_exception("unit should be unit_model")
    

    @property
    def group(self) -> str:
        """
        Function that returns property group
        """
        return self.__group

    @group.setter
    def group(self, value:range_group_model):
        """
        Function that sets property group
        value - range_group_model
        """
        if self._prop_validator.check_type(value,range_group_model):
            self.__group = value
        else:
            raise argument_exception("group should be range_group_model")

    def _create_default_value(name:str,full_name:str,unit:unit_model,range_group:range_group_model):
        """
        Function that creates deafult instances and save it in class
        """
        if name not in range_model.__values.keys():
            range_model.__values[name]=range_model.create(name,full_name,unit,range_group)
        return range_model.__values[name]
    
    @staticmethod
    #@singleton_result
    def create_milk():
        """
        Creates default range milk
        """
        return range_model._create_default_value("молоко","Молоко пастеризованное натуральное",unit_model.create_litr(),range_group_model.create_ingredients())

    @staticmethod
    #@singleton_result
    def create_salt():
        """
        Creates default range salt
        """
        return range_model._create_default_value("соль","Соль пищевая кристализованная",unit_model.create_killogramm(),range_group_model.create_ingredients())


    @staticmethod
    #@singleton_result
    def create_sugar():
        """
        Creates default range sugar
        """
        return range_model._create_default_value("сахар","Сахар песок",unit_model.create_killogramm(),range_group_model.create_ingredients())


    @staticmethod
    #@singleton_result
    def create_flour():
        """
        Creates default range flour
        """
        return range_model._create_default_value("мука","Мука пшеничная 1 сорт",unit_model.create_killogramm(),range_group_model.create_ingredients())

    
    @staticmethod
    #@singleton_result
    def create_egg():
        """
        Creates default range egg
        """
        return range_model._create_default_value("яйцо","Яйцо куринное",unit_model.create_item(),range_group_model.create_ingredients())

    
    @staticmethod
    #@singleton_result
    def create_butter():
        """
        Creates default range butter
        """
        return range_model._create_default_value("масло сливочное","Масло сливочное натуральное",unit_model.create_gramm(),range_group_model.create_ingredients())

    
    @staticmethod
    #@singleton_result
    def create_vanilin():
        """
        Creates default range vanilin
        """
        return range_model._create_default_value("ванилин","Ванилин пищевой ароматизатор",unit_model.create_gramm(),range_group_model.create_ingredients())


    @staticmethod
    #@singleton_result
    def create_water():
        """
        Creates default range water
        """
        return range_model._create_default_value("вода","Вода питьевая негазированная",unit_model.create_millilitr(),range_group_model.create_ingredients())


    @staticmethod
    #@singleton_result
    def create_oil():
        """
        Creates default range oil
        """
        return range_model._create_default_value("масло растительное","Масло растительное подсолнечное",unit_model.create_millilitr(),range_group_model.create_ingredients())


    @staticmethod
    #@singleton_result
    def create_yeasts():
        """
        Creates default range yests
        """
        return range_model._create_default_value("дрожжи","Дрожжи сухие",unit_model.create_gramm(),range_group_model.create_ingredients())


    @staticmethod
    #@singleton_result
    def create_mozarella_cheese():
        """
        Creates default range mozarella cheese
        """
        return range_model._create_default_value("моцарелла сыр","Сыр моцарелла",unit_model.create_gramm(),range_group_model.create_ingredients())

    
    @staticmethod
    #@singleton_result
    def create_adugey_cheese():
        """
        Creates default range adugey cheese
        """
        return range_model._create_default_value("адыгейский сыр","Адыгейский сыр",unit_model.create_gramm(),range_group_model.create_ingredients())



    @staticmethod
    def create(name:str,full_name:str,unit:unit_model,range_group:range_group_model):
        """
        Creates range 
        name:str
        full_name:str
        unit:unit_model
        range_group:range_group_model
        """
        return range_model(name,full_name,unit,range_group)
    
    