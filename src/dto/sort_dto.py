from ..models.abstract_reference import Operator,model_validator
from ..core.common import common


class sort_dto:
    """
    Dto class for sorting data
    keys : list[str] - list of keys of sorting objects
    """
    __keys:list[str]=[]


    @property
    def keys(self)->str:
        """
        Getter for property keys
        """
        return self.__keys
    
    @keys.setter
    def keys(self,value:str):
        """
        Setter for property keys
        """
        model_validator.validate(value,list)
        for item in value:
            model_validator.validate(item,str)
        self.__keys=value
    
    def sort(self,objs:list[dict]):
        """
        Function that sorts data by keys
        """
        return sorted(objs,lambda x:(x[item] for item in self.keys))