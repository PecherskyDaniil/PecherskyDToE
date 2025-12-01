import pytest
import datetime
from src.core.abstract_reference import argument_exception
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
        dt=datetime.datetime.now()
        assert datetime_converter.convert(dt).split("-")[0]==str(dt.year)

    def text_error_convert_datetime(self):
        """
        Test convert error datetime
        """
        dt="datetime.datetime.now()"
        with pytest.raises(argument_exception):
            datetime_converter.convert(dt)