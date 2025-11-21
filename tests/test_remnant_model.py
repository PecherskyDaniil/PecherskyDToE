import pytest
import datetime
from unittest.mock import Mock
from src.models.range_model import range_model
from src.models.unit_model import unit_model
from src.models.storage_model import storage_model
from src.dto.remnant_dto import remnant_dto
from src.models.remnant_model import remnant_model
from src.models.range_group_model import range_group_model

class TestRemnantModel:
    """Тесты для класса remnant_model"""

    @pytest.fixture
    def sample_unit(self):
        """Фикстура для создания тестового unit_model"""
        unit_obj = unit_model.create("b",None,1.0)
        unit_obj.uuid = "unit-uuid-123"
        return unit_obj
    @pytest.fixture
    def sample_group(self):
        """Фикстура для создания тестового range_model"""
        group_obj = range_group_model.create("Agroup")
        return group_obj
    
    @pytest.fixture
    def sample_range(self,sample_unit,sample_group):
        """Фикстура для создания тестового range_model"""
        range_obj = range_model.create("a",'AA',sample_unit,sample_group)
        range_obj.uuid = "range-uuid-123"
        return range_obj


    @pytest.fixture
    def sample_storage(self):
        """Фикстура для создания тестового storage_model"""
        storage_obj = storage_model()
        storage_obj.name="Astorage"
        storage_obj.uuid = "storage-uuid-123"
        return storage_obj

    @pytest.fixture
    def sample_datetime(self):
        """Фикстура для создания тестового datetime"""
        return datetime.datetime(2023, 10, 15, 14, 30, 0)

    @pytest.fixture
    def sample_remnant_model(self, sample_range, sample_unit, sample_storage, sample_datetime):
        """Фикстура для создания тестового remnant_model"""
        obj = remnant_model("test_remnant")
        obj.uuid = "remnant-uuid-123"
        obj.range = sample_range
        obj.unit = sample_unit
        obj.storage = sample_storage
        obj.datetime = sample_datetime
        obj.remnant_value = 150.5
        return obj

    def test_initialization(self):
        """Тест инициализации объекта"""
        # Act
        obj = remnant_model("test_name")
        
        # Assert
        assert obj.name == "test_name"
        assert hasattr(obj, 'uuid')

    def test_properties_setters_and_getters(self, sample_range, sample_unit, sample_storage, sample_datetime):
        """Тест свойств, сеттеров и геттеров"""
        # Arrange
        obj = remnant_model()
        
        # Act & Assert для range
        obj.range = sample_range
        assert obj.range == sample_range
        
        # Act & Assert для unit
        obj.unit = sample_unit
        assert obj.unit == sample_unit
        
        # Act & Assert для storage
        obj.storage = sample_storage
        assert obj.storage == sample_storage
        
        # Act & Assert для datetime
        obj.datetime = sample_datetime
        assert obj.datetime == sample_datetime
        
        # Act & Assert для remnant_value
        obj.remnant_value = 200.75
        assert obj.remnant_value == 200.75

    def test_property_validation(self):
        """Тест валидации свойств"""
        # Arrange
        obj = remnant_model()
        
        # Act & Assert - проверка что неправильные типы вызывают ошибку
        with pytest.raises(Exception):  # Замените на конкретный тип исключения model_validator
            obj.range = "invalid_type"
            
        with pytest.raises(Exception):
            obj.unit = "invalid_type"
            
        with pytest.raises(Exception):
            obj.storage = "invalid_type"
            
        with pytest.raises(Exception):
            obj.datetime = "invalid_datetime"
            
        with pytest.raises(Exception):
            obj.remnant_value = "invalid_float"

    def test_create_factory_method(self, sample_range, sample_unit, sample_storage, sample_datetime):
        """Тест фабричного метода create"""
        # Act
        obj = remnant_model.create(
            range_obj=sample_range,
            storage_obj=sample_storage,
            unit_obj=sample_unit,
            value_obj=300.25,
            datetime=sample_datetime
        )
        
        # Assert
        assert obj.range == sample_range
        assert obj.unit == sample_unit
        assert obj.storage == sample_storage
        assert obj.remnant_value == 300.25
        assert obj.datetime == sample_datetime
        assert obj.name == "remnant"

    def test_from_dto(self, sample_range, sample_unit, sample_storage):
        """Тест конвертации из DTO"""
        # Arrange
        remnant_dto_obj = remnant_dto()
        remnant_dto_obj.unit_id = "unit-uuid-123"
        remnant_dto_obj.range_id = "range-uuid-123"
        remnant_dto_obj.storage_id = "storage-uuid-123"
        remnant_dto_obj.remnant_value = 400.75
        remnant_dto_obj.datetime = datetime.datetime(2023, 10, 16, 10, 0, 0)
        
        cache = {
            "unit-uuid-123": sample_unit,
            "range-uuid-123": sample_range,
            "storage-uuid-123": sample_storage
        }
        
        # Act
        result = remnant_model.from_dto(remnant_dto_obj, cache)
        
        # Assert
        assert result.range == sample_range
        assert result.unit == sample_unit
        assert result.storage == sample_storage
        assert result.remnant_value == 400.75
        assert result.datetime == remnant_dto_obj.datetime

    def test_from_dto_with_missing_cache_entries(self):
        """Тест конвертации из DTO с отсутствующими записями в кэше"""
        # Arrange
        remnant_dto_obj = remnant_dto()
        remnant_dto_obj.unit_id = "missing-unit-id"
        remnant_dto_obj.range_id = "missing-range-id"
        remnant_dto_obj.storage_id = "missing-storage-id"
        remnant_dto_obj.remnant_value = 100.0
        remnant_dto_obj.datetime = datetime.datetime(2023, 10, 16, 10, 0, 0)
        
        cache = {}  # Пустой кэш
        
        # Act
        result = remnant_model.from_dto(remnant_dto_obj, cache)
        
        # Assert
        assert result.range is None
        assert result.unit is None
        assert result.storage is None
        assert result.remnant_value == 100.0
        assert result.datetime == remnant_dto_obj.datetime

    def test_to_dto(self, sample_remnant_model):
        """Тест конвертации в DTO"""
        # Act
        dto_result = sample_remnant_model.to_dto()
        
        # Assert
        assert isinstance(dto_result, remnant_dto)
        assert dto_result.name == "test_remnant"
        assert dto_result.uuid == "remnant-uuid-123"
        assert dto_result.range_id == "range-uuid-123"
        assert dto_result.unit_id == "unit-uuid-123"
        assert dto_result.storage_id == "storage-uuid-123"
        assert dto_result.remnant_value == 150.5
        assert dto_result.datetime == sample_remnant_model.datetime

    def test_inheritance(self):
        """Тест наследования от abstract_reference"""
        # Arrange & Act
        obj = remnant_model()
        
        # Assert
        assert hasattr(obj, 'name')
        assert hasattr(obj, 'uuid')
        # Добавьте другие проверки наследования в зависимости от того, что есть в abstract_reference

    def test_edge_cases(self, sample_range, sample_unit, sample_storage):
        """Тест граничных случаев"""
        # Тест с нулевым значением
        obj = remnant_model.create(sample_range, sample_storage, sample_unit, 0.0, datetime.datetime(2023, 1, 1))
        assert obj.remnant_value == 0.0
        
        # Тест с отрицательным значением (если допустимо)
        obj.remnant_value = -50.0
        assert obj.remnant_value == -50.0
        
        # Тест с очень большим значением
        obj.remnant_value = 1e10
        assert obj.remnant_value == 1e10

    def test_datetime_variations(self, sample_range, sample_unit, sample_storage):
        """Тест с различными форматами datetime"""
        # Тест с разными датами
        test_cases = [
            datetime.datetime(2023, 1, 1),
            datetime.datetime(2023, 12, 31, 23, 59, 59),
            datetime.datetime(2000, 1, 1),
            datetime.datetime(2030, 6, 15, 12, 30, 45)
        ]
        
        for test_datetime in test_cases:
            obj = remnant_model.create(sample_range, sample_storage, sample_unit, 100.0, test_datetime)
            assert obj.datetime == test_datetime