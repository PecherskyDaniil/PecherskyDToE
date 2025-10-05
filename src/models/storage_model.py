
from .abstract_reference import *
class storage_model(abstract_reference):
    """
    Class for work with storage. Inherited from abstract_reference
    """
    def __init__(self,name:str=None):
        """
        Constructor of class
        name - str
        """
        super().__init__(name)