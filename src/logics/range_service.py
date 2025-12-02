
from ..core.reposity_keys import reposity_keys
from ..core.object_service import object_service
from ..core.abstract_reference import model_validator,operation_exception
from ..models.range_model import range_model
class range_service(object_service):
    """
    Class for service range changes
    """
    
    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self._object_maps={
            reposity_keys.transaction_key():"range",
            reposity_keys.remnant_key():"range"
        }
        self._serviced_object=range_model
        self._serviced__object_key=reposity_keys.range_key()
   

    def handle_delete_object(self,reposity_object,reference_object):
        """
        Special handle_delete_object for range_service
        """
        result1=super().handle_delete_object(reposity_object,reference_object)
        for receipt_object in reposity_object.data[reposity_keys.receipt_key()].values():
            for proportion_object in receipt_object.ingridients:
                if proportion_object.range==reference_object:
                    raise operation_exception(f"Cant delete range with uuid {reference_object.uuid}")
        return True and result1
    
    def handle_change_object(self,reposity_object,reference_object):
        """
        Special handle_change_object for range_service
        """
        result1=super().handle_change_object(reposity_object,reference_object)
        for receipt_object in reposity_object.data[reposity_keys.receipt_key()].values():
                for proportion_object in receipt_object.ingridients:
                    if proportion_object.range.uuid==reference_object.uuid:
                        proportion_object.range=reference_object
        return True and result1