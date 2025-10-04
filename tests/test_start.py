import pytest
import json

from src.reposity import *
from src.start_service import *

@pytest.fixture
def start_service_instance():
    s_s=start_service()
    s_s.start()
    return s_s

class TestStart:
    """
    Tests for start_service
    """
    def test_valid_start_service_reposity_not_empty(self,start_service_instance):
        """
        Test valid start service
        """
        # проверка
        assert len(start_service_instance.reposity.data[reposity.unit_key].keys()) != 0
        assert len(start_service_instance.reposity.data[reposity.range_group_key].keys())!=0
        assert len(start_service_instance.reposity.data[reposity.range_key].keys())!=0
        assert len(start_service_instance.reposity.data[reposity.receipt_key].keys())!=0

    def test_valid_start_service_units(self,start_service_instance:start_service):
        """
        Test valid default created units
        """
        assert all(key in start_service_instance.reposity.data[reposity.unit_key].keys() for key in ["килограмм","грамм","литр","миллилитр","штука"])

    def test_valid_start_service_ranges(self,start_service_instance:start_service):
        """
        Test valid default created ranges
        """
        assert all(key in start_service_instance.reposity.data[reposity.range_key].keys() for key in ['яйцо', 'мука', 'молоко', 'соль', 'сахар', 'адыгейский сыр', 'моцарелла сыр', 'ванилин', 'масло растительное', 'масло сливочное', 'дрожжи', 'вода'])
    
    def test_valid_start_service_range_groups(self,start_service_instance:start_service):
        """
        Test valid default created range groups
        """
        assert all(key in start_service_instance.reposity.data[reposity.range_group_key].keys() for key in ["ингридиенты"])
    
    def test_valid_start_service_receipts(self,start_service_instance:start_service):
        """
        Test valid default created receipts
        """
        assert all(key in start_service_instance.reposity.data[reposity.receipt_key].keys() for key in ["Вафли Хрустящие","Хачапури по Адыгейски"])
