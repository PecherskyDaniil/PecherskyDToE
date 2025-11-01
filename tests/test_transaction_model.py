import pytest

from src.models.storage_model import storage_model
from src.models.range_model import range_model
from src.models.range_group_model import range_group_model
from src.models.unit_model import unit_model
from src.models.transaction_model import transaction_model
from src.dto.transaction_dto import transaction_dto
from datetime import datetime
class TestTransactionModel:

    
    
    def test_valid_transaction_creation(self):
        """
        Test valid create transaction
        """
        transaction=transaction_model()
        transaction.name="A"
        unit1=unit_model("gramm",None,1.0)
        unit2=unit_model("kilo",unit1,1000.0)
        group=range_group_model("food")
        transaction.range=range_model("butter","BUTTER",unit2,group)
        transaction.storage=storage_model("storage A")
        transaction.amount=10.0
        dt=datetime.now()
        transaction.datetime=dt
        transaction.unit=unit2
        
        assert transaction.name == "A"
        assert transaction.range.name == "butter"
        assert transaction.storage.name == "storage A"
        assert transaction.amount==10.0
        assert transaction.unit.name=="kilo"
        assert transaction.datetime==dt



    def test_valid_init_from_dto_transaction(self):
        """
        Test on valid init from dto object transaction_model
        """
        #Подготовка
        cache={
            "123":unit_model("gramm",None,1.0),
            "234":range_group_model("products"),
            "555":storage_model("storage A")
        }
        cache["345"]=range_model("sugar","sweet sugar",cache["123"],cache["234"])
        cache["456"]=range_model("salt","salty salt",cache["123"],cache["234"])
        #Создание
        transaction_dto_obj=transaction_dto()
        transaction_dto_obj.name="AAA"
        transaction_dto_obj.uuid="333"
        transaction_dto_obj.range_id="345"
        transaction_dto_obj.unit_id="123"
        transaction_dto_obj.storage_id="555"
        transaction_dto_obj.amount=10.0
        transaction_dto_obj.datetime="2025-12-31 12:00:00"
        #Присваивание
        transaction_obj=transaction_model.from_dto(transaction_dto_obj,cache)

        #Проверка
        assert transaction_obj.uuid=="333"
        assert transaction_obj.name=="AAA"
        assert transaction_obj.range==cache["345"]
        assert transaction_obj.unit==cache["123"]
        assert transaction_obj.storage==cache["555"]
        assert transaction_obj.amount==10.0
        assert transaction_obj.datetime==datetime(2025,12,31,12,0,0,0)
    
    def test_valid_convert_to_dto_transaction(self):
        """
        Test on valid convert to dto object transaction_model
        """
        #Подготовка
        cache={
            "123":unit_model("gramm",None,1.0),
            "234":range_group_model("products"),
            "555":storage_model("storage A")
        }
        cache["345"]=range_model("sugar","sweet sugar",cache["123"],cache["234"])
        cache["456"]=range_model("salt","salty salt",cache["123"],cache["234"])
        #Создание
        transaction_obj=transaction_model()     
        transaction_obj.name="AAA"
        transaction_obj.datetime=datetime(2025,12,31,12,0,0,0)
        transaction_obj.range=cache["345"]
        transaction_obj.storage=cache["555"]
        transaction_obj.amount=10.0
        transaction_obj.unit=cache["123"]
        #Присваивание
        transaction_dto_obj=transaction_obj.to_dto()
        #Проверка
        assert transaction_dto_obj.name=="AAA"
        assert transaction_dto_obj.unit_id==cache["123"].uuid
        assert transaction_dto_obj.range_id == cache["345"].uuid
        assert transaction_dto_obj.storage_id == cache["555"].uuid
        assert transaction_dto_obj.amount == 10.0
        assert transaction_dto_obj.datetime == "2025-12-31 12:00:00"

    