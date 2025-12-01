from ..core.abstract_reference import *
from .range_model import range_model
from .range_group_model import range_group_model
from .step import step
from .proportion import proportion
from ..dto.receipt_dto import receipt_dto
from ..dto.proportion_dto import proportion_dto
from ..dto.step_dto import step_dto
from ..core.reposity_keys import reposity_keys
class receipt_model(abstract_reference):
    """
    Class that contains info about receipt
    ingridients:list[proportion] - all proportions of receipt
    steps:list[step] - all steps of instruction for receipts
    """
    __ingridients:list[proportion]
    __steps:list[step]
    __time:float

    def __init__(self,name:str=None,ingridients:list[proportion]=None,steps:list[step]=None,time=None):
        """
        Constructor of class
        name:str
        ingridients:list[proportion]
        steps:list[step]
        """
        super().__init__(name)
        self.ingridients=ingridients
        self.steps=steps
        self.time=time
    
    @property
    def ingridients(self):
        """
        Function that returns ingridients
        """
        return self.__ingridients
    
    @ingridients.setter
    def ingridients(self,value:list[proportion]):
        """
        Function that sets property ingridients
        value:list[proportion]
        """
        if value is None or self._prop_validator.check_type(value,list):
            if value is not None and all(self._prop_validator.check_type(prop,proportion) for prop in value):
                self.__ingridients=value
            elif value is None:
                self.__ingridients=value   
            else:
                raise argument_exception("ingridients should be list of proportions")
        else:
            raise argument_exception("ingridients should be list of proportions")

    @property
    def steps(self):
        """
        Function that returns steps
        """
        return self.__steps
    
    @steps.setter
    def steps(self,value:list[step]):
        """
        Function that sets property steps
        value:list[step]
        """
        if value is None or self._prop_validator.check_type(value,list):
            if value is not None and all(self._prop_validator.check_type(stp,step) for stp in value):
                self.__steps=value
            elif value is None:
                self.__steps=value 
            else:
                raise argument_exception("steps should be list of steps")
        else:
            raise argument_exception("steps should be list of steps")
    
    @property
    def time(self):
        """
        Function that returns time
        """
        return self.__time
    
    @time.setter
    def time(self,value:float):
        """
        Function that sets property time
        value:float
        """
        if value is None or self._prop_validator.check_type(value,float):
            self.__time=value   
        else:
            raise argument_exception("time should be float")
    
    @staticmethod
    def create(name:str,ingridients:list[proportion],steps:list[step],time:float):
        """
        Function that creates receipt
        """
        return receipt_model(name,ingridients,steps,time)

    @staticmethod
    def from_dto(dto:receipt_dto, cache:dict):
        """
        Function that convert instance from dto
        """
        model_validator.validate(dto, receipt_dto)
        model_validator.validate(cache, dict)
        
        steps=[]
        for step_obj in dto.steps:
            steps.append(step(step_obj["step_description"]))
        ingridients=[]
        for receipt_item in dto.ingridients:
            range_obj=cache[reposity_keys.range_key()][receipt_item["range_id"]] if receipt_item["range_id"] in cache[reposity_keys.range_key()] else None
            ingridients.append(proportion(range_obj,receipt_item["proportion_value"]))
        item = receipt_model.create(dto.name,ingridients,steps,dto.time)
        item.uuid=dto.uuid
        return item

    def to_dto(self):
        """
        Function that convert instance to dto
        """
        item=receipt_dto()
        item.name=self.name
        item.uuid=self.uuid
        ingridients=[]
        for proportion_obj in self.ingridients:
            ingridients.append(proportion_obj.to_dto())
        item.ingridients=ingridients
        steps=[]
        for step_obj in self.steps:
            steps.append(step_obj.to_dto())
        item.steps=steps
        item.time=self.time
        return item
