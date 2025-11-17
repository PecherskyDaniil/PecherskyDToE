import pytest
import json

from src.reposity import *
from src.start_service import *

@pytest.fixture
def start_service_instance():
    """Default start_service instance in fixture"""
    s_s=start_service()
    s_s.start()
    return s_s

class TestStart:
    """
    Tests for start_service
    """
    def test_valid_start_service_reposity_not_empty(self,start_service_instance):
        """
        Test valid start service
        """
        # проверка
        assert len(start_service_instance.reposity.data[reposity.unit_key()].keys()) != 0
        assert len(start_service_instance.reposity.data[reposity.range_group_key()].keys())!=0
        assert len(start_service_instance.reposity.data[reposity.range_key()].keys())!=0
        assert len(start_service_instance.reposity.data[reposity.receipt_key()].keys())!=0

    def test_valid_start_service_units(self,start_service_instance:start_service):
        """
        Test valid default created units
        """
        #Проверка всех значений
        assert all(key in start_service_instance.reposity.data[reposity.unit_key()].keys() for key in ["килограмм","грамм","литр","миллилитр","штука"])

    def test_valid_start_service_ranges(self,start_service_instance:start_service):
        """
        Test valid default created ranges
        """
        #Проверка всех значений
        assert all(key in start_service_instance.reposity.data[reposity.range_key()].keys() for key in ['яйцо', 'мука', 'молоко', 'соль', 'сахар', 'адыгейский сыр', 'моцарелла сыр', 'ванилин', 'масло растительное', 'масло сливочное', 'дрожжи', 'вода'])
    
    def test_valid_start_service_range_groups(self,start_service_instance:start_service):
        """
        Test valid default created range groups
        """
        #Проверка всех значений
        assert all(key in start_service_instance.reposity.data[reposity.range_group_key()].keys() for key in ["ингридиенты"])
    
    def test_valid_start_service_receipts(self,start_service_instance:start_service):
        """
        Test valid default created receipts
        """
        #Проверка всех значений
        assert all(key in start_service_instance.reposity.data[reposity.receipt_key()].keys() for key in ["Вафли Хрустящие","Хачапури по Адыгейски"])

    def test_valid_create_kilogram(self, start_service_instance):
        """Test kilogram unit creation"""
        #Создание
        kilogram = start_service_instance.create_killogramm()
        #Проверка
        assert kilogram.name == "килограмм"
        assert kilogram.coef == 1000.0
        assert kilogram.base_unit is not None

    def test_valid_create_gram(self, start_service_instance):
        """Test gram unit creation"""
        #Создание
        gram = start_service_instance.create_gramm()
        #Проверка
        assert gram.name == "грамм"
        assert gram.coef == 1.0
        assert gram.base_unit is None

    def test_valid_create_liter(self, start_service_instance):
        """Test liter unit creation"""
        #Создание
        liter = start_service_instance.create_litr()
        #Проверка
        assert liter.name == "литр"
        assert liter.coef == 1.0
        assert liter.base_unit is None

    def test_valid_create_milliliter(self, start_service_instance):
        """Test milliliter unit creation"""
        #Создание
        milliliter = start_service_instance.create_millilitr()
        #Проверка
        assert milliliter.name == "миллилитр"
        assert milliliter.coef == 0.001
        assert milliliter.base_unit is not None

    def test_valid_create_item(self, start_service_instance):
        """Test item unit creation"""
        #Создание
        item = start_service_instance.create_item()
        #Проверка
        assert item.name == "штука"
        assert item.coef == 1.0
        assert item.base_unit is None

    def test_valid_create_ingredients(self, start_service_instance):
        """Test ingredients group creation"""
        #Создание
        ingredients = start_service_instance.create_ingredients()
        #Проверка
        assert ingredients.name == "ингридиенты"

    def test_valid_create_milk(self, start_service_instance):
        """Test milk range creation"""
        #Создание
        milk = start_service_instance.create_milk()
        #Проверка
        assert milk.name == "молоко"
        assert milk.full_name == "Молоко пастеризованное натуральное"
        assert milk.unit is not None
        assert milk.group is not None

    def test_valid_create_salt(self, start_service_instance):
        """Test salt range creation"""
        #Создание
        salt = start_service_instance.create_salt()
        #Проверка
        assert salt.name == "соль"
        assert salt.full_name == "Соль пищевая кристализованная"
        assert salt.unit is not None
        assert salt.group is not None

    def test_valid_create_sugar(self, start_service_instance):
        """Test sugar range creation"""
        #Создание
        sugar = start_service_instance.create_sugar()
        #Проверка
        assert sugar.name == "сахар"
        assert sugar.full_name == "Сахар песок"
        assert sugar.unit is not None
        assert sugar.group is not None

    def test_valid_create_flour(self, start_service_instance):
        """Test flour range creation"""
        #Создание
        flour = start_service_instance.create_flour()
        #Проверка
        assert flour.name == "мука"
        assert flour.full_name == "Мука пшеничная 1 сорт"
        assert flour.unit is not None
        assert flour.group is not None

    def test_valid_create_egg(self, start_service_instance):
        """Test egg range creation"""
        #Создание
        egg = start_service_instance.create_egg()
        #Проверка
        assert egg.name == "яйцо"
        assert egg.full_name == "Яйцо куринное"
        assert egg.unit is not None
        assert egg.group is not None

    def test_valid_create_butter(self, start_service_instance):
        """Test butter range creation"""
        #Создание
        butter = start_service_instance.create_butter()
        #Проверка
        assert butter.name == "масло сливочное"
        assert butter.full_name == "Масло сливочное натуральное"
        assert butter.unit is not None
        assert butter.group is not None

    def test_valid_create_vanilin(self, start_service_instance):
        """Test vanilin range creation"""
        #Создание
        vanilin = start_service_instance.create_vanilin()
        #Проверка
        assert vanilin.name == "ванилин"
        assert vanilin.full_name == "Ванилин пищевой ароматизатор"
        assert vanilin.unit is not None
        assert vanilin.group is not None

    def test_valid_create_water(self, start_service_instance):
        """Test water range creation"""
        #Создание
        water = start_service_instance.create_water()
        #Проверка
        assert water.name == "вода"
        assert water.full_name == "Вода питьевая негазированная"
        assert water.unit is not None
        assert water.group is not None

    def test_valid_create_oil(self, start_service_instance):
        """Test oil range creation"""
        #Создание
        oil = start_service_instance.create_oil()
        #Проверка
        assert oil.name == "масло растительное"
        assert oil.full_name == "Масло растительное подсолнечное"
        assert oil.unit is not None
        assert oil.group is not None

    def test_valid_create_yeasts(self, start_service_instance):
        """Test yeasts range creation"""
        #Создание
        yeasts = start_service_instance.create_yeasts()
        #Проверка
        assert yeasts.name == "дрожжи"
        assert yeasts.full_name == "Дрожжи сухие"
        assert yeasts.unit is not None
        assert yeasts.group is not None

    def test_valid_create_mozarella_cheese(self, start_service_instance):
        """Test mozarella cheese range creation"""
        #Создание
        cheese = start_service_instance.create_mozarella_cheese()
        #Проверка
        assert cheese.name == "моцарелла сыр"
        assert cheese.full_name == "Сыр моцарелла"
        assert cheese.unit is not None
        assert cheese.group is not None

    def test_valid_create_adugey_cheese(self, start_service_instance):
        """Test adugey cheese range creation"""
        #Создание
        cheese = start_service_instance.create_adugey_cheese()
        #Проверка
        assert cheese.name == "адыгейский сыр"
        assert cheese.full_name == "Адыгейский сыр"
        assert cheese.unit is not None
        assert cheese.group is not None

    def test_valid_create_wafels_receipt(self, start_service_instance):
        """Test wafels receipt creation with correct ingridients and steps"""
        #Создание
        wafels = start_service_instance.create_wafels_receipt()
        #Проверка
        assert wafels.name == "Вафли Хрустящие"
        assert wafels.time == 20.0
        assert len(wafels.ingridients) == 5
        assert len(wafels.steps) == 8
        
        # Check ingridients
        proportion_names = [prop.range.name for prop in wafels.ingridients]
        expected_ingredients = ['мука', 'сахар', 'масло сливочное', 'яйцо', 'ванилин']
        for ingredient in expected_ingredients:
            assert ingredient in proportion_names

    def test_valid_create_hachapuri_receipt(self, start_service_instance):
        """Test hachapuri receipt creation with correct ingridients and steps"""
        #Создание
        hachapuri = start_service_instance.create_hachapuri()
        #Проверка
        assert hachapuri.name == "Хачапури по Адыгейски"
        assert hachapuri.time == 60.0
        assert len(hachapuri.ingridients) == 10
        assert len(hachapuri.steps) == 16
        
        # Check ingridients
        proportion_names = [prop.range.name for prop in hachapuri.ingridients]
        expected_ingredients = ['мука', 'сахар', 'масло сливочное', 'яйцо', 'молоко', 
                               'дрожжи', 'вода', 'масло растительное', 'адыгейский сыр', 'моцарелла сыр']
        for ingredient in expected_ingredients:
            assert ingredient in proportion_names

    def test_valid_start_method(self, start_service_instance):
        """Test that start method initializes all default data"""
        start_service_instance.start()
        
        # Verify that all data types are populated
        assert len(start_service_instance.reposity.data[reposity.unit_key()]) > 0
        assert len(start_service_instance.reposity.data[reposity.range_group_key()]) > 0
        assert len(start_service_instance.reposity.data[reposity.range_key()]) > 0
        assert len(start_service_instance.reposity.data[reposity.receipt_key()]) > 0

    def test_valid_duplicate_creation(self, start_service_instance):
        """Test that duplicate creation returns existing objects"""
        # First creation
        gram1 = start_service_instance.create_gramm()
        kilogram1 = start_service_instance.create_killogramm()
        
        # Second creation
        gram2 = start_service_instance.create_gramm()
        kilogram2 = start_service_instance.create_killogramm()
        
        # Verify same objects are returned
        assert gram1 is gram2
        assert kilogram1 is kilogram2
    
    def test_valid_hierarchy(self,start_service_instance):
        """Test that check if base unit is unit"""
        #Создание
        gram = start_service_instance.create_gramm()
        kilogram = start_service_instance.create_killogramm()

        mililiter = start_service_instance.create_millilitr()
        litr = start_service_instance.create_litr()
        #Проверка
        assert kilogram.base_unit == gram

        assert mililiter.base_unit == litr
    
    def test_reposity_data_persistence(self, start_service_instance):
        """Test that data persists in repository across method calls"""
        # Create some data
        start_service_instance.create_gramm()
        start_service_instance.create_ingredients()
        start_service_instance.create_egg()
        
        # Verify data is stored in repository
        assert 'грамм' in start_service_instance.reposity.data[reposity.unit_key()].keys()
        assert 'ингридиенты' in start_service_instance.reposity.data[reposity.range_group_key()].keys()
        assert 'яйцо' in start_service_instance.reposity.data[reposity.range_key()].keys()

    def test_valid_save_defaults_to_config(self, start_service_instance:start_service):
        """
        Test of start_service to save dafaults to config 
        """
        filepath="./tests/test_dir/test_default_config.json"
        if os.path.exists(filepath):
            os.remove(filepath)
        assert start_service_instance.save_data_to_config(filepath)==True
        with open(filepath,"r",encoding="UTF-8") as json_file:
            json_obj=json.load(json_file)
        assert len(json_obj["receipts"])==2
        assert len(json_obj["units"])==5
        assert len(json_obj["ranges"])==12
        assert len(json_obj["range_groups"])==1
    
    def test_valid_load_config_to_start_service(self):
        """
        Test of start_service to load from dafaults to config 
        """
        filepath="./tests/test_dir/test_default_config.json"
        s_s=start_service()
        s_s.start(False)
        assert s_s.load(filepath)==True
        assert len(s_s.reposity.data[reposity.receipt_key()])==2
        assert len(s_s.reposity.data[reposity.unit_key()])==5
        assert len(s_s.reposity.data[reposity.range_key()])==12
        assert len(s_s.reposity.data[reposity.range_group_key()])==1
        assert len (s_s.reposity.data[reposity.transaction_key()])==24
        assert len (s_s.reposity.data[reposity.storage_key()])==2
    
    def test_error_load_config_to_start_service(self):
        """
        Test of error start_service to load from defaults to config from wrong path
        """
        filepath="./wrong_path.json"
        s_s=start_service()
        s_s.start(False)
        assert s_s.load(filepath)==False
        with pytest.raises(operation_exception):
            s_s.load("")
    
    def test_valid_create_balance_sheet(self):
        s_s=start_service()
        s_s.start(True)
        start_datetime_filters=[
            filter_dto.create(
                "datetime",
                "lt",
                datetime.datetime.now()+datetime.timedelta(hours=2)
            )
        ]
        main_datteime_filters=[
            filter_dto.create(
                "datetime",
                "gt",
                datetime.datetime.now()+datetime.timedelta(hours=2)
            ),
            filter_dto.create(
                "datetime",
                "lt",
                datetime.datetime.now()+datetime.timedelta(days=2)
            )
        ]
        storage_filters=[
            filter_dto.create(
                "storage.name",
                "like",
                "Storage A"
            )
        ]
        result=s_s.create_balance_sheet(start_datetime_filters,
                                        main_datteime_filters,
                                        storage_filters,[])
        assert len(result)==len(list(s_s.reposity.data[reposity.range_key()].values()))
        line1=result[0]
        assert line1["end_balance"]==line1["start_balance"]-line1["out"]+line1["in"]


