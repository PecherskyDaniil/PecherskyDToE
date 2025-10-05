from .abstract_reference import *
from functools import lru_cache
class range_group_model(abstract_reference):
    """
    Class for work with range groups. Inherited from abstract_reference
    """
    __values:dict={}

    def __init__(self,name:str=None):
        """
        Constructor of class
        name - str
        """
        super().__init__(name)

    def _create_default_value(name:str):
        """
        Function that creates deafult instances and save it in class
        """
        if name not in range_group_model.__values.keys():
            range_group_model.__values[name]=range_group_model.create(name)
        return range_group_model.__values[name]


    #@singleton_result
    @staticmethod
    def create_ingredients():
        """
        Function that creates deafult value ingridients
        """
        return range_group_model._create_default_value("ингридиенты")

    
    @staticmethod
    def create(name):
        return range_group_model(name)

   
