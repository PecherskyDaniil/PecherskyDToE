import pytest

from src.dto.receipt_dto import *

class TestReceiptDTO:
    """
    Test for receipt_dto
    """
    
    def test_valid_receipt_dto_creation(self):
        """
        Test create of receipt_dto
        """
        receipt_dto_obj = receipt_dto()
        
        assert receipt_dto_obj.steps == []
        assert receipt_dto_obj.ingridients == []
        assert receipt_dto_obj.time == 0.0

    def test_valid_receipt_dto_set_properties(self):
        """
        Test of receipt_dto's set properties
        """
        receipt_dto_obj = receipt_dto()
        receipt_dto_obj.steps = ["Step 1", "Step 2", "Step 3"]
        receipt_dto_obj.ingridients = [{"name": "flour", "amount": 200}, {"name": "sugar", "amount": 100}]
        receipt_dto_obj.time = 45.5
        
        assert receipt_dto_obj.steps == ["Step 1", "Step 2", "Step 3"]
        assert receipt_dto_obj.ingridients == [{"name": "flour", "amount": 200}, {"name": "sugar", "amount": 100}]
        assert receipt_dto_obj.time == 45.5