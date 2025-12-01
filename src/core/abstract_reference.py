import json
import uuid
from enum import Enum,auto
from abc import ABC, abstractmethod

def singleton_result(func):
        """
        Special Decorator that save result of function after first use and returns it
        result:any - result of function
        initialized:bool - value for check first use of function
        """
        result = None
        initialized = False
        
        def wrapper(*args, **kwargs):
            """
            Function that replace original function
            """
            nonlocal result, initialized
            if not initialized: #if not initialized calculate result
                result = func(*args, **kwargs)
                initialized = True
            return result #returns result
        return wrapper

class argument_exception(Exception):
    """
    Exception that raises when argument of function is not valid
    """
    pass
class operation_exception(Exception):
    """
    Exception that raises when operation have a problems with work
    """
    pass
class error_proxy(Exception):
    """
    Exception that raises when idk
    """
    pass
class Operator(Enum):
    """
    Special class that contains all operators of compare
    """
    EQ="eq" #=
    GT="gt" #>
    LT="lt" #<
    GE="ge" #>=
    LE="le" #<=
    NE="ne" #!=
    IN="in"
    LIKE="like"


class limit_model():
    """
    Special class that contains limits of values
    For example:
    name <= 50

    __name - name of limit
    __operator - operator of compare between values
    __value - value compare with
    """
    __name:str # name of limit
    __operator:Operator #operator
    __value:any #value

    def __init__(self,name:str,operator:Operator,value): 
        """
        Constructor of class
        name - str
        operator - Operator
        value - any
        """
        self.name=name #set name
        self.operator=operator #set operator
        self.value=value # set value
    
    @property
    def name(self)->str:
        """
        Function that return property name
        """
        return self.__name

    @name.setter
    def name(self,value:str):
        """
        Function that sets property name
        value - str
        """
        if not(isinstance(value,str)) or len(value.strip())==0: # name should be str and its length should be > 0
            raise argument_exception("name should be string and not be empty") # if value wrong raises exception
        self.__name=value # if everythin is okay sets value

    @property
    def operator(self)->Operator:
        """
        Function that return property operator
        """
        return self.__operator

    @operator.setter
    def operator(self,value:Operator):
        """
        Function that sets property operator
        value - Operator
        """
        if not(isinstance(value,Operator)): # value should be Operator type
            raise argument_exception("operator should be operator and not be empty") # if value wrong raises exception
        self.__operator=value #if everything ok sets value

    @property
    def value(self)->any:
        """
        Function that return property value
        """
        return self.__value

    @value.setter
    def value(self,value:any):
        """
        Function that sets property value
        value - any
        """
        if value is None: #value cant be None
            raise argument_exception("value cant be None") #if None raises exception
        self.__value=value # if everything ok sets value

    def check_limit(self,value):
        """
        Function that check is value fits limit
        """
        match self.operator: #check what operator it is
            case Operator.EQ: return value == self.value #if eq =
            case Operator.GT: return value > self.value  # if gt >
            case Operator.LT: return value < self.value  # if lt <
            case Operator.GE: return value >= self.value # if ge >=
            case Operator.LE: return value <= self.value # if le <=
            case Operator.NE: return value != self.value # if ne !=

class model_validator():
    """
    Special class for validator of model properties
    limits - list of limit models for properties of class
    """
    __limits=None #list of limit_model

    def __init__(self,limits:list[limit_model]):
        """
        Constructor of class
        limits - list[limit_model]
        """
        self.limits=limits #set limits
    
    @property
    def limits(self)->list[limit_model]:
        """
        Function that return property limits
        """
        return self.__limits
    
    @limits.setter
    def limits(self,value:list[limit_model]):
        """
        Function that sets property limits
        value - list[limit_model]
        """
        if value is None:
            self.__limits=value
            return
        if not isinstance(value,list):# value can be only list
            raise argument_exception("model validator accepts only list of limits") # else raise exception
        for limit in value: # check all elements of value
            if not isinstance(limit,limit_model): # element can be only limit_model
                raise argument_exception("limits can be only 'limit_model'") #else raise exception
        self.__limits=value #if everythong ok set value

    def valid_property(self,property_name:str,property_value:str|int):
        """
        Function that check if value of property filts limit
        property_name - str
        property_value - str|int
        """
        if property_value is not None and property_name is not None: # property_value and property_name can not be None
            for limit in self.limits: # check all limits
                if limit.name==property_name: # if find limit by name check it
                    if limit.check_limit(len(str(property_value).strip())): #check value fits limit 
                        return True # if fits return true
                    else: # else
                        return False # if not fits return false
            return False # if limit not found return false
        else: #else
            raise argument_exception("property name and value cant be None") # if rpoperty_name or property_value is None raise exception

    @staticmethod
    def check_type(value,type):
        """
        Function that checks type of value
        value - any
        type - any (class)
        """
        if isinstance(value,type): #value should be type
            return True #if it is return true
        else: #else
            return False # return false
    @staticmethod
    def validate(value,type):
        if value is None:
            return
        if not(model_validator.check_type(value,type)):
            raise argument_exception(f"value should be {type}")

class abstract_reference(ABC):
    """
    Abstract class that parent for all models of system

    uuid - str : unique identifier for object of system
    name - str : name of model
    _prop_validator - model_validator : validator of models property
    """

    __uuid:str # unique identifier for object of system
    __name:str # name of model
    _prop_validator=model_validator([limit_model("name",Operator.LE,50),limit_model("uuid",Operator.GT,0)]) # name should be <=50, uuid >=0
    @abstractmethod
    def __init__(self,name:str):
        """
        Constructor of class
        name - str
        """
        self.__uuid=str(uuid.uuid4()) #create unique identifier
        self.name=name # set name
    
    @property
    def name(self)->str:
        """
        Function that return property name
        """
        return self.__name
    
    @name.setter
    def name(self,value:str):
        """
        Function that sets property name
        value - str
        """
        if value==None or self._prop_validator.valid_property("name",value): # value should fits limit

            self.__name=value # if everything ok sets value
        else: #else
            raise argument_exception("wrong value for name") # else raises exception

    @property
    def uuid(self) -> str:
        """
        Function that return property uuid
        """
        return self.__uuid
    
    @uuid.setter
    def uuid(self, value:str):
        """
        Function that sets property uuid
        value - str
        """
        if self._prop_validator.valid_property("uuid",value.strip()): # value should fits limit
            self.__uuid = value.strip() # if everything ok sets value
        else: # else
            raise argument_exception(f"empty value cant be 'uuid'") # else raises exception

    def __eq__(self,obj):
        """
        Magic function that resets operator =
        obj - any
        """
        if obj is not None and obj.uuid is not None: # obj cant be None and should have uuid
            return self.__uuid==obj.uuid #if uuid equals then objects equals
        else: #else
            raise operation_exception(f"cant compare with None object or object without 'uuid'") # else raise exception
        

    def create():
        """
        Function that creates instance of model
        """
        pass

    #def __str__(self):
    #    return self.uuid