
from ..core.event_type import event_type
from ..core.reposity_keys import reposity_keys
from ..core.abstract_logic import abstract_logic
from ..core.observe_service import observe_service
from ..core.abstract_reference import model_validator,operation_exception,abstract_reference
from ..models.storage_model import storage_model
from ..models.unit_model import unit_model
from ..core.prototype import prototype
from ..dto.filter_dto import filter_dto
class object_service(abstract_logic):
    """
    Class for service object changes
    """
    
    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self._serviced_object=None
        self._serviced__object_key=None
        self._object_maps={}
        # Подключение в наблюдение
        observe_service.add(self)
   
    """
    Обработка событий
    """
    def handle(self, event:str, params):
        super().handle(event, params)  

        if not(isinstance(params,list)) or not(isinstance(params[1],self._serviced_object)):
            return
        
        if event==event_type.add_new_object():
            return self.handle_add_new_object(params[0],params[1])
        elif event==event_type.start_deletion_object():
            return self.handle_delete_object(params[0],params[1])
        elif event==event_type.change_object():
            return self.handle_change_object(params[0],params[1])
    
    def handle_add_new_object(self,reposity_object,reference_object:abstract_reference):
        """
        Addition handle
        """
        if reference_object.uuid in reposity_object.data[self._serviced__object_key].keys():
            raise operation_exception(f"Object with this uuid already in reposity {reference_object.uuid}")

    def handle_delete_object(self,reposity_object,reference_object:abstract_reference):
        """
        Deletion handle
        """
        for key,value in self._object_maps.items():
            base_prototype=prototype(list(reposity_object.data[key].values()))
            filtered_prototype=base_prototype.filter([filter_dto.create(f"{value}.uuid","eq",reference_object.uuid)])
            if len(filtered_prototype.data)>0:
                raise operation_exception(f"Cant delete object with uuid {reference_object.uuid}")

    def handle_change_object(self,reposity_object,reference_object:abstract_reference):
        """
        Alter handle
        """
        for key,value in self._object_maps.items():
            base_prototype=prototype(list(reposity_object.data[key].values()))
            filtered_prototype=base_prototype.filter([filter_dto.create(f"{value}.uuid","eq",reference_object.uuid)])
            for object in filtered_prototype.data:
                setattr(reposity_object.data[key][object.uuid],value,reference_object)
        
        return True