import pytest
import json

from src.logics.response_csv import *

from src.reposity import *
from src.start_service import start_service
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

class TestResponceCSV:
    """
    Tests of responce_csv
    """
    def test_valid_create_responce_csv(self,simple_valid_data):
        csv_formatter=response_csv()
        csv_result=csv_formatter.create(simple_valid_data)
        assert csv_result.split("\n")[0]=="full_name;group_id;id;name;unit_id"
        assert len(csv_result.split("\n")[1].split(";"))==len(csv_result.split("\n")[0].split(";"))
        assert len(csv_result.split("\n"))==4
        
    def test_valid_create_file_responce_csv(self,valid_data_of_factory):
        """
        Test on valid create of reponce_csv
        """
        #Создание
        data=list(valid_data_of_factory[reposity.receipt_key()].values())
        csv=response_csv().create(data)
        #Проверка
        assert len(csv.split("\n")[0].split(";"))==5
        with open("./examples/receipts.csv","w",encoding="UTF-8") as file:
            file.write(csv)
    