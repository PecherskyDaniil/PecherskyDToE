import pytest
from src.core.prototype import prototype
from src.logics.prototype_report import prototype_report
from src.logics.factory_entities import factory_entities
from src.settings_manager import settings_manager
from src.start_service import start_service
from src.reposity import reposity
import datetime
from src.dto.filter_dto import filter_dto
class TestPrototype:
    """
    Test for class prototype
    """
    def test_valid_clone_prototype(self):
        """
        Test on valid cloning prototype
        """
        list_obj=[1,2,3,4,5,6]
        prototype_obj=prototype(list_obj)
        new_prototype_obj=prototype_obj.clone(prototype_obj.data)
        assert prototype_obj is not new_prototype_obj
        assert prototype_obj.data == new_prototype_obj.data

    def test_valid_prototype_filter(self):
        """
        Test on valid filter prototype
        """
        start_service_instance=start_service()
        start_service_instance.start(True)
        start_prototype=prototype_report(list(start_service_instance.reposity.data[reposity.transaction_key()].values()))
        first_range=list(start_service_instance.reposity.data[reposity.range_key()].values())[0]
        storage_obj=start_service_instance.reposity.data[reposity.storage_key()]["Storage A"]
        filters=[
            filter_dto.create("range","eq",first_range),
            filter_dto.create("storage","eq",storage_obj)
        ]
        next_prototype=prototype_report.filter(start_prototype,filters)

        assert len(next_prototype.data)==365
        assert len(start_prototype.data)>=len(next_prototype.data)
    

    def test_valid_prototype_filter_ladder(self):
        """
        Test on valid filter ladder of prototypes
        """
        start_service_instance=start_service()
        start_service_instance.start(True)
        start_prototype=prototype_report(list(start_service_instance.reposity.data[reposity.transaction_key()].values()))
        first_range=list(start_service_instance.reposity.data[reposity.range_key()].values())[0]
        second_range=list(start_service_instance.reposity.data[reposity.range_key()].values())[1]
        filters1=[
            filter_dto.create("range","in",[first_range,second_range])
        ]
        filters2=[
            filter_dto.create("range","eq",first_range),
        ]
        next_prototype=prototype_report.filter(start_prototype,filters1)
        second_prototype=prototype_report.filter(next_prototype,filters2)
        assert len(next_prototype.data)>len(second_prototype.data)
        #assert len(start_prototype.data)>=len(next_prototype.data)
    
