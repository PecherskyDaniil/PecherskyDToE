
from ..core.observe_service import observe_service
from ..core.event_type import event_type
from ..core.abstract_reference import abstract_reference
from ..models.range_group_model import range_group_model
from ..models.range_model import range_model
from ..models.receipt_model import receipt_model
from ..models.storage_model import storage_model
from ..models.transaction_model import transaction_model
from ..models.unit_model import unit_model
from ..models.remnant_model import remnant_model
from ..core.reposity_keys import reposity_keys
from ..start_service import start_service

class reference_service:
    """
    Service for managing objects in reposity
    """
    _reference_keys_maps={
        unit_model:reposity_keys.unit_key(),
        range_model:reposity_keys.range_key(),
        range_group_model:reposity_keys.range_group_key(),
        storage_model:reposity_keys.storage_key(),
        receipt_model:reposity_keys.receipt_key(),
        transaction_model:reposity_keys.transaction_key()
    }

    def add(start_service_instance:start_service,reference_object:abstract_reference):
        """
        Adding object to reposity
        """
        try:
            observe_service.create_event(event_type.add_new_object(),reference_object)
            start_service_instance.reposity.data[reference_service._reference_keys_maps[type(reference_object)]][reference_object.uuid]=reference_object
            observe_service.create_event(event_type.added_new_object(),reference_object)
            return True
        except:
            return False
    
    def delete(start_service_instance:start_service,reference_object:abstract_reference):
        """
        Deleting object from reposity
        """
        try:
            observe_service.create_event(event_type.start_deletion_object(),reference_object)
            start_service_instance.reposity.data[reference_service._reference_keys_maps[type(reference_object)]].pop(reference_object.uuid)
            observe_service.create_event(event_type.object_deleted(),reference_object)
            return True
        except:
            return False
    
    def change(start_service_instance:start_service,reference_object:abstract_reference):
        """
        Changing object in reposity
        """
        start_service_instance.reposity.data[reference_service._reference_keys_maps[type(reference_object)]][reference_object.uuid]=reference_object
        observe_service.create_event(event_type.change_object(),reference_object)
        return True
