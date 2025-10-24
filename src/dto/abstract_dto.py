import abc
from ..core.common import common
from ..models.abstract_reference import model_validator,argument_exception, operation_exception

class abstract_dto:
    """
    Abstract class for dtos
    """
    __name:str = ""
    __uuid:str = ""

    @property
    def name(self) ->str:
        """
        Property name
        """
        return self.__name
    
    @name.setter
    def name(self, value):
        """
        Setter for property name
        """
        self.__name = value

    @property
    def uuid(self) -> str:
        """
        Property id
        """
        return self.__uuid

    @uuid.setter
    def uuid(self, value):
        """
        Setter for property id
        """
        self.__uuid = value   

    @abc.abstractmethod
    def create(self, data) -> "abstract_dto":
        """
        Function create for dto
        """
        if not(model_validator.check_type(data, dict)):
            raise argument_exception("dto can be created only from dict")
        fields = common.get_fields(self)
        matching_keys = list(filter(lambda key: key in fields, data.keys()))

        try:
            for key in matching_keys:
                setattr(self, key, data[ key ])
        except:
            raise operation_exception("Невозможно загрузить данные!")    

        return self
    
