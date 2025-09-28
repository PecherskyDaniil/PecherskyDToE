import pytest
import json

from src.models.abstract_reference import *
from src.models.company_model import company_model
from src.models.range_group_model import range_group_model
from src.models.range_model import range_model
from src.models.settings_model import settings_model
from src.models.unit_model import unit_model
from src.models.storage_model import storage_model
from src.settings_manager import settings_manager

class TestSettingsManager:
    """
    Tests of settings_manager
    """
    #проверка загрузки из класса settings
    def test_valid_create_manager_settings(self):
        """
        Test on normal create of settings_manager
        """
        #Создание
        file_name="./tests/test_dir/test_config2.json"
        manager=settings_manager(file_name)
        #Проверка
        assert manager.config_filename=="./tests/test_dir/test_config2.json"
    
    def test_valid_load_manager_settings_company_settings(self):
        """
        Test on normal load data of settings_manager from file
        """
        #Создание
        file_name="./tests/test_dir/test_config2.json"
        manager=settings_manager(file_name)
        #Проверка
        assert manager.load()==True
        assert manager.company_settings.name=="Moonshine"
        assert manager.company_settings.inn==123456789101
        assert manager.company_settings.account=="12345678910"
        assert manager.company_settings.coraccount=="12345678910"
        assert manager.company_settings.bic==123456789
        assert manager.company_settings.property_type=="OAOAO"
    
    def test_valid_wrong_config_filepath_manager_settings_company_settings(self):
        """
        Test on normal load error from empty file of settings_manager
        """
        #Создание
        file_name="./wrong_file_path.json"
        manager=settings_manager(file_name)
        #Проверка
        assert manager.load()==True
    
    def test_valid_wrong_config_file_manager_settings_company_settings(self):
        """
        Test on normal load error from wrong config_file of settings_manager
        """
        #Создание
        file_name="./tests/test_wrong_config.json"
        manager=settings_manager(file_name)
        #Проверка
        assert manager.load()==False
    