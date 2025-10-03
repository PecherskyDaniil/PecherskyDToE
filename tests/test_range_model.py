import pytest
import json

from src.models.abstract_reference import *
from src.models.range_group_model import range_group_model
from src.models.range_model import range_model
from src.models.unit_model import unit_model

class TestRangeModel:
    """
    Tests of range_model
    """
    #проверка создания номенклатуры
    def test_valid_create_range_model(self):
        """
        Test on normal create of range_model
        """
        #Создание
        mls=unit_model("mls",None,1.0)
        litr=unit_model("litr",mls,1000.0)
        range_g=range_group_model("Food")
        new_range=range_model("Milk","Cow milk",litr,range_g)
        #Проверка
        assert new_range.name=="Milk"
        assert new_range.full_name=="Cow milk"
        assert new_range.unit.print_eq_coef()=="1 litr = 1000.0 mls"
    
    def test_error_wrong_name_length_range_model(self):
        """
        Test on error when name length not fits of range_model
        """
        #Создание
        mls=unit_model("mls",None,1.0)
        litr=unit_model("litr",mls,1000.0)
        range_g=range_group_model("Food")
        new_range=range_model("Milk","Cow milk",litr,range_g)
        #получение ошибки
        with pytest.raises(argument_exception):
            new_range.name="1"*51

    def test_error_wrong_full_name_length_range_model(self):
        """
        Test on error when full name length not fits in limits of range_model
        """
        #Создание
        mls=unit_model("mls",None,1.0)
        litr=unit_model("litr",mls,1000.0)
        range_g=range_group_model("Food")
        new_range=range_model("Milk","Cow milk",litr,range_g)
        #получение ошибки
        with pytest.raises(argument_exception):
            new_range.full_name="1"*256

    def test_error_wrong_unit_range_model(self):
        """
        Test on error when unit not fits in limits of range_model
        """
        #Создание
        range_g=range_group_model("Food")
        #получение ошибки
        with pytest.raises(argument_exception):
            new_range=range_model("Milk","Cow milk","wrong",range_g)

    def test_error_wrong_range_group_range_model(self):
        """
        Test on error when range group not fits in limits of range_model
        """
        #Создание
        mls=unit_model("mls",None,1.0)
        litr=unit_model("litr",mls,1000.0)
        #получение ошибки
        with pytest.raises(argument_exception):
            new_range=range_model("Milk","Cow milk",litr,"wrong")

    def test_valid_create_milk(self):
        """
        Test create milk range
        """
        milk_item = range_model.create_milk()
        assert milk_item.name == "молоко"
        assert milk_item.full_name == "Молоко пастеризованное натуральное"
        assert milk_item.unit.name == "литр"
        assert milk_item.group is not None
    
    def test_valid_create_salt(self):
        """
        Test create salt range
        """
        salt_item = range_model.create_salt()
        assert salt_item.name == "соль"
        assert salt_item.full_name == "Соль пищевая кристализованная"
        assert salt_item.unit.name == "килограмм"
        assert salt_item.group is not None
    
    def test_valid_create_sugar(self):
        """
        Test create sugar range
        """
        sugar_item = range_model.create_sugar()
        assert sugar_item.name == "сахар"
        assert sugar_item.full_name == "Сахар песок"
        assert sugar_item.unit.name == "килограмм"
        assert sugar_item.group is not None
    
    def test_valid_create_flour(self):
        """
        Test create flour range
        """
        flour_item = range_model.create_flour()
        assert flour_item.name == "мука"
        assert flour_item.full_name == "Мука пшеничная 1 сорт"
        assert flour_item.unit.name == "килограмм"
        assert flour_item.group is not None
    
    def test_valid_create_egg(self):
        """
        Test create egg range
        """
        egg_item = range_model.create_egg()
        assert egg_item.name == "яйцо"
        assert egg_item.full_name == "Яйцо куринное"
        assert egg_item.unit.name == "штука"
        assert egg_item.group is not None
    
    def test_valid_create_butter(self):
        """
        Test create butter range
        """
        butter_item = range_model.create_butter()
        assert butter_item.name == "масло сливочное"
        assert butter_item.full_name == "Масло сливочное натуральное"
        assert butter_item.unit.name == "грамм"
        assert butter_item.group is not None
    
    def test_valid_create_vanilin(self):
        """
        Test create vanilin range
        """
        vanilin_item = range_model.create_vanilin()
        assert vanilin_item.name == "ванилин"
        assert vanilin_item.full_name == "Ванилин пищевой ароматизатор"
        assert vanilin_item.unit.name == "грамм"
        assert vanilin_item.group is not None
    
    def test_valid_create_water(self):
        """
        Test create water range
        """
        water_item = range_model.create_water()
        assert water_item.name == "вода"
        assert water_item.full_name == "Вода питьевая негазированная"
        assert water_item.unit.name == "миллилитр"
        assert water_item.group is not None
    
    def test_valid_create_oil(self):
        """
        Test create oil range
        """
        oil_item = range_model.create_oil()
        assert oil_item.name == "масло растительное"
        assert oil_item.full_name == "Масло растительное подсолнечное"
        assert oil_item.unit.name == "миллилитр"
        assert oil_item.group is not None
    
    def test_valid_create_yeasts(self):
        """
        Test create yests range
        """
        yeasts_item = range_model.create_yeasts()
        assert yeasts_item.name == "дрожжи"
        assert yeasts_item.full_name == "Дрожжи сухие"
        assert yeasts_item.unit.name == "грамм"
        assert yeasts_item.group is not None
    
    def test_valid_create_mozarella_cheese(self):
        """
        Test create mozarella cheese range
        """
        cheese_item = range_model.create_mozarella_cheese()
        assert cheese_item.name == "моцарелла сыр"
        assert cheese_item.full_name == "Сыр моцарелла"
        assert cheese_item.unit.name == "грамм"
        assert cheese_item.group is not None
    
    def test_valid_create_adugey_cheese(self):
        """
        Test create adugey cheese range
        """
        cheese_item = range_model.create_adugey_cheese()
        assert cheese_item.name == "адыгейский сыр"
        assert cheese_item.full_name == "Адыгейский сыр"
        assert cheese_item.unit.name == "грамм"
        assert cheese_item.group is not None
    
    def test_valid_singleton_behavior(self):
        """
        Test singleton of default objects
        """
        # Проверяем, что декоратор singleton_result работает корректно
        milk_item1 = range_model.create_milk()
        milk_item2 = range_model.create_milk()
        
        salt_item1 = range_model.create_salt()
        salt_item2 = range_model.create_salt()
        
        # Должны возвращаться одни и те же объекты
        assert milk_item1 is milk_item2
        assert salt_item1 is salt_item2
    
    def test_valid_create_method_directly(self):
        """
        Test create instance range
        """
        # Тестируем базовый метод create напрямую
        test_unit = unit_model.create_gramm()
        test_group = range_group_model.create_ingredients()
        
        custom_item = range_model.create("тест", "Тестовый продукт", test_unit, test_group)
        
        assert custom_item.name == "тест"
        assert custom_item.full_name == "Тестовый продукт"
        assert custom_item.unit is test_unit
        assert custom_item.group is test_group