
from ..core.event_type import event_type
from ..core.reposity_keys import reposity_keys
from ..core.object_service import object_service
from ..core.observe_service import observe_service
from ..core.abstract_reference import model_validator,operation_exception
from ..models.storage_model import storage_model
from ..models.unit_model import unit_model
from ..core.prototype import prototype
from ..dto.filter_dto import filter_dto
class unit_service(object_service):
    """
    Class for service units changes
    """
    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self._object_maps={
            reposity_keys.unit_key():"base_unit",
            reposity_keys.range_key():"unit",
            reposity_keys.transaction_key():"unit"
        }
        self._serviced_object=unit_model
        self._serviced__object_key=reposity_keys.unit_key()