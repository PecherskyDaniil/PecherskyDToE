import pytest
import json

from src.models.abstract_reference import *
from src.models.range_group_model import range_group_model

class TestRangeGroupModel:
    """
    Tests of range_group_model
    """
    #проверка создания группы номенклатуры
    def test_valid_create_range_group(self):
        """
        Test on normal create of range_group_model
        """
        #Создание
        range_g=range_group_model("Stuff")
        #Проверка
        assert range_g.name=="Stuff"
    
    def test_valid_change_name_range_group(self):
        """
        Test on normal change name of range_group_model
        """
        #Создание
        range_g=range_group_model("Stuff")
        #Проверка
        assert range_g.name=="Stuff"
        range_g.name="Stuff2"
        assert range_g.name=="Stuff2"
    
    def test_error_set_wrong_length_name_range_group(self):
        """
        Test on error when name not fits limit of range_group_model
        """
        #Создание
        range_g=range_group_model("Stuff")
        #получение ошибки
        with pytest.raises(argument_exception):
            range_g.name="1"*51