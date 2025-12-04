import pytest

from src.logics.response_markdown import *

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

class TestResponceMD:
    """
    Tests of responce_markdown
    """
    def test_valid_create_responce_markdown(self,simple_valid_data):
        markdown_formatter=response_markdown()
        markdown_result=markdown_formatter.create(simple_valid_data)
        #assert markdown_result.split("\n")[0]=="|full_name|group_id|id|name|unit_id|"
        assert len(markdown_result.split("\n")[2].split("|"))==len(markdown_result.split("\n")[0].split("|"))
        assert len(markdown_result.split("\n"))==5

    def test_valid_create_file_responce_markdown(self,valid_data_of_factory):
        """
        Test on valid create of reponce_markdown
        """
        #Создание
        data=list(valid_data_of_factory[reposity_keys.range_key()].values())
        markdown=response_markdown().create(data)
        #Проверка
        assert len(markdown.split("\n")[0].split("|"))==7
        with open("./examples/ranges.md","w",encoding="UTF-8") as file:
            file.write(markdown)
    