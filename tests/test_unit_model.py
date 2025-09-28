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
    