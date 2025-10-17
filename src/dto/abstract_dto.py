import abc
from ..core.common import common
from ..models.abstract_reference import model_validator,argument_exception, operation_exception

class abstract_dto:
    """
    Abstract class for dtos
    """
    __name:str = ""
    __id:str = ""

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
    def id(self) -> str:
        """
        Property id
        """
        return self.__id

    @id.setter
    def id(self, value):
        """
        Setter for property id
        """
        self.__id = value   

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
    
    @abc.abstractmethod
    def to_dict(self) -> dict:
        """
        Function for convert dto to dictionary
        """
        fields = common.get_fields(self)
        data={}
        for key in fields:
            attr=getattr(self, key) 
            if isinstance(attr,abstract_dto):
                data[key]=attr.to_dict()
            elif isinstance(attr,list) and len(attr)>0 and isinstance(attr[0],abstract_dto):
                sub_data=[]
                for obj in attr:
                    sub_data.append(obj.to_dict())
                data[key]=sub_data
            else:
                data[key]=attr
        return data
