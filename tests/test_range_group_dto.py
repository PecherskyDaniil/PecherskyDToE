import pytest

from src.dto.range_group_dto import *

class TestRangeGroupDTO:
    """
    Test for range_group_dto
    """
    
    def test_valid_range_group_dto_creation(self):
        """
        Test create of range_group_dto
        """
        range_group_dto_obj = range_group_dto()
        
        # Проверяем, что объект создается без ошибок
        assert range_group_dto_obj is not None
        assert isinstance(range_group_dto_obj, range_group_dto)

    def test_valid_range_group_dto_set_params(self):
        """
        Test of range_group_dto's set params
        """
        range_group_dto_obj = range_group_dto()
        range_group_dto_obj.name="AAA"
        assert range_group_dto_obj.name=="AAA"
    