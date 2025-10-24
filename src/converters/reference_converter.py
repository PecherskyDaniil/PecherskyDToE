from .abstract_converter import abstract_converter
from ..models.abstract_reference import abstract_reference
from ..models.proportion import proportion
from ..models.step import step
from .dto_converter import dto_converter
from .basic_converter import basic_converter
from .datetime_converter import datetime_converter
from ..core.common import common
class reference_converter(abstract_converter):
    """
    Class for converting reference data to dict
    """
    @staticmethod
    def convert(obj):
        """
        Function to converting reference object to dict
        """
        data={}
        fields=common.get_fields(obj)
        for key in fields:
            attr=getattr(obj, key) 
            if isinstance(attr,abstract_reference) or isinstance(attr,step) or isinstance(attr,proportion):
                data[key]=dto_converter.convert(attr.to_dto())
            elif isinstance(attr,list) and len(attr)>0 and (isinstance(attr[0],abstract_reference) or isinstance(attr[0],step) or isinstance(attr[0],proportion)):
                sub_data=[]
                for item in attr:
                    sub_data.append(dto_converter.convert(item.to_dto()))
                data[key]=sub_data
        data=data | dto_converter.convert(obj)
        data=data | basic_converter.convert(obj)
        data=data | datetime_converter.convert(obj)
        return data

