import pytest
from src.core.abstract_reference import argument_exception
from src.dto.filter_dto import filter_dto
from src.models.unit_model import unit_model
class TestFilterDto:
    """
    Test for filter_dto
    """
    def test_valid_create_filter_dto(self):
        """
        Test on valid creation of filter_dto
        """
        filter_dto_obj=filter_dto()
        filter_dto_obj.key="name"
        filter_dto_obj.operator="eq"
        filter_dto_obj.value="name1"
        assert filter_dto_obj.key=="name"
        assert filter_dto_obj.operator=="eq"
        assert filter_dto_obj.value=="name1"
    
    def test_error_create_filter_dto(self):
        """
        Test on error creation of filter_dto
        """
        filter_dto_obj=filter_dto()
        with pytest.raises(argument_exception):
            filter_dto_obj.key=1
        with pytest.raises(argument_exception):
            filter_dto_obj.operator=1
        with pytest.raises(argument_exception):
            filter_dto_obj.operator="wrong"

    def test_valid_validate_filter_dto(self):
        """
        Test on valid validate filter_dto
        """
        filter_dto_obj=filter_dto.create("name","eq","name1")
        unit_obj1=unit_model.create("name1",None,1.0)
        unit_obj2=unit_model.create("name2",unit_obj1,1.0)
        assert filter_dto_obj.validate(unit_obj1)==True
        assert filter_dto_obj.validate(unit_obj2)==False

    def test_valid_validate_inside_objects_attributes_filter_dto(self):
        """
        Test on validation inside attributes in values
        """
        filter_dto_obj=filter_dto.create("base_unit.name","eq","name1")
        unit_obj1=unit_model.create("name1",None,1.0)
        unit_obj2=unit_model.create("name2",unit_obj1,1.0)
        assert filter_dto_obj.validate(unit_obj1)==False
        assert filter_dto_obj.validate(unit_obj2)==True
    
    


