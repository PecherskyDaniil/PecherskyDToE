
from ..core.event_type import event_type
from ..core.reposity_keys import reposity_keys
from ..core.object_service import object_service
from ..core.observe_service import observe_service
from ..core.abstract_reference import model_validator,operation_exception
from ..models.range_group_model import range_group_model
class range_group_service(object_service):
    """
    Class for service units changes
    """
    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self._object_maps={
            reposity_keys.range_key():"group"
        }
        self._serviced_object=range_group_model
        self._serviced__object_key=reposity_keys.range_group_key()