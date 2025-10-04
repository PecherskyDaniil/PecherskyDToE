import pytest
import json

from src.models.abstract_reference import *
from src.models.unit_model import unit_model

class TestUnitModel:
    """
    Tests for unit_model
    """
    #проверка создания единицы измерения
    def test_valid_create_unit_model(self):
        """
        Test on normal create of unit_model
        """
        #Создание
        gramm=unit_model("gramm",None,1.0)
        #Проверка
        assert str(gramm)=="gramm"

    def test_valid_set_base_unit_to_other_unit_model(self):
        """
        Test on normal create of unit_model with base_unit
        """
        #Создание
        gramm=unit_model("gramm",None,1.0)
        kg=unit_model("kilogramm",gramm,1000.0)
        #Проверка
        assert kg.print_eq_coef() == "1 kilogramm = 1000.0 gramm"

    def test_error_set_wrong_length_name_unit_model(self):
        """
        Test on error when set name with wrong length name of unit_model
        """
        #Создание
        gramm=unit_model("gramm",None,1.0)
        kg=unit_model("kilogramm",gramm,1000.0)
        #получение ошибки
        with pytest.raises(argument_exception):
            kg.name="1"*51
    
    def test_error_set_wrong_base_unit_unit_model(self):
        """
        Test on error when set name with wrong base_unit of unit_model
        """
        #получение ошибки
        with pytest.raises(argument_exception):
            kg=unit_model("kilogramm",12,1000.0)

    def test_error_set_wrong_coef_unit_model(self):
        """
        Test on error when set name with wrong coef of unit_model
        """
        #получение ошибки
        with pytest.raises(argument_exception):
            gramm=unit_model("gramm",None,"wrong")    
    
    def test_valid_create_static_func_unit_model(self):
        """
        Test valid create unit
        """
        unit=unit_model.create("мегаграмм",None,1.0)
        assert unit.name=="мегаграмм"
        assert unit.base_unit is None
        assert unit.coef==1.0
    
    def test_valid_create_gramm_unit_model(self):
        """
        Test valid create default gramm unit
        """
        gramm_unit = unit_model.create_gramm()
        assert gramm_unit.name == "грамм"
        assert gramm_unit.base_unit is None
        assert gramm_unit.coef == 1.0
    
    def test_valid_create_killogramm_unit_model(self):
        """
        Test valid create default killogramm unit
        """
        kilogram_unit = unit_model.create_killogramm()
        gramm_unit = unit_model.create_gramm()
        
        assert kilogram_unit.name == "килограмм"
        assert kilogram_unit.base_unit is not None
        assert kilogram_unit.base_unit.name == "грамм"
        assert kilogram_unit.coef == 1000.0
    
    def test_valid_create_litr_unit_model(self):
        """
        Test valid create default litr unit
        """
        litr_unit = unit_model.create_litr()
        
        assert litr_unit.name == "литр"
        assert litr_unit.base_unit is None
        assert litr_unit.coef == 1.0
    
    def test_valid_create_millilitr_unit_model(self):
        """
        Test valid create default millilitr unit
        """
        milliliter_unit = unit_model.create_millilitr()
        litr_unit = unit_model.create_litr()
        
        assert milliliter_unit.name == "миллилитр"
        assert milliliter_unit.base_unit is not None
        assert milliliter_unit.base_unit.name == "литр"
        assert milliliter_unit.coef == 0.001
    
    def test_valid_create_item_unit_model(self):
        """
        Test valid create default item unit
        """
        item_unit = unit_model.create_item()
        
        assert item_unit.name == "штука"
        assert item_unit.base_unit is None
        assert item_unit.coef == 1.0
    
    def test_valid_singleton_behavior(self):
        """
        Test valid singleton behaivor
        """
        # Проверяем, что декоратор singleton_result работает корректно
        gramm_unit1 = unit_model.create_gramm()
        gramm_unit2 = unit_model.create_gramm()
        
        kilogram_unit1 = unit_model.create_killogramm()
        kilogram_unit2 = unit_model.create_killogramm()
        
        # Должны возвращаться одни и те же объекты
        assert gramm_unit1 is gramm_unit2
        assert kilogram_unit1 is kilogram_unit2
    
    def test_valid_units_hierarchy(self):
        """
        Test valid unit hierarchy
        """
        # Проверяем иерархию единиц измерения
        kilogram_unit = unit_model.create_killogramm()
        gramm_unit = unit_model.create_gramm()
        
        milliliter_unit = unit_model.create_millilitr()
        litr_unit = unit_model.create_litr()
        
        # Килограмм должен ссылаться на грамм как базовую единицу
        assert kilogram_unit.base_unit is gramm_unit
        
        # Миллилитр должен ссылаться на литр как базовую единицу
        assert milliliter_unit.base_unit is litr_unit
    