from ..core.reposity_keys import reposity_keys
from ..core.object_service import object_service
from ..models.remnant_model import remnant_model
class remnant_service(object_service):
    """
    Class for service remnant changes
    """
    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self._object_maps={}
        self._serviced_object=remnant_model
        self._serviced__object_key=reposity_keys.remnant_key()