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
