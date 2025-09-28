import pytest
import json

from src.models.abstract_reference import *

class TestAbstractReference:
    """
    Tests of abstract_reference
    """
    def test_valid_create_abstract_reference(self):
        """
        Test on normal create of abstract_reference
        """
        #Создание
        model=abstract_reference("new_name")
        #Проверка
        assert model.name=="new_name"
    
    def test_valid_change_name_abstract_reference(self):
        """
        Test on normal change name of abstract_reference
        """
        #Создание
        model=abstract_reference("old_name")
        #Проверка
        assert model.name=="old_name"
        model.name="new_name"
        assert model.name=="new_name"
    
    def test_error_set_wrong_name_abstract_reference(self):
        """
        Test on error when sets name of abstract_reference with wrong length
        """
        #получение ошибки
        with pytest.raises(argument_exception):
            model=abstract_reference("w"*51)

    def test_valid_unique_uuid_abstract_reference(self):
        """
        Test on normal check unique uuid of abstract_reference
        """
        #Создание
        model1=abstract_reference("instance")
        model2=abstract_reference("instance")
        #Проверка
        assert model1.uuid!=model2.uuid
    
    def test_valid_set_other_uuid_abstract_reference(self):
        """
        Test on normal sets of uuid of abstract_reference
        """
        #Создание
        model1=abstract_reference("instance1")
        model1.uuid="same"
        #Проверка
        assert model1.uuid=="same"

    def test_valid_compare_objects_by_uuid_abstract_reference(self):
        """
        Test on normal compare of abstract_reference
        """
        #Создание
        model1=abstract_reference("instance1")
        model2=abstract_reference("instance2")
        #Проверка
        assert model1!=model2
        model1.uuid="same"
        model2.uuid="same"
        assert model1==model2
    
    def test_error_set_empty_uuid_abstract_reference(self):
        """
        Test on error when trying set empty uuid of abstract_reference
        """
        #Создание
        model1=abstract_reference("instance1")
        #получение ошибки
        with pytest.raises(argument_exception):
            model1.uuid=""

        