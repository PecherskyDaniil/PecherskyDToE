from ..core.reposity_keys import reposity_keys
from ..core.object_service import object_service
from ..models.storage_model import storage_model
class storage_service(object_service):
    """
    Class for service storage changes
    """
    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self._object_maps={
            reposity_keys.transaction_key():"storage",
            reposity_keys.remnant_key():"storage"
        }
        self._serviced_object=storage_model
        self._serviced__object_key=reposity_keys.storage_key()