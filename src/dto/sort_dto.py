from ..models.abstract_reference import Operator,model_validator
from ..core.common import common


class sort_dto:
    __keys:list[str]=[]


    @property
    def keys(self)->str:
        return self.__keys
    
    @keys.setter
    def keys(self,value:str):
        model_validator.validate(value,list)
        for item in value:
            model_validator.validate(item,str)
        self.__keys=value
    
    def sort(self,objs:list[dict]):
        return sorted(objs,lambda x:(x[item] for item in self.keys))