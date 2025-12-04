import pytest
import json 
from src.logics.response_json import *

from src.reposity import *
from src.start_service import start_service
from src.models.range_model import range_model
from src.models.unit_model import unit_model
from src.models.range_group_model import range_group_model
from src.core.reposity_keys import reposity_keys
@pytest.fixture
def valid_data_of_factory():
    """
    Fixture for example data
    """
    s_s=start_service()
    s_s.start()
    return s_s.reposity.data
@pytest.fixture
def simple_valid_data():
    return [
            range_model("name1","The Name1",unit_model("gramm",None,1.0),range_group_model("products")),
            range_model("name2","The Name2",unit_model("litr",None,5.0),range_group_model("drinks")),
            ]

class TestResponceJSON:
    """
    Tests of responce_json
    """
    def test_valid_create_responce_json(self,simple_valid_data):
        json_formatter=response_json()
        json_result=json_formatter.create(simple_valid_data)
        json_obj=json.loads(json_result)
        assert len(json_obj["data"][0].keys())==5
        assert json_obj["data"][0].keys()==json_obj["data"][1].keys()

    def test_valid_create_file_responce_json(self,valid_data_of_factory):
        """
        Test on valid create of reponce_json
        """
        #Создание
        data=list(valid_data_of_factory[reposity_keys.unit_key()].values())
        json=response_json().create(data)
        #Проверка
        assert json!=""
        with open("./examples/units.json","w",encoding="UTF-8") as file:
            file.write(json)
    