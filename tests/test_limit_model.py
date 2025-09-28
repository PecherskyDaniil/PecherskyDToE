import pytest
import json

from src.models.abstract_reference import *

class TestLimitModel:
    """
    Tests for limit_model
    """
    def test_valid_create_limit_model(self):
        """
        Test on normal create of limit_model
        """
        #Создание
        model=limit_model("name",Operator.EQ,12)
        #Проверка
        assert model.name=="name"
        assert model.operator==Operator.EQ
        assert model.value==12
    
    def test_valid_change_name_limit_model(self):
        """
        Test on normal change name of limit_model
        """
        #Создание
        model=limit_model("name",Operator.EQ,12)
        #Проверка
        assert model.name=="name"
        model.name="new_name"
        assert model.name=="new_name"
    
    def test_error_set_wrong_name_limit_model(self):
        """
        Test on error when name is not fit limit of limit_model
        """
        #получение ошибки
        with pytest.raises(argument_exception):
            model=limit_model(1,Operator.EQ,12)
    
    def test_valid_change_operator_limit_model(self):
        """
        Test on normal change operator of limit_model
        """
        #Создание
        model=limit_model("name",Operator.EQ,12)
        #Проверка
        assert model.operator==Operator.EQ
        model.operator=Operator.GT
        assert model.operator==Operator.GT

    def test_error_set_wrong_operator_limit_model(self):
        """
        Test on error when operator is not fit type of limit_model
        """
        #получение ошибки
        with pytest.raises(argument_exception):
            model=limit_model("name","wrong",12)

    def test_valid_change_value_limit_model(self):
        """
        Test on normal change value of limit_model
        """
        #Создание
        model=limit_model("name",Operator.EQ,12)
        #Проверка
        assert model.value==12
        model.value=0
        assert model.value==0
    
    def test_error_set_empty_value_limit_model(self):
        """
        Test on error when value is empty of limit_model
        """
        #получение ошибки
        with pytest.raises(argument_exception):
            model=limit_model("name",Operator.EQ,None)
    
    @pytest.mark.parametrize(
        "limit_name,limit_operator,limit_value,wrong_value,valid_value",
        [("name",Operator.EQ,10,11,10),
         ("bic",Operator.GT,8,8,9),
         ("inn",Operator.LT,13,13,12),
         ("name",Operator.GE,5,4,5),
         ("name",Operator.LE,16,17,16),
         ("name",Operator.NE,10,10,1)]
    )
    def test_valid_check_all_operators_and_different_values_limit_model(self,limit_name,limit_operator,limit_value,wrong_value,valid_value):  
        """
        Test on normal check limits of limit_model
        """
        #Создание
        model=limit_model(limit_name,limit_operator,limit_value)  
        #Проверка  
        assert model.check_limit(wrong_value)==False
        assert model.check_limit(valid_value)==True

    
    
