from .abstract_converter import abstract_converter
from ..core.abstract_reference import argument_exception
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
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        raise argument_exception("Gets only datetime")
