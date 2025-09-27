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
class TestModels:
    #проверка создание основной модели
    #данные после создания должны быть пусты

    def create_company_example_data(self,lengths:dict):
        example_data={}
        for prop in lengths.keys():
            example_data[prop]="1"*lengths[prop]
        answer={}
        answer["company"]=example_data
        return answer
    
    def test_check_create_model_company_model(self):
        #подготовка
        model=company_model()
        print(dir(model))
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
    
    #проверка загрузки данных в организацию из словаря
    def test_convert_company_model(self):
        new_settings_manager=settings_manager()
        data={"company":{"name":"Horns and Clops", "inn":"123456789101","account":"12345678910","cor_account":"12345678910","bic":"123456789","property_type":"OAOAO"}}
        new_settings_manager.convert(data)
        assert new_settings_manager.company_settings.name=="Horns and Clops"

    #проверка загрузки из другого пути
    def test_other_filepath_create_company_model(self):
        #Чтение данных
        file_name="./tests/test_dir/test_config2.json"
        manager=settings_manager(file_name)
        assert manager.load()==True

        assert  manager.company_settings.name=="Moonshine"
    #проверка всех ограничений параметров
    def test_parse_data_company_model(self):
        new_settings_manager=settings_manager()
        company_limits={"name":50,"inn":12,"account":11,"coraccount":11,"bic":9,"property_type":5}
        data=self.create_company_example_data(company_limits)
        assert new_settings_manager.convert(data)==True
        for property in company_limits.keys():
            bad_lengths=company_limits.copy()
            bad_lengths[property]=company_limits[property]+1
            data=self.create_company_example_data(bad_lengths)
            assert new_settings_manager.convert(data)==False
    
    #проверка создания склада
    def test_create_storage(self):
        storage=storage_model("mystorage")
        assert storage.name=="mystorage"
        storage.name="other storage"
        assert storage.name=="other storage"
        with pytest.raises(argument_exception):
            storage.name="1"*51
    #проверка создания группы номенклатуры
    def test_create_range_group(self):
        range_g=range_group_model("Stuff")
        assert range_g.name=="Stuff"
        range_g.name="Stuff2"
        assert range_g.name=="Stuff2"
        with pytest.raises(argument_exception):
            range_g.name="1"*51
    #проверка создания единицы измерения
    def test_create_unit(self):
        gramm=unit_model("gramm",None,1)
        kg=unit_model("kilogramm",gramm,1000)
        assert kg.print_eq_coef() == "1 kilogramm = 1000 gramm"
        with pytest.raises(argument_exception):
            kg.name="1"*51
    #проверка создания номенклатуры
    def test_create_range(self):
        mls=unit_model("mls",None,1)
        litr=unit_model("litr",mls,1000)
        range_g=range_group_model("Food")
        new_range=range_model("Milk","Cow milk",litr,range_g)
        assert new_range.name=="Milk"
        assert new_range.full_name=="Cow milk"
        assert new_range.unit.print_eq_coef()=="1 litr = 1000 mls"

        with pytest.raises(argument_exception):
            new_range.name="1"*51

        with pytest.raises(argument_exception):
            new_range.full_name="1"*256
    
    #проверка загрузки из класса settings
    def test_load_from_settings(self):
        file_name="./tests/test_dir/test_config2.json"
        manager=settings_manager(file_name)
        assert manager.load()==True
        company2=company_model(manager.company_settings)
        assert company2.name=="Moonshine"
        assert company2.inn==123456789101
        assert company2.account=="12345678910"
        assert company2.coraccount=="12345678910"
        assert company2.bic==123456789
        assert company2.property_type=="OAOAO"

    #проверка uuid
    def test_inputs_storage_model_create(self):
        #Подготовка
        storage1 = storage_model("storage1")
        storage1.uuid="uuid1"
        storage2 = storage_model("storage2")
        storage2.uuid="uuid1"
        #Действие
        assert storage1==storage2