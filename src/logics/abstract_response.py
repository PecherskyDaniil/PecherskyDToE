from abc import ABC,abstractmethod
from ..models.abstract_reference import model_validator,operation_exception,argument_exception,abstract_reference

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
        model_validator.validate(data[0],abstract_reference)
        dict_obj=list(map(lambda x:x.to_dto().to_dict(),data))
        return dict_obj

    