import pytest
import json

from src.models.abstract_reference import *
from src.models.range_group_model import range_group_model
from src.models.range_model import range_model
from src.models.settings_model import settings_model
from src.models.unit_model import unit_model
from src.models.storage_model import storage_model
from src.settings_manager import settings_manager
from src.dto.storage_dto import storage_dto
class TestStorageModel:
    """
    Tests for storage_model
    """
    #проверка создания склада
    def test_valid_create_storage_model(self):
        """
        Test on normal create storage_model
        """
        #Создание
        storage=storage_model("mystorage")
        #Проверка
        assert storage.name=="mystorage"
    
    def test_valid_change_storage_name(self):
        """
        Test on normal change name storage_model
        """
        #Создание
        storage=storage_model("mystorage")
        #Проверка
        assert storage.name=="mystorage"
        storage.name="other storage"
        assert storage.name=="other storage"

    def test_error_set_name_with_wrong_length_for_storage_model(self):
        """
        Test on error when name length is not fit limit storage_model
        """
        #Создание
        storage=storage_model("mystorage")
        #получение ошибки
        with pytest.raises(argument_exception):
            storage.name="1"*51
    

    def test_valid_init_from_dto_storage(self):
        """
        Test on valid init from dto object storage_model
        """
        #Подготовка
        cache={}
        #Создание
        storage_dto_obj=storage_dto()
        storage_dto_obj.uuid="123"
        storage_dto_obj.name="AAA"
        #Присваивание
        storage_obj=storage_model.from_dto(storage_dto_obj,cache)

        #Проверка
        assert storage_obj.uuid=="123"
        assert storage_obj.name=="AAA"
    
    def test_valid_convert_to_dto_storage(self):
        """
        Test on valid convert to dto object storage_model
        """
        #Подготовка
        storage_obj=storage_model()
        storage_obj.name="AAA"
        storage_dto_obj=storage_obj.to_dto()
        #Проверка
        assert storage_dto_obj.name=="AAA"
