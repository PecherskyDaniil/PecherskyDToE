import pytest
import json

from src.logics.factory_entities import factory_entities
from src.logics.response_csv import response_csv
from src.logics.response_json import response_json
from src.logics.response_xml import response_xml
from src.logics.response_markdown import response_markdown
from src.models.abstract_reference import argument_exception,operation_exception
class TestFactoryEntities:
    """
    Tests for factory_entities
    """
    def test_valid_create_factory_entities(self):
        """
        Test on valid create factory_entities
        """
        #Создание
        fe_instance=factory_entities()
        fe_instance.default_value="xml"
        #Проверка
        assert fe_instance.default_value=="xml"

    def test_valid_set_params_factory_entities(self):
        """
        Test on valid set params factory_entities
        """
        #Создание
        fe_instance=factory_entities()
        fe_instance.default_value="xml"
        #Проверка
        assert fe_instance.default_value=="xml"
    
    def test_valid_func_create_factory_entities(self):
        """
        Test on valid func create factory_entities
        """
        #Создание
        fe_instance=factory_entities()
        #Проверка
        assert fe_instance.create("xml")==response_xml
        assert fe_instance.create("csv")==response_csv
        assert fe_instance.create("json")==response_json
        assert fe_instance.create("markdown")==response_markdown
    
    def test_valid_func_create_default_factory_entities(self):
        """
        Test on valid func create factory_entities
        """
        #Создание
        fe_instance=factory_entities()
        fe_instance.default_value="xml"
        #Проверка
        assert fe_instance.create_default()==response_xml
        #Создание
        fe_instance=factory_entities()
        fe_instance.default_value="csv"
        #Проверка
        assert fe_instance.create_default()==response_csv
        #Создание
        fe_instance=factory_entities()
        fe_instance.default_value="json"
        #Проверка
        assert fe_instance.create_default()==response_json
        #Создание
        fe_instance=factory_entities()
        fe_instance.default_value="markdown"
        #Проверка
        assert fe_instance.create_default()==response_markdown
    
    def test_error_create_factory_entities(self):
        """
        Test on error func create factory_entities
        """
        fe_instance=factory_entities()
        with pytest.raises(operation_exception):
            fe_instance.create("wrong")
    
    def test_error_create_default_factory_entities(self):
        """
        Test on error func create default factory_entities
        """
        
        with pytest.raises(operation_exception):
            fe_instance=factory_entities()
            fe_instance.default_value="wrong"