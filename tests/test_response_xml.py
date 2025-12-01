import pytest
import xml.etree.ElementTree as ET

from src.logics.response_xml import *

from src.reposity import *
from src.start_service import start_service
from src.models.range_model import range_model
from src.models.unit_model import unit_model
from src.models.range_group_model import range_group_model
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

class TestResponceXML:
    """
    Tests of responce_xml
    """

    def test_valid_create_responce_xml(self,simple_valid_data):
        xml_formatter=response_xml()
        xml_result=xml_formatter.create(simple_valid_data)
        xml_obj = ET.fromstring(xml_result)
        #assert xml_result==None
        assert len(xml_obj.findall("obj"))==2
        assert len(xml_obj.findall("obj")[0].findall("uuid"))==1
        assert len(xml_obj.findall("obj")[1].findall("*"))==5

    def test_valid_create_file_responce_xml(self,valid_data_of_factory):
        """
        Test on valid create of reponce_xml
        """
        #Создание
        data=list(valid_data_of_factory[reposity_keys.receipt_key()].values())
        xml=response_xml().create(data)
        #Проверка
        assert xml!=""
        with open("./examples/receipts.xml","w",encoding="UTF-8") as file:
            file.write(xml)
    