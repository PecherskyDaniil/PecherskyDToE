from .abstract_response import abstract_response
from ..core.common import common
from ..models.abstract_reference import abstract_reference

class response_xml(abstract_response):
    """
    Class for response xml formatter
    """

    @staticmethod
    def response_type():
        """
        Type of API response
        """
        return "application/xml"

    # Сформировать xml
    def create(self, data: list):
        """
        Function that convert data to xml format
        """
        text = super().create(data)
        dict_obj=self.build_object_dict(data)
        text="<data>"
        text+=self.__build_xml_from_dict(dict_obj,"obj")
        text+="</data>"
        return text
    
    def __build_xml_from_dict(self,obj:dict,tag:str):
        """
        Function that convert dict to xml format
        """
        text=""
        if isinstance(obj,list):
            for item in obj:
                text+=f"<{tag}>"+self.__build_xml_from_dict(item,"")+f"</{tag}>"
        elif isinstance(obj,dict):
            for key in obj.keys():
                if isinstance(obj[key],dict) or isinstance(obj[key],list):
                    text+=f"<{key}>{self.__build_xml_from_dict(obj[key],key+'_obj')}</{key}>"
                else:
                    text+=f"<{key}>{obj[key]}</{key}>"
        else:
            text+=str(obj)
        return text