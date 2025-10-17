import pytest

from src.dto.range_dto import *

class TestRangeDTO:
    """
    Test for range_dto
    """
    
    def test_valid_range_dto_creation(self):
        """
        Test create of range_dto
        """
        range_dto_obj = range_dto()
        
        assert range_dto_obj.full_name == ""
        assert range_dto_obj.unit_id == ""
        assert range_dto_obj.group_id == ""

    def test_valid_range_dto_set_properties(self):
        """
        Test of range_dto's set properties
        """
        range_dto_obj = range_dto()
        range_dto_obj.full_name = "Test Range"
        range_dto_obj.unit_id = "unit123"
        range_dto_obj.group_id = "group456"
        
        assert range_dto_obj.full_name == "Test Range"
        assert range_dto_obj.unit_id == "unit123"
        assert range_dto_obj.group_id == "group456"