import pytest
import datetime
from src.dto.remnant_dto import remnant_dto


class TestRemnantDto:
    """Тесты для класса remnant_dto"""


    def test_name_property(self):
        """Тест свойства name"""
        # Arrange
        dto = remnant_dto()
        
        # Act
        dto.name = "Test Remnant"
        
        # Assert
        assert dto.name == "Test Remnant"

    def test_uuid_property(self):
        """Тест свойства uuid"""
        # Arrange
        dto = remnant_dto()
        
        # Act
        dto.uuid = "test-uuid-123"
        
        # Assert
        assert dto.uuid == "test-uuid-123"

    def test_range_id_property(self):
        """Тест свойства range_id"""
        # Arrange
        dto = remnant_dto()
        
        # Act
        dto.range_id = "range-uuid-456"
        
        # Assert
        assert dto.range_id == "range-uuid-456"

    def test_unit_id_property(self):
        """Тест свойства unit_id"""
        # Arrange
        dto = remnant_dto()
        
        # Act
        dto.unit_id = "unit-uuid-789"
        
        # Assert
        assert dto.unit_id == "unit-uuid-789"

    def test_storage_id_property(self):
        """Тест свойства storage_id"""
        # Arrange
        dto = remnant_dto()
        
        # Act
        dto.storage_id = "storage-uuid-101"
        
        # Assert
        assert dto.storage_id == "storage-uuid-101"

    def test_datetime_property(self):
        """Тест свойства datetime"""
        # Arrange
        dto = remnant_dto()
        test_datetime = datetime.datetime(2023, 10, 15, 14, 30, 0)
        
        # Act
        dto.datetime = test_datetime
        
        # Assert
        assert dto.datetime == test_datetime

    def test_remnant_value_property(self):
        """Тест свойства remnant_value"""
        # Arrange
        dto = remnant_dto()
        
        # Act
        dto.remnant_value = 150.75
        
        # Assert
        assert dto.remnant_value == 150.75

    def test_all_properties_together(self):
        """Тест установки всех свойств вместе"""
        # Arrange
        dto = remnant_dto()
        test_datetime = datetime.datetime(2023, 10, 15, 14, 30, 0)
        
        # Act
        dto.name = "Complete Test Remnant"
        dto.uuid = "complete-uuid-123"
        dto.range_id = "complete-range-456"
        dto.unit_id = "complete-unit-789"
        dto.storage_id = "complete-storage-101"
        dto.datetime = test_datetime
        dto.remnant_value = 250.25
        
        # Assert
        assert dto.name == "Complete Test Remnant"
        assert dto.uuid == "complete-uuid-123"
        assert dto.range_id == "complete-range-456"
        assert dto.unit_id == "complete-unit-789"
        assert dto.storage_id == "complete-storage-101"
        assert dto.datetime == test_datetime
        assert dto.remnant_value == 250.25

    def test_property_sequence_operations(self):
        """Тест последовательных операций с свойствами"""
        # Arrange
        dto = remnant_dto()
        
        # Act & Assert - последовательное изменение значений
        dto.name = "First Name"
        assert dto.name == "First Name"
        
        dto.name = "Second Name"
        assert dto.name == "Second Name"
        
        dto.remnant_value = 100.0
        assert dto.remnant_value == 100.0
        
        dto.remnant_value = 200.0
        assert dto.remnant_value == 200.0

    def test_edge_cases_remnant_value(self):
        """Тест граничных случаев для remnant_value"""
        # Arrange
        dto = remnant_dto()
        
        # Test cases
        test_cases = [
            0.0,           # нулевое значение
            -50.5,         # отрицательное значение
            1e10,          # очень большое значение
            0.0001,        # очень маленькое значение
            -0.0001,       # очень маленькое отрицательное значение
            999999.999,    # значение с плавающей точкой
        ]
        
        for value in test_cases:
            # Act
            dto.remnant_value = value
            
            # Assert
            assert dto.remnant_value == value

    def test_datetime_variations(self):
        """Тест различных форматов datetime"""
        # Arrange
        dto = remnant_dto()
        
        # Test cases
        test_datetimes = [
            datetime.datetime(2023, 1, 1),                    # начало года
            datetime.datetime(2023, 12, 31, 23, 59, 59),      # конец года
            datetime.datetime(2000, 1, 1),                    # другое тысячелетие
            datetime.datetime(2030, 6, 15, 12, 30, 45, 123456), # с микросекундами
            datetime.datetime(2023, 2, 28),                   # февраль не високосный
            datetime.datetime(2020, 2, 29),                   # февраль високосный
        ]
        
        for test_dt in test_datetimes:
            # Act
            dto.datetime = test_dt
            
            # Assert
            assert dto.datetime == test_dt

    def test_string_properties_edge_cases(self):
        """Тест граничных случаев для строковых свойств"""
        # Arrange
        dto = remnant_dto()
        
        # Test cases
        test_cases = [
            "",                    # пустая строка
            "a",                   # один символ
            " " * 100,             # много пробелов
            "test-with-dashes",    # строки с дефисами
            "test_with_underscores", # строки с подчеркиваниями
            "123456",              # числовая строка
            "test@email.com",      # строка с специальными символами
            "🚀",                  # emoji
        ]
        
        for test_str in test_cases:
            # Act & Assert для name
            dto.name = test_str
            assert dto.name == test_str
            
            # Act & Assert для uuid
            dto.uuid = test_str
            assert dto.uuid == test_str
            
            # Act & Assert для range_id
            dto.range_id = test_str
            assert dto.range_id == test_str
            
            # Act & Assert для unit_id
            dto.unit_id = test_str
            assert dto.unit_id == test_str
            
            # Act & Assert для storage_id
            dto.storage_id = test_str
            assert dto.storage_id == test_str

    def test_property_independence(self):
        """Тест независимости свойств друг от друга"""
        # Arrange
        dto = remnant_dto()
        
        # Act - установка одного свойства не должна влиять на другие
        dto.name = "Test Name"
        dto.uuid = "test-uuid"
        dto.range_id = "range-1"
        dto.unit_id = "unit-1"
        dto.storage_id = "storage-1"
        dto.datetime = datetime.datetime(2023, 1, 1)
        dto.remnant_value = 100.0
        
        # Assert - проверка что все свойства сохранили свои значения
        assert dto.name == "Test Name"
        assert dto.uuid == "test-uuid"
        assert dto.range_id == "range-1"
        assert dto.unit_id == "unit-1"
        assert dto.storage_id == "storage-1"
        assert dto.datetime == datetime.datetime(2023, 1, 1)
        assert dto.remnant_value == 100.0
        
        # Act - изменение одного свойства
        dto.remnant_value = 200.0
        
        # Assert - остальные свойства не изменились
        assert dto.name == "Test Name"
        assert dto.uuid == "test-uuid"
        assert dto.range_id == "range-1"
        assert dto.unit_id == "unit-1"
        assert dto.storage_id == "storage-1"
        assert dto.datetime == datetime.datetime(2023, 1, 1)

    def test_multiple_instances_independence(self):
        """Тест независимости нескольких экземпляров"""
        # Arrange
        dto1 = remnant_dto()
        dto2 = remnant_dto()
        
        # Act
        dto1.name = "First DTO"
        dto1.uuid = "first-uuid"
        dto1.remnant_value = 100.0
        
        dto2.name = "Second DTO"
        dto2.uuid = "second-uuid"
        dto2.remnant_value = 200.0
        
        # Assert
        assert dto1.name == "First DTO"
        assert dto1.uuid == "first-uuid"
        assert dto1.remnant_value == 100.0
        
        assert dto2.name == "Second DTO"
        assert dto2.uuid == "second-uuid"
        assert dto2.remnant_value == 200.0

    def test_none_values(self):
        """Тест установки None значений (где это допустимо)"""
        # Arrange
        dto = remnant_dto()
        
        # Act & Assert - для свойств, которые могут быть None
        dto.datetime = None
        assert dto.datetime is None
        
        dto.remnant_value = None
        assert dto.remnant_value is None

    def test_property_types(self):
        """Тест типов возвращаемых значений свойств"""
        # Arrange
        dto = remnant_dto()
        dto.name = "Test"
        dto.uuid = "uuid-123"
        dto.range_id = "range-123"
        dto.unit_id = "unit-123"
        dto.storage_id = "storage-123"
        dto.datetime = datetime.datetime(2023, 1, 1)
        dto.remnant_value = 100.5
        
        # Assert
        assert isinstance(dto.name, str)
        assert isinstance(dto.uuid, str)
        assert isinstance(dto.range_id, str)
        assert isinstance(dto.unit_id, str)
        assert isinstance(dto.storage_id, str)
        assert isinstance(dto.datetime, datetime.datetime)
        assert isinstance(dto.remnant_value, float)