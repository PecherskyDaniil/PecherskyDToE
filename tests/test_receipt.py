import pytest

from src.models.receipt_model import *

class TestReceiptModel:
    
    @pytest.fixture
    def sample_ingredients(self):
        """
        Fixture of sample ingridients
        """
        range1 = range_model.create_flour()
        range2 = range_model.create_butter()
        return [
            proportion(range1, 2.0),
            proportion(range2, 1.5)
        ]
    
    @pytest.fixture
    def sample_steps(self):
        """
        Fixtur of sample steps
        """
        return [
            step("Шаг 1: Подготовить ингредиенты"),
            step("Шаг 2: Смешать все вместе"),
            step("Шаг 3: Запекать 30 минут")
        ]
    
    def test_valid_receipt_creation(self, sample_ingredients, sample_steps):
        """
        Test valid create receipt
        """
        receipt = receipt_model(
            name="Тестовый рецепт",
            ingridients=sample_ingredients,
            steps=sample_steps
        )
        
        assert receipt.name == "Тестовый рецепт"
        assert receipt.ingridients == sample_ingredients
        assert receipt.steps == sample_steps
    
    def test_valid_ingredients_setter(self, sample_ingredients):
        """
        Test valid set ingridients
        """
        receipt = receipt_model()
        receipt.ingridients = sample_ingredients
        
        assert receipt.ingridients == sample_ingredients
        assert len(receipt.ingridients) == 2
    
    def test_error_ingredients_setter(self):
        """
        Test error set ingridients
        """
        receipt = receipt_model()
        
        with pytest.raises(argument_exception):
            receipt.ingridients = "not_a_list"
    
    def test_error_ingredients_setter_element_type(self):
        """
        Test error set ingridients list
        """
        receipt = receipt_model()
        
        with pytest.raises(argument_exception):
            receipt.ingridients = ["not_a_proportion", 123]
    
    def test_valid_steps_setter(self, sample_steps):
        """
        Test valid set steps
        """
        receipt = receipt_model()
        receipt.steps = sample_steps
        
        assert receipt.steps == sample_steps
        assert len(receipt.steps) == 3
    
    def test_valid_steps_setter_none(self):
        """
        Test valid set none steps
        """
        receipt = receipt_model()
        receipt.steps = None
        
        assert receipt.steps is None
    
    def test_error_steps_setter(self):
        """
        Test error set steps
        """
        receipt = receipt_model()
        
        with pytest.raises(argument_exception, match="steps should be list of steps"):
            receipt.steps = "not_a_list"
    
    def test_error_steps_setter_element_type(self):
        """
        Test error set list steps
        """
        receipt = receipt_model()
        
        with pytest.raises(argument_exception):
            receipt.steps = ["not_a_step", 123]

    def test_valid_complete_receipt_workflow(self):
        """
        Test valid create full receipt
        """
        # Создаем шаги
        steps = [
            step("Подготовить ингредиенты"),
            step("Смешать в миске"),
            step("Выпекать при 180°C")
        ]
        
        # Создаем ингредиенты
        ingredients = [
            proportion(range_model.create_butter(), 2.0),
            proportion(range_model.create_flour(), 1.5),
            proportion(range_model.create_milk(), 100.0)
        ]
        
        # Создаем рецепт
        recipe = receipt_model(
            name="Торт Наполеон",
            ingridients=ingredients,
            steps=steps
        )
        
        # Проверяем целостность данных
        assert recipe.name == "Торт Наполеон"
        assert len(recipe.ingridients) == 3
        assert len(recipe.steps) == 3
        
        # Проверяем типы всех элементов
        assert all(isinstance(ing, proportion) for ing in recipe.ingridients)
        assert all(isinstance(stp, step) for stp in recipe.steps)
        
        # Проверяем значения
        assert recipe.ingridients[0].proportion_value == 2.0
        assert str(recipe.steps[0]) == "Подготовить ингредиенты"

    def test_valid_create_wafels(self):
        """
        Test valid create default wafels
        """
        wafels=receipt_model.create_wafels_receipt()
        assert wafels.name=="Вафли Хрустящие"
        assert len(wafels.steps)==8
        assert len(wafels.ingridients)==5

    def test_valid_create_hachapuri(self):
        """
        Test valid create default hachapuri
        """
        hachapuri=receipt_model.create_hachapuri()
        assert hachapuri.name=="Хачапури по Адыгейски"
        assert len(hachapuri.steps)==16
        assert len(hachapuri.ingridients)==10
    