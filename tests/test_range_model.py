import pytest
import json

from src.core.abstract_reference import *
from src.models.range_group_model import range_group_model
from src.models.range_model import range_model
from src.models.unit_model import unit_model
from src.dto.range_dto import range_dto
from src.reposity import reposity
from src.core.reposity_keys import reposity_keys
class TestRangeModel:
    """
    Tests of range_model
    """
    #проверка создания номенклатуры
    def test_valid_create_range_model(self):
        """
        Test on normal create of range_model
        """
        #Создание
        mls=unit_model("mls",None,1.0)
        litr=unit_model("litr",mls,1000.0)
        range_g=range_group_model("Food")
        new_range=range_model("Milk","Cow milk",litr,range_g)
        #Проверка
        assert new_range.name=="Milk"
        assert new_range.full_name=="Cow milk"
        assert new_range.unit.print_eq_coef()=="1 litr = 1000.0 mls"
    
    def test_error_wrong_name_length_range_model(self):
        """
        Test on error when name length not fits of range_model
        """
        #Создание
        mls=unit_model("mls",None,1.0)
        litr=unit_model("litr",mls,1000.0)
        range_g=range_group_model("Food")
        new_range=range_model("Milk","Cow milk",litr,range_g)
        #получение ошибки
        with pytest.raises(argument_exception):
            new_range.name="1"*51

    def test_error_wrong_full_name_length_range_model(self):
        """
        Test on error when full name length not fits in limits of range_model
        """
        #Создание
        mls=unit_model("mls",None,1.0)
        litr=unit_model("litr",mls,1000.0)
        range_g=range_group_model("Food")
        new_range=range_model("Milk","Cow milk",litr,range_g)
        #получение ошибки
        with pytest.raises(argument_exception):
            new_range.full_name="1"*256

    def test_error_wrong_unit_range_model(self):
        """
        Test on error when unit not fits in limits of range_model
        """
        #Создание
        range_g=range_group_model("Food")
        #получение ошибки
        with pytest.raises(argument_exception):
            new_range=range_model("Milk","Cow milk","wrong",range_g)

    def test_error_wrong_range_group_range_model(self):
        """
        Test on error when range group not fits in limits of range_model
        """
        #Создание
        mls=unit_model("mls",None,1.0)
        litr=unit_model("litr",mls,1000.0)
        #получение ошибки
        with pytest.raises(argument_exception):
            new_range=range_model("Milk","Cow milk",litr,"wrong")
    
    def test_valid_create_method_directly(self):
        """
        Test create instance range
        """
        # Тестируем базовый метод create напрямую
        test_unit = unit_model.create("gramm",None,1.0)
        test_group = range_group_model.create("ingridients")
        
        custom_item = range_model.create("тест", "Тестовый продукт", test_unit, test_group)
        
        assert custom_item.name == "тест"
        assert custom_item.full_name == "Тестовый продукт"
        assert custom_item.unit is test_unit
        assert custom_item.group is test_group
    

    def test_valid_init_from_dto_range(self):
        """
        Test on valid init from dto object range_model
        """
        #Подготовка
        cache={
            reposity_keys.unit_key():{"123":unit_model("gramm",None,1.0)},
            reposity_keys.range_group_key():{"234":range_group_model("products")}
        }
        #Создание
        range_dto_obj=range_dto()
        range_dto_obj.name="Cheese"
        range_dto_obj.group_id="234"
        range_dto_obj.unit_id="123"
        range_dto_obj.full_name="Mega Cheese"
        range_dto_obj.uuid="112233"
        #Присваивание
        range_obj=range_model.from_dto(range_dto_obj,cache)
        #Проверка
        assert range_obj.name=="Cheese"
        assert range_obj.full_name=="Mega Cheese"
        assert range_obj.group is cache[reposity_keys.range_group_key()]["234"]
        assert range_obj.unit is cache[reposity_keys.unit_key()]["123"]
    
    def test_valid_convert_to_dto_range_group(self):
        """
        Test on valid convert to dto object range_group_model
        """
        #Создание
        range_obj=range_model("Cheese","Mega Cheese",unit_model("gramm",None,1.0),range_group_model("products"))
        #Присваивание
        range_dto_obj=range_obj.to_dto()
        #Проверка
        assert range_dto_obj.name=="Cheese"
        assert range_dto_obj.full_name=="Mega Cheese"
        assert range_dto_obj.unit_id==range_obj.unit.uuid
        assert range_dto_obj.group_id==range_obj.group.uuid