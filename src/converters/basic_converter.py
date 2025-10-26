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
        #if isinstance(obj,str) or isinstance(obj,int) or isinstance(obj,float):
        return obj
