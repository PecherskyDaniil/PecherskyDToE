import pytest

from src.models.step import *


class TestStep:
    """Тесты для класса step"""
    
    def test_step_creation_valid(self):
        """Тест создания шага с валидным описанием"""
        description = "Нарезать овощи"
        step_obj = step(description)
        
        assert step_obj.step_description == description
        assert str(step_obj) == description
    
    def test_step_setter_valid(self):
        """Тест сеттера с валидным значением"""
        step_obj = step("Старое описание")
        step_obj.step_description = "Новое описание"
        assert step_obj.step_description == "Новое описание"
    
    def test_step_setter_invalid_type(self):
        """Тест сеттера с невалидным типом"""
        step_obj = step("Нормальное описание")
        
        with pytest.raises(argument_exception, match="step_description can be only string"):
            step_obj.step_description = 123
    
    def test_step_str_representation(self):
        """Тест строкового представления"""
        step_obj = step("Перемешать ингредиенты")
        assert str(step_obj) == "Перемешать ингредиенты"
