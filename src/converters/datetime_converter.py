from .abstract_converter import abstract_converter
from ..core.common import common
import datetime
class datetime_converter(abstract_converter):
    """
    Class for converting datetime data to dict
    """
    @staticmethod
    def convert(obj):
        """
        Function to converting datetime data to dict
        """
        if isinstance(obj,datetime.datetime):
            return obj
        dict_obj={}
        fields=common.get_fields(obj)

        for field in fields:
            value=getattr(obj,field)
            if isinstance(value,datetime.datetime):
                dict_obj[field]=value.strftime("%Y-%m-%d %H:%M:%S")
            elif isinstance(value,list) and len(value)>0:
                if isinstance(value,datetime.datetime):
                    dict_obj[field]=list(map(lambda x:x.strftime("%Y-%m-%d %H:%M:%S"),value))
        return dict_obj
