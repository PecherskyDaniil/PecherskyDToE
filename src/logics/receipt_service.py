from ..core.reposity_keys import reposity_keys
from ..core.object_service import object_service
from ..models.receipt_model import receipt_model
class receipt_service(object_service):
    """
    Class for service receipt changes
    """
    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self._object_maps={}
        self._serviced_object=receipt_model
        self._serviced__object_key=reposity_keys.receipt_key()