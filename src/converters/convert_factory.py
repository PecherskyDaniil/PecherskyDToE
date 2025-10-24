from .dto_converter import dto_converter
from .basic_converter import basic_converter
from .datetime_converter import datetime_converter
from .reference_converter import reference_converter
class convert_factory:
    """
    Class for universal converting objects to dict
    """    
    def __convert_item(self,obj:any):
        """
        Function to converting single object of array or dict to dict
        """
        data={}
        data=data | basic_converter.convert(obj)
        data=data | datetime_converter.convert(obj)
        data=data | dto_converter.convert(obj)
        data=data | reference_converter.convert(obj)
        return data
    
    def convert(self,obj:any):
        """
        Function to converting any object to dict
        """
        data={}
        if isinstance(obj,list):
            sub_list=[]
            for item in obj:
                sub_list.append(self.__convert_item(item))
            data["data"]=sub_list
        elif isinstance(obj,dict):
            for key in obj.keys():
                data[key]=self.__convert_item(obj)
        else:
            data=self.__convert_item(obj)
        return data  