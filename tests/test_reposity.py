import pytest

from src.reposity import *
from src.start_service import *
class TestReposity:
    
    def test_valid_reposity_to_json(self):
        s_s=start_service()
        s_s.start()
        data=s_s.reposity.to_json()
        assert "receipts" in data.keys()
        assert "units" in data.keys()
        assert "ranges" in data.keys()
        assert "range_groups" in data.keys()
        assert "transactions" in data.keys()
        assert "storages" in data.keys()

    