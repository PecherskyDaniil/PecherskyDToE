import pytest
import datetime

from src.converters.convert_factory import convert_factory
from src.reposity import reposity
from src.models.range_model import range_model
from src.models.unit_model import unit_model
from src.models.range_group_model import range_group_model
@pytest.fixture
def simple_valid_data():
    return [
            range_model("name1","The Name1",unit_model("gramm",None,1.0),range_group_model("products")),
            range_model("name2","The Name2",unit_model("litr",None,5.0),range_group_model("drinks")),
            ]
class TestConvertFactory:
    """
    Test for convert_factory
    """
    
    def test_valid_convert_factory_object(self,simple_valid_data):
        """
        Test convert factory
        """
        c_f=convert_factory()
        dict_obj=c_f.convert(simple_valid_data)
        # Проверяем, что объект создается без ошибок
        assert len(dict_obj)==2
        assert dict_obj[0]["name"]=="name1"
        assert dict_obj[1]["full_name"]=="The Name2"

    