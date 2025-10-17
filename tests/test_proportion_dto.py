
import pytest

from src.dto.proportion_dto import *
class TestProportionDTO:
    """
    Test for proportion_dto
    """
    
    def test_valid_proportion_dto_creation(self):
        """
        Test create of proportion_dto
        """
        proportion_dto_obj = proportion_dto()
        
        assert proportion_dto_obj.range_id == ""
        assert proportion_dto_obj.proportion_value == 1.0

    def test_valid_proportion_dto_set_properties(self):
        """
        Test of proportion_dto's set properties
        """
        proportion_dto_obj = proportion_dto()
        proportion_dto_obj.range_id="id"
        proportion_dto_obj.proportion_value=2.0
        
        assert proportion_dto_obj.range_id == "id"
        assert proportion_dto_obj.proportion_value == 2.0
