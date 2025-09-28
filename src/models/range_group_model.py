from .abstract_reference import *

class range_group_model(abstract_reference):
    """
    Class for work with range groups. Inherited from abstract_reference
    """
    def __init__(self,name:str):
        """
        Constructor of class
        name - str
        """
        super().__init__(name)
