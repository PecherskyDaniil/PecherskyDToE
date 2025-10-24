import pytest

from src.converters.basic_converter import basic_converter
from src.models.receipt_model import *
from src.models.unit_model import unit_model

@pytest.fixture
def sample_receipt():
    """
    Fixture of sample ingridients
    """
    range1 = range_model.create("A","A",unit_model.create("name",None,1.0),range_group_model.create("name"))
    range2 = range_model.create("B","B",unit_model.create("name",None,1.0),range_group_model.create("name"))
    receipt=receipt_model("myreceipt",
                        [proportion(range1, 2.0),
                        proportion(range2, 1.5)],
                        [
                            step("step1"),
                            step("step2")
                        ],
                        20.0)
    return receipt

class TestBasicConverter:
    """
    Test for basic_converter
    """
    
    def test_valid_convert_basic(self,sample_receipt:receipt_model):
        """
        Test convert basic
        """
        json_obj=basic_converter.convert(sample_receipt)
        # Проверяем, что объект создается без ошибок
        assert list(json_obj.keys())==["name","time","uuid"]

    