import pytest
import json

from src.models.models import company_model
from src.settings_manager import settings_manager
class TestModels:
    #проверка создание основной модели
    #данные после создания должны быть пусты
    def test_check_create_model_company_model(self):
        #подготовка
        model=company_model()
        #Проверка
        assert model.name==""
    
    #Проверка создания модели и задания именя объекта
    def test_not_empty_create_model_company_model(self):
        #подготовка
        model=company_model()
        #задание имени
        model.name="test"
        #проверка
        assert model.name=="test"
    
    #Проверка передачи данных в модель из файла
    def test_load_create_model_company_model(self):
        #Чтение данных
        file_name="./tests/test_config.json"
        new_settings_manager=settings_manager(file_name)
        assert new_settings_manager.load()==True
        model=new_settings_manager.company_settings
        assert model.name=="Horns and Clops"
    
    #Проверка сравнения двух моделей при одинаковом наполнении
    def test_compare_models_create_model_company_model(self):
        #Чтение данных
        file_name="./tests/test_config.json"
        manager1=settings_manager(file_name)
        manager2=settings_manager(file_name)
        assert manager1.load()==True
        assert manager2.load()==True

        assert  manager2.company_settings==manager1.company_settings
    
    def test_convert_company_model(self):
        new_settings_manager=settings_manager()
        data={"company":{"name":"Horns and Clops", "inn":"123456789101","account":"12345678910","cor_account":"12345678910","bic":"123456789","property_type":"OAOAO"}}
        new_settings_manager.convert(data)
        assert new_settings_manager.company_settings.name=="Horns and Clops"

    def test_other_filepath_create_company_model(self):
        #Чтение данных
        file_name="./tests/test_dir/test_config2.json"
        manager=settings_manager(file_name)
        assert manager.load()==True

        assert  manager.company_settings.name=="Moonshine"
    
    def test_convert_company_model(self):
        new_settings_manager=settings_manager()
        data={"company":{"name":"Horns and Clops", "inn":"123456789101","account":"12345678910","cor_account":"12345678910","bic":"123456789","property_type":"OAOAO"}}
        new_settings_manager.convert(data)
        assert new_settings_manager.company_settings.name=="Horns and Clops"
    def test_parse_data_company_model(self):
        new_settings_manager=settings_manager()
        data={"company":{"name":"Horns and Clops", "inn":"123456789101","account":"12345678910","cor_account":"12345678910","bic":"123456789","property_type":"OAOAO"}}
        assert new_settings_manager.convert(data)==True
        data["company"]["inn"]="11"
        assert new_settings_manager.convert(data)==False
        data["company"]["inn"]="123456789101"
        data["company"]["property_type"]="OAOAOAOAOAOO"
        assert new_settings_manager.convert(data)==False
        data["company"]["property_type"]="OAOAA"
        data["company"]["account"]="1234567891110"
        assert new_settings_manager.convert(data)==False
        data["company"]["account"]="12345678911"
        data["company"]["cor_account"]="12345678910111111"
        assert new_settings_manager.convert(data)==False
        data["company"]["cor_account"]="12345678911"
        data["company"]["bic"]="12345654323456"
        assert new_settings_manager.convert(data)==False