import pytest
import json

from src.models.abstract_reference import *
from src.models.range_group_model import range_group_model
from src.dto.range_group_dto import range_group_dto
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
        
    def test_valid_init_from_dto_range_group(self):
        """
        Test on valid init from dto object range_group_model
        """
        #Создание
        range_group_dto_obj=range_group_dto()
        range_group_dto_obj.name="Name"
        #Присваивание
        range_group_obj=range_group_model.from_dto(range_group_dto_obj,{})
        #Проверка
        assert range_group_dto_obj.name==range_group_obj.name
    
    def test_valid_convert_to_dto_range_group(self):
        """
        Test on valid convert to dto object range_group_model
        """
        #Создание
        range_group_obj=range_group_model("name")
        #Присваивание
        range_group_dto_obj=range_group_obj.to_dto()
        #Проверка
        assert range_group_dto_obj.name=="name"