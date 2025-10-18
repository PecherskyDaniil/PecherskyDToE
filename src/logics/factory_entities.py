from .abstract_response import abstract_response
from .response_csv import response_csv
from .response_markdown import response_markdown
from .response_json import response_json
from .response_xml import response_xml
from ..models.abstract_reference import operation_exception

class factory_entities:
    """
    Class for choosing response formatter
    """
    __match = {
        "csv":  response_csv,
        "markdown":response_markdown,
        "xml":response_xml,
        "json":response_json
    }
    __default_value:str

    @property
    def default_value(self)->str:
        """
        Property default value
        """
        return self.__default_value
    
    @default_value.setter
    def default_value(self,value:str):
        """
        Setter for property default value
        """
        if value not in self.__match.keys():
            raise operation_exception("Формат не верный")
        self.__default_value=value

    # Получить нужный тип
    def create(self, format:str) -> abstract_response:
        """
        Create response formatter
        """
        if format not in self.__match.keys():
            raise operation_exception("Формат не верный")
        
        return self.__match[format]
    
    def create_default(self)->abstract_response:
        """
        Create default response formatter
        """
        return self.create(self.default_value)
    

