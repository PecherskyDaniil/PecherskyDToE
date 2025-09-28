import pytest
import json

from src.models.abstract_reference import *
from src.models.range_group_model import range_group_model
from src.models.range_model import range_model
from src.models.settings_model import settings_model
from src.models.unit_model import unit_model
from src.models.storage_model import storage_model
from src.settings_manager import settings_manager

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
