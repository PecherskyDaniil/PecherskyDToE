from .abstract_reference import *
from ..dto.step_dto import step_dto

class step():
    """
    Class that contain data of step of receipt's instruction 

    step_description:str - info about step
    """
    __step_description:str

    def __init__(self,step_description:str=None):
        """
        Constructor of class
        step_description:str
        """
        self.step_description=step_description

    @property
    def step_description(self):
        """
        Function that returns step_description
        """
        return self.__step_description
    
    @step_description.setter
    def step_description(self,value:str):
        """
        Function that set step_description
        value:str
        """
        if model_validator.check_type(value,str):
            self.__step_description=value
        else:
            raise argument_exception("step_description can be only string")

    def __str__(self):
        """
        Magic function that returns string value of class object
        """
        return str(self.step_description)

    @staticmethod
    def to_dto(model:"step"):
        item=step_dto()
        item.step_description=model.step_description
        return item