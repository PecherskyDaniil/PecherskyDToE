from .abstract_converter import abstract_converter
from ..core.common import common

class basic_converter(abstract_converter):
    """
    Class for converting basic data of object (str,int,float) to dict
    """
    @staticmethod
    def convert(obj):
        """
        Function that converts basic object data to dict
        """
        if isinstance(obj,str) or isinstance(obj,int) or isinstance(obj,float):
            return obj
        
        dict_obj={}
        fields=common.get_fields(obj)

        for field in fields:
            value=getattr(obj,field)
            if isinstance(value,str) or isinstance(value,int) or isinstance(value,float) or value is None:
                dict_obj[field]=value
            elif isinstance(value,list) and len(value)>0:
                if isinstance(value[0],str) or isinstance(value[0],int) or isinstance(value[0],float) or value==None:
                    dict_obj[field]=value
        
        return dict_obj
