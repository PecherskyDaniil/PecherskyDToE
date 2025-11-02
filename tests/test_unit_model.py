import pytest
import json

from src.models.abstract_reference import *
from src.models.unit_model import unit_model
from src.dto.unit_dto import unit_dto
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
    
    def test_valid_init_from_dto_range(self):
        """
        Test on valid init from dto object unit_model
        """
        #Подготовка
        cache={
            "123":unit_model("gramm",None,1.0),
        }
        #Создание
        unit_dto_obj=unit_dto()
        unit_dto_obj.name="kilo"
        unit_dto_obj.base_id="123"
        unit_dto_obj.coef=1000.0
        unit_dto_obj.uuid="112233"
        #Присваивание
        unit_obj=unit_model.from_dto(unit_dto_obj,cache)
        #Проверка
        assert unit_obj.name=="kilo"
        assert unit_obj.base_unit is cache["123"]
        assert unit_obj.coef == 1000.0
    
    def test_valid_convert_to_dto_unit(self):
        """
        Test on valid convert to dto object unit_model
        """
        cache={
            "123":unit_model("gramm",None,1.0),
        }
        #Создание
        unit_obj=unit_model("kilo",cache["123"],1000.0)
        #Присваивание
        unit_dto_obj=unit_obj.to_dto()
        #Проверка
        assert unit_dto_obj.name=="kilo"
        assert unit_dto_obj.base_id==cache["123"].uuid
        assert unit_dto_obj.coef==1000.0
        
    def test_valid_get_base_function(self):
        """
        Test on valid get base function work
        """
        #Подготовка
        unit1=unit_model("a",None,1.0)
        unit2=unit_model("b",unit1,100.0)
        #проверка
        assert unit1.get_base()==("a",1.0)
        assert unit2.get_base()==("a",100.0)
    