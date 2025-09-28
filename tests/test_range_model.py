import pytest
import json

from src.models.abstract_reference import *
from src.models.range_group_model import range_group_model
from src.models.range_model import range_model
from src.models.unit_model import unit_model

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

    