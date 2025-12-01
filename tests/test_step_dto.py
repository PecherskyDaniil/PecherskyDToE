import pytest

from src.dto.step_dto import *

class TestStepDTO:
    """
    Test for step_dto
    """
    
    def test_valid_step_dto_creation(self):
        """
        Test create of step_dto
        """
        step_dto_obj = step_dto()
        
        assert step_dto_obj.step_description == ""

    def test_valid_step_dto_set_properties(self):
        """
        Test of step_dto's set properties
        """
        step_dto_obj = step_dto()
        step_dto_obj.step_description = "Mix all ingredients thoroughly"
        
        assert step_dto_obj.step_description == "Mix all ingredients thoroughly"