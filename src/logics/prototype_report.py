
from ..core.prototype import prototype
from ..models.range_model import range_model
from ..models.storage_model import storage_model
from ..models.abstract_reference import model_validator
import datetime
from ..dto.filter_dto import filter_dto
class prototype_report(prototype):
    """
    Class for prototype report
    """
    def __init__(self,data):
        """
        Constructor of class
        """
        super().__init__(data)
    
    def clone(self,data:list):
        """
        Function for cloning data
        """
        return super().clone(data)
            