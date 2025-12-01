from abc import ABC,abstractmethod
from ..core.abstract_reference import model_validator,operation_exception,argument_exception,abstract_reference
from ..converters.convert_factory import convert_factory
class abstract_response(ABC):
    """
    Abstract class for responses
    """
    @abstractmethod
    def create(self,data:list)->str:
        """
        Abstract method for creating responses
        """
        model_validator.validate(data,list)
        if len(data)==0:
            raise operation_exception("data is empty")
        return ""

    #@abstractmethod
    def build_object_dict(self,data:list[abstract_reference]):
        """
        Method for build dict from object
        """
        model_validator.validate(data,list)
        if isinstance(data[0],abstract_reference):
            c_f=convert_factory()
            dict_obj=c_f.convert(data)
            return dict_obj
        elif isinstance(data[0],dict):
            return data
        else:
            argument_exception("object should be absatrct reference or dict")

    