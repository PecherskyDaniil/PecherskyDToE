import pytest
import datetime

from src.logics.reference_service import reference_service
from src.start_service import *
from src.core.observe_service import observe_service
from src.core.event_type import event_type
from src.core.reposity_keys import reposity_keys
from src.logics.unit_service import unit_service
from src.logics.range_service import range_service
from src.logics.range_group_service import range_group_service
from src.logics.receipt_service import receipt_service
from src.logics.transaction_service import transaction_service
from src.logics.storage_service import storage_service
from src.logics.remnant_service import remnant_service
@pytest.fixture
def sample_start_service():
    #observe_service.handlers=[]

    s_s=start_service()
    s_s.block_datetime=datetime.datetime(2024,10,1)
    s_s.start()
    return s_s

class TestReferenceService:
    """
    Tests for reference_service
    """

    def test_valid_reference_service_add_object(self,sample_start_service):
        """
        Test valid add object
        """
        #Создание
        new_range=range_model.create("aa1",
                                     "AAA1",
                                     list(sample_start_service.reposity.data[reposity_keys.unit_key()].values())[0],
                                     list(sample_start_service.reposity.data[reposity_keys.range_group_key()].values())[0])
        #Добавление
        result=reference_service.add(sample_start_service,new_range)
        #Проверка
        assert result==True
        assert sample_start_service.reposity.data[reposity_keys.range_key()][new_range.uuid]==new_range
        #Добавление
        result2=reference_service.add(sample_start_service,new_range)
        #Проверка
        assert result2==False

    
    def test_valid_reference_service_delete_object(self,sample_start_service):
        """
        Test valid delete object
        """
        #Создание
        new_unit=unit_model.create("new_unit2",None,1.0)
        new_range=range_model.create("aa3",
                                     "AAA3",
                                     new_unit,
                                     list(sample_start_service.reposity.data[reposity_keys.range_group_key()].values())[0])
        #Добавление
        reference_service.add(sample_start_service,new_unit)
        reference_service.add(sample_start_service,new_range)
        #Проверка
        assert new_unit.uuid in sample_start_service.reposity.data[reposity_keys.unit_key()].keys()
        assert new_range.uuid in sample_start_service.reposity.data[reposity_keys.range_key()].keys()

        #Удаление
        result1=reference_service.delete(sample_start_service,new_unit)
        #Проверка
        assert result1==False
        assert new_unit.uuid in sample_start_service.reposity.data[reposity_keys.unit_key()].keys()

        #Удаление
        result2=reference_service.delete(sample_start_service,new_range)
        #Проверка
        assert result2==True
        assert not(new_range.uuid in sample_start_service.reposity.data[reposity_keys.range_key()].keys())

        #Удаление
        result3=reference_service.delete(sample_start_service,new_unit)
        #Проверка
        assert result3==True
        assert not(new_unit.uuid in sample_start_service.reposity.data[reposity_keys.unit_key()].keys())


    def test_valid_reference_service_change_object(self,sample_start_service):
        """
        Test valid change object
        """
        #Создание
        new_unit=unit_model.create("new_unit",None,1.0)
        new_range=range_model.create("aa2",
                                     "AAA2",
                                     new_unit,
                                     list(sample_start_service.reposity.data[reposity_keys.range_group_key()].values())[0])
        #Добавление
        reference_service.add(sample_start_service,new_unit)
        reference_service.add(sample_start_service,new_range)
        #Проверка
        assert sample_start_service.reposity.data[reposity_keys.unit_key()][new_unit.uuid].coef==1.0
        assert sample_start_service.reposity.data[reposity_keys.range_key()][new_range.uuid].unit.coef==1.0
        #Создание
        changed_unit=unit_model.create("new_unit",None,2.0)
        changed_unit.uuid=new_unit.uuid
        
        #Изменение
        result=reference_service.change(sample_start_service,changed_unit)
        #Проверка
        assert result==True
        assert sample_start_service.reposity.data[reposity_keys.unit_key()][new_unit.uuid].coef==2.0
        assert sample_start_service.reposity.data[reposity_keys.range_key()][new_range.uuid].unit.coef==2.0
    