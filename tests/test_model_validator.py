import pytest
import json

from src.models.abstract_reference import *

class TestModelValidator:
    """
    Tests for model_validator
    """
    def test_valid_create_model_validator(self):
        """
        Test on normal create model_validator
        """
        #Создание
        validator=model_validator([limit_model("name",Operator.EQ,10)])
        #Проверка
        assert len(validator.limits)==1
    
    def test_valid_set_different_size_of_limits_model_validator(self):
        """
        Test on normal create model_validator with many limits
        """
        #Создание
        validator=model_validator([limit_model("name",Operator.LE,50),limit_model("inn",Operator.EQ,12)])
        #Проверка
        assert validator.limits[0].name=="name"
        assert validator.limits[0].operator==Operator.LE
        assert validator.limits[0].value==50

        assert validator.limits[1].name=="inn"
        assert validator.limits[1].operator==Operator.EQ
        assert validator.limits[1].value==12
    
    def test_error_set_wrong_limits_model_validator(self):
        """
        Test on error model_validator when sets wrong limits
        """
        #получение ошибки
        with pytest.raises(argument_exception):
            validator=model_validator(1)
    
    def test_error_set_wrong_limits_inside_model_validator(self):
        """
        Test on error model_validator when sets wrong limits
        """
        #получение ошибки
        with pytest.raises(argument_exception):
            validator=model_validator([limit_model("name",Operator.LE,50),1])

    def test_valid_valid_property_model_validator(self):
        """
        Test on normal work of valid_property function of model_validator
        """
        #Создание
        validator=model_validator([limit_model("name",Operator.LE,50),limit_model("inn",Operator.EQ,12)])
        #Проверка
        assert validator.valid_property("name","1"*50)==True
        assert validator.valid_property("name","1"*51)==False
        assert validator.valid_property("inn","1"*12)==True
        assert validator.valid_property("inn","1"*50)==False
        assert validator.valid_property("wrong_name","1")==False
    
    def test_error_valid_property_empty_params_model_validator(self):
        """
        Test on error when empty params in valid_property function of model_validator
        """
        #Создание
        validator=model_validator([limit_model("name",Operator.LE,50),limit_model("inn",Operator.EQ,12)])
        #получение ошибки
        with pytest.raises(argument_exception):
            validator.valid_property(None,None)
    
    def test_valid_check_type_model_validator(self):
        """
        Test on normal work of check_type function of model_validator
        """
        #Создание
        validator=model_validator([limit_model("name",Operator.LE,50),limit_model("inn",Operator.EQ,12)])
        #Проверка
        assert validator.check_type(1,int)==True
        assert validator.check_type("wrong",int)==False

        