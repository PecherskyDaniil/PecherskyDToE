from .abstract_reference import *
from functools import lru_cache
class range_group_model(abstract_reference):
    """
    Class for work with range groups. Inherited from abstract_reference
    """
    def __init__(self,name:str=None):
        """
        Constructor of class
        name - str
        """
        super().__init__(name)

    @singleton_result
    @staticmethod
    def create_ingredients():
        item=range_group_model.create("ингридиенты")
        return item
    
    @staticmethod
    def create(name):
        return range_group_model(name)

   
