import pytest

from src.dto.unit_dto import *

class TestUnitDTO:
    """
    Test for unit_dto
    """
    
    def test_valid_unit_dto_creation(self):
        """
        Test create of unit_dto
        """
        unit_dto_obj = unit_dto()
        
        assert unit_dto_obj.base_id is None
        assert unit_dto_obj.coef == 1

    def test_valid_unit_dto_set_properties(self):
        """
        Test of unit_dto's set properties
        """
        unit_dto_obj = unit_dto()
        unit_dto_obj.base_id = "gram"
        unit_dto_obj.coef = 1000
        
        assert unit_dto_obj.base_id == "gram"
        assert unit_dto_obj.coef == 1000