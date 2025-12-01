
#from .converters.convert_factory import convert_factory
from .core.abstract_logic import abstract_logic
from .core.abstract_reference import model_validator
from .core.event_type import event_type
from .core.reposity_keys import reposity_keys
from .core.abstract_logic import abstract_logic
from .core.observe_service import observe_service
from .core.event_type import event_type
from .core.abstract_reference import abstract_reference,model_validator,operation_exception
from .models.range_group_model import range_group_model
from .models.range_model import range_model
from .models.receipt_model import receipt_model
from .models.storage_model import storage_model
from .models.transaction_model import transaction_model
from .models.unit_model import unit_model
from .core.prototype import prototype
from .dto.filter_dto import filter_dto
class reposity(abstract_logic):
    """
    Class that contains data of all system
    data:dict - dict of all data
    """
    _reference_keys_maps={
        unit_model:reposity_keys.unit_key(),
        range_model:reposity_keys.range_key(),
        range_group_model:reposity_keys.range_group_key(),
        storage_model:reposity_keys.storage_key(),
        receipt_model:reposity_keys.receipt_key(),
        transaction_model:reposity_keys.transaction_key()
    }


    __data:dict={}

    def __init__(self):
        super().__init__()

        # Подключение в наблюдение
        observe_service.add(self)
    @property
    def data(self):
        """
        Function that returns data
        """
        return self.__data
    @data.setter
    def data(self,data:dict):
        """
        Function that sets property data
        value:dict
        """
        self.__data=data
    
    

    """
    Обработка событий
    """
    def handle(self, event:str, params):
        super().handle(event, params)  

        if not(isinstance(params,abstract_reference)):
            return
        
        if event==event_type.add_new_object():
            return self.handle_add_new_object(params)
        elif event==event_type.start_deletion_object():
            return self.handle_delete_object(params)
        elif event==event_type.change_object():
            return self.handle_change_object(params)
    
    def handle_add_new_object(self,reference_object:abstract_reference):
        if reference_object.uuid in self.data[reposity._reference_keys_maps[type(reference_object)]].keys():
            raise operation_exception(f"Object with this uuid already in reposity {reference_object.uuid}")

    def handle_delete_object(self,reference_object:abstract_reference):

        if isinstance(reference_object,unit_model):

            unit_base_prototype=prototype(list(self.data[reposity_keys.unit_key()].values()))
            filtered_unit_base_prototype=unit_base_prototype.filter([filter_dto.create("base_unit.uuid","eq",reference_object.uuid)])
            if len(filtered_unit_base_prototype.data)>0:
                raise operation_exception(f"Cant delete object with uuid {reference_object.uuid}")

            range_base_prototype=prototype(list(self.data[reposity_keys.range_key()].values()))
            filtered_range_base_prototype=range_base_prototype.filter([filter_dto.create("unit.uuid","eq",reference_object.uuid)])
            if len(filtered_range_base_prototype.data)>0:
                raise operation_exception(f"Cant delete object with uuid {reference_object.uuid}")
            
            transaction_base_prototype=prototype(list(self.data[reposity_keys.transaction_key()].values()))
            filtered_transaction_base_prototype=transaction_base_prototype.filter([filter_dto.create("unit.uuid","eq",reference_object.uuid)])
            if len(filtered_transaction_base_prototype.data)>0:
                raise operation_exception(f"Cant delete object with uuid {reference_object.uuid}")
            
        elif isinstance(reference_object,range_model):
            for receipt_object in self.data[reposity_keys.receipt_key()].values():
                for proportion_object in receipt_object.ingridients:
                    if proportion_object.range==reference_object:
                        raise operation_exception(f"Cant delete object with uuid {reference_object.uuid}")
            
            transaction_base_prototype=prototype(list(self.data[reposity_keys.transaction_key()].values()))
            filtered_transaction_base_prototype=transaction_base_prototype.filter([filter_dto.create("range.uuid","eq",reference_object.uuid)])
            if len(filtered_transaction_base_prototype.data)>0:
                raise operation_exception(f"Cant delete object with uuid {reference_object.uuid}")
        elif isinstance(reference_object,range_group_model):
            range_base_prototype=prototype(list(self.data[reposity_keys.range_key()].values()))
            filtered_range_base_prototype=range_base_prototype.filter([filter_dto.create("group.uuid","eq",reference_object.uuid)])
            if len(filtered_range_base_prototype.data)>0:
                raise operation_exception(f"Cant delete object with uuid {reference_object.uuid}")
        elif isinstance(reference_object,storage_model):
            transaction_base_prototype=prototype(list(self.data[reposity_keys.transaction_key()].values()))
            filtered_transaction_base_prototype=transaction_base_prototype.filter([filter_dto.create("storage.uuid","eq",reference_object.uuid)])
            if len(filtered_transaction_base_prototype.data)>0:
                raise operation_exception(f"Cant delete object with uuid {reference_object.uuid}")


    def handle_change_object(self,reference_object:abstract_reference):
        if isinstance(reference_object,unit_model):
            unit_base_prototype=prototype(list(self.data[reposity_keys.unit_key()].values()))
            filtered_unit_base_prototype=unit_base_prototype.filter([filter_dto.create("base_unit.uuid","eq",reference_object.uuid)])
            for unit_object in filtered_unit_base_prototype.data:
                self.data[reposity_keys.unit_key()][unit_object.uuid].base_unit=reference_object

            range_base_prototype=prototype(list(self.data[reposity_keys.range_key()].values()))
            filtered_range_base_prototype=range_base_prototype.filter([filter_dto.create("unit.uuid","eq",reference_object.uuid)])
            for range_object in filtered_range_base_prototype.data:
                self.data[reposity_keys.range_key()][range_object.uuid].unit=reference_object

            transaction_base_prototype=prototype(list(self.data[reposity_keys.transaction_key()].values()))
            filtered_transaction_base_prototype=transaction_base_prototype.filter([filter_dto.create("unit.uuid","eq",reference_object.uuid)])
            for transaction_object in filtered_transaction_base_prototype.data:
                self.data[reposity_keys.transaction_key()][transaction_object.uuid].unit=reference_object

            remnant_base_prototype=prototype(list(self.data[reposity_keys.transaction_key()].values()))
            filtered_remnant_base_prototype=remnant_base_prototype.filter([filter_dto.create("unit.uuid","eq",reference_object.uuid)])
            for remnant_obj in filtered_remnant_base_prototype.data:
                self.data[reposity_keys.transaction_key()][remnant_obj.uuid].unit=reference_object
            
            return True
        elif isinstance(reference_object,range_model):
            for receipt_object in self.data[reposity_keys.receipt_key()].values():
                for proportion_object in receipt_object.ingridients:
                    if proportion_object.range.uuid==reference_object.uuid:
                        proportion_object.range=reference_object
            
            transaction_base_prototype=prototype(list(self.data[reposity_keys.transaction_key()].values()))
            filtered_transaction_base_prototype=transaction_base_prototype.filter([filter_dto.create("range.uuid","eq",reference_object.uuid)])
            for transaction_object in filtered_transaction_base_prototype.data:
                self.data[reposity_keys.transaction_key()][transaction_object.uuid].range=reference_object

            remnant_base_prototype=prototype(list(self.data[reposity_keys.transaction_key()].values()))
            filtered_remnant_base_prototype=remnant_base_prototype.filter([filter_dto.create("range.uuid","eq",reference_object.uuid)])
            for remnant_obj in filtered_remnant_base_prototype.data:
                self.data[reposity_keys.transaction_key()][remnant_obj.uuid].range=reference_object
        elif isinstance(reference_object,range_group_model):
            range_base_prototype=prototype(list(self.data[reposity_keys.range_key()].values()))
            filtered_range_base_prototype=range_base_prototype.filter([filter_dto.create("group.uuid","eq",reference_object.uuid)])
            for range_object in filtered_range_base_prototype.data:
                self.data[reposity_keys.range_key()][range_object.uuid].group=reference_object
            
        elif isinstance(reference_object,storage_model):
            transaction_base_prototype=prototype(list(self.data[reposity_keys.transaction_key()].values()))
            filtered_transaction_base_prototype=transaction_base_prototype.filter([filter_dto.create("storage.uuid","eq",reference_object.uuid)])
            for transaction_object in filtered_transaction_base_prototype.data:
                self.data[reposity_keys.transaction_key()][transaction_object.uuid].storage=reference_object

            return True