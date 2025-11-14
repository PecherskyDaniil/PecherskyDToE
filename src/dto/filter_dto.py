from ..models.abstract_reference import Operator,model_validator,argument_exception
from ..core.common import common


class filter_dto:
    """
    Class for filter dto
    key:str - key fielad of filter
    operator:str - operator for filtering
    value:any - value of filtering
    """
    __key:str=None
    __operator:str=None
    __value:any=None

    @property
    def key(self)->str:
        """
        Getter for property key
        """
        return self.__key
    
    @key.setter
    def key(self,value:str):
        """
        Setter for property key
        """
        model_validator.validate(value,str)
        self.__key=value
    
    @property
    def operator(self)->str:
        """
        Getter for property opeartor
        """
        return self.__operator
    
    @operator.setter
    def operator(self,value:str):
        """
        Setter for property operator
        """
        model_validator.validate(value,str)
        if value not in [e.value for e in Operator]:
            raise argument_exception(f"Operator is not valid (not in {[e.value for e in Operator]})")
        self.__operator=value

    @property
    def value(self)->any:
        """
        Getter for property value
        """
        return self.__value
    
    @value.setter
    def value(self,value:any):
        """
        Setter for property value
        """
        self.__value=value
    
    def __apply_operator(self,value1,operator,value2):
        """
        Function for applying operator
        """
        match operator:
            case "eq": return value1==value2
            case "gt": return value1>value2
            case "lt": return value1<value2
            case "ge": return value1>=value2
            case "le": return value1<=value2
            case "ne": return value1!=value2
            case "in": return value1 in value2
            case "like":return value1 in value2
            case _: return False

    def validate(self,obj:any):
        """
        Function for validating object in filter
        """
        keys=self.key.split(".")
        attr=obj
        for key in keys:
            if attr is None:
                return False
            fields=common.get_fields(attr)
            if key not in fields:
                return False
            attr=getattr(attr,key) 
        answer=self.__apply_operator(attr,self.operator,self.value)
        return answer 
    
    def create(key:str,operator:str,value:any)->"filter_dto":
        filter_obj=filter_dto()
        filter_obj.key=key
        filter_obj.operator=operator
        filter_obj.value=value
        return filter_obj

    def from_dict(dict_obj:dict):
        model_validator.validate(dict_obj,dict)
        return filter_dto.create(dict_obj["field_name"],dict_obj["type"],dict_obj["value"])
    
        