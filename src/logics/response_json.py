import json

from .abstract_response import abstract_response
from ..core.common import common
from ..models.abstract_reference import abstract_reference

class response_json(abstract_response):
    """
    Class for response json formatter
    """

    @staticmethod
    def response_type():
        """
        Type of API response
        """
        return "application/json"
    
    # Сформировать CSV
    def create(self, data: list):
        """
        Function that convert data to json format
        """
        text = super().create(data)
        dict_obj=self.build_object_dict(data)
        result={}
        result["data"]=dict_obj
        text+=json.dumps(result)
        return text 