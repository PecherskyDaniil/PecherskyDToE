from .abstract_converter import abstract_converter
from ..models.abstract_reference import abstract_reference
from ..models.proportion import proportion
from ..models.step import step
from ..models.abstract_reference import argument_exception
class reference_converter(abstract_converter):
    """
    Class for converting reference data to dict
    """
    @staticmethod
    def convert(obj):
        """
        Function to converting reference object to dict
        """
        if isinstance(obj,abstract_reference) or isinstance(obj,step) or isinstance(obj,proportion):
            return obj.to_dto()
        raise argument_exception("Gets only reference")

