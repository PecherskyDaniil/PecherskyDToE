import pytest

from src.dto.transaction_dto import *

class TestTransactionDTO:
    """
    Test for transaction_dto
    """

    def test_valid_transaction_dto_set_properties(self):
        """
        Test of receipt_dto's set properties
        """
        transaction_dto_obj = transaction_dto()
        transaction_dto_obj.uuid = "123"
        transaction_dto_obj.datetime = "123"
        transaction_dto_obj.range_id = "321"
        transaction_dto_obj.unit_id = "213"
        transaction_dto_obj.storage_id = "312"
        transaction_dto_obj.amount = 10.0
        
        assert transaction_dto_obj.uuid == "123"
        assert transaction_dto_obj.datetime == "123"
        assert transaction_dto_obj.range_id == "321"
        assert transaction_dto_obj.unit_id == "213"
        assert transaction_dto_obj.storage_id == "312"
        assert transaction_dto_obj.amount == 10.0