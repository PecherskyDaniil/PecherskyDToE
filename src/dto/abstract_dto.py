import abc
from ..core.common import common
from ..core.abstract_reference import model_validator,argument_exception, operation_exception

class abstract_dto:
    """
    Abstract class for dtos
    """ 

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
    
