import pytest

from src.dto.storage_dto import *

class TestStorageDTO:
    """
    Test for storage_dto
    """
    
    def test_valid_storage_dto_creation(self):
        """
        Test create of storage_dto
        """
        storage_dto_obj = storage_dto()
        
        # Проверяем, что объект создается без ошибок
        assert storage_dto_obj is not None
        assert isinstance(storage_dto_obj, storage_dto)

    def test_valid_storage_dto_set_params(self):
        """
        Test of storage_dto's set params
        """
        storage_dto_obj = storage_dto()
        storage_dto_obj.name="AAA"
        assert storage_dto_obj.name=="AAA"
    