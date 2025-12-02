from ..core.reposity_keys import reposity_keys
from ..core.object_service import object_service
from ..models.transaction_model import transaction_model
class transaction_service(object_service):
    """
    Class for service transaction changes
    """
    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self._object_maps={}
        self._serviced_object=transaction_model
        self._serviced__object_key=reposity_keys.transaction_key()