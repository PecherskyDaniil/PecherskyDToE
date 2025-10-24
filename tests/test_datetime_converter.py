import pytest
import datetime

from src.converters.datetime_converter import datetime_converter
class SampleObject:
    """
    Class for testing datetime converting
    """
    def __init__(self):
        self.datetime_of_creation=datetime.datetime.now()
        self.name="sample_name"

    @property
    def datetime_of_creation(self):
        return self.__datetime_of_creation
    
    @datetime_of_creation.setter
    def datetime_of_creation(self,value:datetime.datetime):
        self.__datetime_of_creation=value
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value:str):
        self.__name=value

class TestDatetimeConverter:
    """
    Test for basic_converter
    """
    
    def test_valid_convert_datetime(self):
        """
        Test convert datetime
        """
        obj=SampleObject()
        json_obj=datetime_converter.convert(obj)
        # Проверяем, что объект создается без ошибок
        assert "datetime_of_creation" in json_obj.keys()
        assert "name" not in json_obj.keys()

    