
import pytest

from src.models.proportion import *
from src.models.unit_model import *
from src.models.range_model import *
class TestProportion:
    """
    Test for proportion
    """
    
    def test_valid_proportion_creation(self):
        """
        Test create of proportion
        """
        test_range = range_model.create("A","A",unit_model.create("name",None,1.0),range_group_model.create("name"))
        proportion_obj = proportion(test_range, 2.5)
        
        assert proportion_obj.range == test_range
        assert proportion_obj.proportion_value == 2.5
    
    def test_valid_range_setter(self):
        """
        Test set range of proportion
        """
        test_range1=range_model.create("A","A",unit_model.create("name",None,1.0),range_group_model.create("name"))
        proportion_obj = proportion(test_range1)
        test_range2 = range_model.create("B","B",unit_model.create("name",None,1.0),range_group_model.create("name"))
        
        proportion_obj.range = test_range2
        assert proportion_obj.range == test_range2
    
    def test_error_range_setter(self):
        """
        Test error set range of proportion
        """
        test_range=range_model.create("A","A",unit_model.create("name",None,1.0),range_group_model.create("name"))
        proportion_obj = proportion(test_range)
        
        with pytest.raises(argument_exception, match="range should be range_model type"):
            proportion_obj.range = "invalid_range"
    
    def test_valid_proportion_value_setter(self):
        """
        Test set proportion_value of proportion
        """
        test_range=range_model.create("A","A",unit_model.create("name",None,1.0),range_group_model.create("name"))
        proportion_obj = proportion(test_range,2.0)
        proportion_obj.proportion_value = 3.14
        assert proportion_obj.proportion_value == 3.14
    
    def test_error_proportion_value_setter(self):
        """
        Test error set proportion_value of proportion
        """
        test_range=range_model.create("A","A",unit_model.create("name",None,1.0),range_group_model.create("name"))
        proportion_obj = proportion(test_range)
        
        with pytest.raises(argument_exception, match="proportion_value should be float type"):
            proportion_obj.proportion_value = "not_a_float"
