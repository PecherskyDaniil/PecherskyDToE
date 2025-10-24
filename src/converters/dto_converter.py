from .abstract_converter import abstract_converter
from ..dto.abstract_dto import abstract_dto
from .basic_converter import basic_converter
from .datetime_converter import datetime_converter
from ..core.common import common
class dto_converter(abstract_converter):
    """
    Class for converting dto data to dict
    """
    @staticmethod
    def convert(obj):
        """
        Function to converting dto object to dict
        """
        data={}
        fields=common.get_fields(obj)
        for key in fields:
            attr=getattr(obj, key) 
            if isinstance(attr,abstract_dto):
                data[key]=dto_converter.convert(attr)
            elif isinstance(attr,list) and len(attr)>0 and isinstance(attr[0],abstract_dto):
                sub_data=[]
                for item in attr:
                    sub_data.append(dto_converter.convert(item))
                data[key]=sub_data
        data=data | basic_converter.convert(obj)
        data=data | datetime_converter.convert(obj)
        return data

