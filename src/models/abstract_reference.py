import json
import uuid
from enum import Enum,auto
from abc import ABC

class argument_exception(Exception):
    pass
class operation_exception(Exception):
    pass
class error_proxy(Exception):
    pass
class OperatorType(Enum):
    EQ=auto()
    GT=auto()
    LT=auto()
    GE=auto()
    LE=auto()
    NE=auto()


class limit_model():
    name:str
    operator:OperatorType
    value:any

    def __init__(self,name:str,operator:OperatorType,value):
        self.name=name
        if isinstance(operator,OperatorType):
            self.operator=operator
        else:
            raise argument_exception("неверный тип оператора")
        self.value=value
    
    def check_limit(self,value):
        match self.operator:
            case OperatorType.EQ: return value == self.value
            case OperatorType.GT: return value > self.value
            case OperatorType.LT: return value < self.value
            case OperatorType.GE: return value >= self.value
            case OperatorType.LE: return value <= self.value
            case OperatorType.NE: return value != self.value

class model_validator():
    __limits=None

    def __init__(self,limits:list[limit_model]):
        self.limits=limits
    
    @property
    def limits(self)->list[limit_model]:
        return self.__limits
    
    @limits.setter
    def limits(self,value:dict):
         self.__limits=value

    def valid_property(self,property_name,property_value):
        if property_value is not None:
            for limit in self.limits:
                if limit.name==property_name:
                    if limit.check_limit(len(str(property_value))):
                        return property_value
                    else:
                        raise argument_exception("неверная длина")
            raise argument_exception("неверная длина")

    def check_type(self,value,type):
        if isinstance(value,type):
            return value
        else:
            raise argument_exception("неверный тип")

class abstract_reference(ABC):
    __uuid=None
    __name:str=""
    _prop_validator=model_validator([limit_model("name",OperatorType.LE,50)])
    def __init__(self,name:str):
        self.__uuid=str(uuid.uuid4())
        self.name=name
   
    @property
    def name(self)->str:
        return self.__name
    
    @name.setter
    def name(self,value:str):
        self.__name=self._prop_validator.valid_property("name",value)
    def __eq__(self,obj):
        return self.__uuid==obj.uuid
    @property
    def uuid(self) -> str:
        return self.__uuid
    @uuid.setter
    def uuid(self, value:str):
        if value.strip()!="":
            self.__uuid = value.strip()



    

