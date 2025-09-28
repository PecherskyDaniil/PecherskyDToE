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

@pytest.fixture
def valid_example_company_model():
    """
    Fixture for example data
    """
    return {"company":{"name":"Horns and Clops", "inn":"123456789101","account":"12345678910","coraccount":"12345678910","bic":"123456789","property_type":"OAOAO"}}

class TestCompanyModel:
    """
    Tests of company_model
    """
    def create_company_example_data(self,lengths:dict):
        """
        Function that creates example data of company_model dictionary
        """
        example_data={}
        for prop in lengths.keys():
            example_data[prop]="1"*lengths[prop]
        answer={}
        answer["company"]=example_data
        return answer
    
    def test_valid_create_empty_model_company_model(self):
        """
        Test on normal create of empty name company_model
        """
        #подготовка
        model=company_model()
        #Проверка
        assert model.name==""
    
    #Проверка создания модели и задания именя объекта
    def test_valid_create_not_empty_name_model_company_model(self):
        """
        Test on normal create of not empty name company_model
        """
        #подготовка
        model=company_model()
        #задание имени
        model.name="test"
        #проверка
        assert model.name=="test"
    
    def test_valid_create_with_params_company_model(self,valid_example_company_model):
        """
        Test on normal create of company_model with params in init
        """
        #Создание
        modelq=company_model(name=valid_example_company_model["company"]["name"],
                            inn=int(valid_example_company_model["company"]["inn"]),
                            account=valid_example_company_model["company"]["account"],
                            coraccount=valid_example_company_model["company"]["coraccount"],
                            bic=int(valid_example_company_model["company"]["bic"]),
                            property_type=valid_example_company_model["company"]["property_type"])
        #Проверка
        assert modelq.name==valid_example_company_model["company"]["name"]
        assert modelq.inn==int(valid_example_company_model["company"]["inn"])
        assert modelq.account==valid_example_company_model["company"]["account"]
        assert modelq.coraccount==valid_example_company_model["company"]["coraccount"]
        assert modelq.bic==int(valid_example_company_model["company"]["bic"])
        assert modelq.property_type==valid_example_company_model["company"]["property_type"]
        #Создание
        modelw=company_model(valid_example_company_model["company"]["name"],
                            int(valid_example_company_model["company"]["inn"]),
                            valid_example_company_model["company"]["account"],
                            valid_example_company_model["company"]["coraccount"],
                            int(valid_example_company_model["company"]["bic"]),
                            valid_example_company_model["company"]["property_type"])
        #Проверка
        assert modelw.name==valid_example_company_model["company"]["name"]
        assert modelw.inn==int(valid_example_company_model["company"]["inn"])
        assert modelw.account==valid_example_company_model["company"]["account"]
        assert modelw.coraccount==valid_example_company_model["company"]["coraccount"]
        assert modelw.bic==int(valid_example_company_model["company"]["bic"])
        assert modelw.property_type==valid_example_company_model["company"]["property_type"]


    def test_error_create_with_wrong_inn_and_bic_company_model(self,valid_example_company_model):
        """
        Test on error when inn or bic is not int company_model
        """
        #получение ошибки
        with pytest.raises(argument_exception):
            model=company_model(name=valid_example_company_model["company"]["name"],
                                inn="a"*12,
                                account=valid_example_company_model["company"]["account"],
                                coraccount=valid_example_company_model["company"]["coraccount"],
                                bic=int(valid_example_company_model["company"]["bic"]),
                                property_type=valid_example_company_model["company"]["property_type"])
        #получение ошибки    
        with pytest.raises(argument_exception):
            model=company_model(name=valid_example_company_model["company"]["name"],
                                inn=int("1"*12),
                                account=valid_example_company_model["company"]["account"],
                                coraccount=valid_example_company_model["company"]["coraccount"],
                                bic="a"*12,
                                property_type=valid_example_company_model["company"]["property_type"])
        
    def test_error_create_with_wrong_amount_params(self):
        """
        Test on error when wrong params company_model
        """
        #получение ошибки
        with pytest.raises(argument_exception):
            model=company_model(1,2,3,4,5,6,7,8,9)
    
    #Проверка сравнения двух моделей при одинаковом наполнении
    def test_valid_compare_models_create_model_company_model(self):
        """
        Test on normal same load from settings_manager company_model
        """
        #Чтение данных
        file_name="./tests/test_config.json"
        manager1=settings_manager(file_name)
        manager2=settings_manager(file_name)
        #Проверка
        assert manager1.load()==True
        assert manager2.load()==True

        assert  manager2.company_settings==manager1.company_settings
    

    #Проверка передачи данных в модель из файла
    def test_valid_load_model_company_model_from_settings_manager(self):
        """
        Test on normal load from settings_manager company_model
        """
        #Чтение данных
        file_name="./tests/test_config.json"
        new_settings_manager=settings_manager(file_name)
        #Проверка
        assert new_settings_manager.load()==True
        model=new_settings_manager.company_settings
        assert model.name=="Horns and Clops"

    #проверка всех ограничений параметров
    def test_error_load_wrong_data_company_model_from_settings_manager(self):
        """
        Test on error when data not fits limits company_model
        """
        #Создание
        new_settings_manager=settings_manager()
        company_limits={"name":50,"inn":12,"account":11,"coraccount":11,"bic":9,"property_type":5}
        data=self.create_company_example_data(company_limits)
        #Проверка
        assert new_settings_manager.convert(data)==True
        for property in company_limits.keys():
            bad_lengths=company_limits.copy()
            bad_lengths[property]=company_limits[property]+1
            data=self.create_company_example_data(bad_lengths)
            assert new_settings_manager.convert(data)==False

    #проверка загрузки данных в организацию из словаря
    def test_valid_load_company_model_from_dict(self,valid_example_company_model):
        """
        Test on normal load params from dict company_model
        """
        #Создание
        new_settings_manager=settings_manager()
        new_settings_manager.convert(valid_example_company_model)
        #Проверка
        assert new_settings_manager.company_settings.name=="Horns and Clops"

    #проверка загрузки из другого пути
    def test_valid_load_company_model_from_different_filepath(self):
        """
        Test on normal load from settings_manager different filepath company_model
        """
        #Чтение данных
        file_name="./tests/test_dir/test_config2.json"
        manager=settings_manager(file_name)
        #Проверка
        assert manager.load()==True
        assert  manager.company_settings.name=="Moonshine"

    
    #проверка загрузки из класса settings
    def test_valid_load_from_settings_company_model(self):
        """
        Test on normal load from settings_manager different filepath company_model
        """
        #Создание
        file_name="./tests/test_dir/test_config2.json"
        manager=settings_manager(file_name)
        #Проверка
        assert manager.load()==True
        company2=company_model(manager.company_settings)
        assert company2.name=="Moonshine"
        assert company2.inn==123456789101
        assert company2.account=="12345678910"
        assert company2.coraccount=="12345678910"
        assert company2.bic==123456789
        assert company2.property_type=="OAOAO"
    
    def test_error_input_not_settings_company_model(self):
        """
        Test on error when params is None company_model
        """
        #получение ошибки
        with pytest.raises(argument_exception):
            company=company_model(None)
