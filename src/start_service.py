from .reposity import *
from .models.abstract_reference import *
from .models.unit_model import unit_model
from .models.range_group_model import range_group_model
from .models.range_model import range_model
from .models.receipt_model import receipt_model
from .models.proportion import proportion
from .models.step import step
class start_service:
    """
    Class that creates all default data and start work of all service
    reposity:reposity - where the data contains
    """
    __reposity: reposity = reposity()
    __instance = None

    def __init__(self):
        """
        Constructor of class
        """
        self.__reposity.data[reposity.unit_key] = {}
        self.__reposity.data[reposity.range_key] = {}
        self.__reposity.data[reposity.range_group_key] = {}
        self.__reposity.data[reposity.receipt_key] = {}

    """
    Реализация Singleton
    """
    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super(start_service, cls).__new__(cls)
        return cls.__instance
    
    @property
    def reposity(self):
        """
        Function that returns property reposity
        """
        return self.__reposity
    

    def __create_default_value(self,key:str,obj:abstract_reference):
        """
        Function that creates deafult instances and save it in class
        """
        if obj.name not in self.reposity.data[key].keys():
            self.reposity.data[key][obj.name]=obj
        return self.reposity.data[key][obj.name]

    def default_create_unit(self):
        """
        Function that creates all default units
        """
        self.create_killogramm()
        self.create_gramm()
        self.create_litr()
        self.create_millilitr()
        self.create_item()
    
    def default_create_range_group(self):
        """
        Function that creates all default range_groups
        """
        self.create_ingredients()
        
    def default_create_range(self):
        """
        Function that creates all default ranges
        """
        self.create_egg()
        self.create_flour()
        self.create_milk()
        self.create_salt()
        self.create_sugar()
        self.create_adugey_cheese()
        self.create_mozarella_cheese()
        self.create_vanilin()
        self.create_oil()
        self.create_butter()
        self.create_yeasts()
        self.create_water()

    def default_create_receipt(self):
        """
        Function that creates all default receipts
        """
        self.create_wafels_receipt()
        self.create_hachapuri()

    #@staticmethod
    def create_killogramm(self):
        """
        Creates default unit killogramm
        """
        inner_gramm=self.create_gramm()
        item=self.__create_default_value(reposity.unit_key,unit_model.create("килограмм",inner_gramm,1000.0))
        return item
    
    #@staticmethod
    def create_gramm(self):
        """
        Creates default unit gramm
        """
        item=self.__create_default_value(reposity.unit_key,unit_model.create("грамм",None,1.0))
        return item
    
    #@staticmethod
    def create_litr(self):
        """
        Creates default unit litr
        """
        item=self.__create_default_value(reposity.unit_key,unit_model.create("литр",None,1.0))
        return item

    #@staticmethod
    def create_millilitr(self):
        """
        Creates default unit millilitr
        """
        item=self.__create_default_value(reposity.unit_key,unit_model.create("миллилитр",self.create_litr(),0.001))
        return item
    
    #@staticmethod
    def create_item(self):
        """
        Creates default unit item
        """
        item=self.__create_default_value(reposity.unit_key,unit_model.create("штука",None,1.0))
        return item


    #@staticmethod
    def create_ingredients(self):
        """
        Function that creates deafult value ingridients
        """
        return self.__create_default_value(reposity.range_group_key,range_group_model.create("ингридиенты"))

    #@staticmethod
    def create_milk(self):
        """
        Creates default range milk
        """
        return self.__create_default_value(reposity.range_key,range_model.create("молоко","Молоко пастеризованное натуральное",self.create_litr(),self.create_ingredients()))

    #@staticmethod
    def create_salt(self):
        """
        Creates default range salt
        """
        return self.__create_default_value(reposity.range_key,range_model.create("соль","Соль пищевая кристализованная",self.create_killogramm(),self.create_ingredients()))


    #@staticmethod
    def create_sugar(self):
        """
        Creates default range sugar
        """
        return self.__create_default_value(reposity.range_key,range_model.create("сахар","Сахар песок",self.create_killogramm(),self.create_ingredients()))


    #@staticmethod
    def create_flour(self):
        """
        Creates default range flour
        """
        return self.__create_default_value(reposity.range_key,range_model.create("мука","Мука пшеничная 1 сорт",self.create_killogramm(),self.create_ingredients()))
    
    #@staticmethod
    def create_egg(self):
        """
        Creates default range egg
        """
        return self.__create_default_value(reposity.range_key,range_model.create("яйцо","Яйцо куринное",self.create_item(),self.create_ingredients()))

    
    #@staticmethod
    def create_butter(self):
        """
        Creates default range butter
        """
        return self.__create_default_value(reposity.range_key,range_model.create("масло сливочное","Масло сливочное натуральное",self.create_gramm(),self.create_ingredients()))

    
    #@staticmethod
    def create_vanilin(self):
        """
        Creates default range vanilin
        """
        return self.__create_default_value(reposity.range_key,range_model.create("ванилин","Ванилин пищевой ароматизатор",self.create_gramm(),self.create_ingredients()))



    #@staticmethod
    def create_water(self):
        """
        Creates default range water
        """
        return self.__create_default_value(reposity.range_key,range_model.create("вода","Вода питьевая негазированная",self.create_millilitr(),self.create_ingredients()))

    #@staticmethod
    def create_oil(self):
        """
        Creates default range oil
        """
        return self.__create_default_value(reposity.range_key,range_model.create("масло растительное","Масло растительное подсолнечное",self.create_millilitr(),self.create_ingredients()))


    #@staticmethod
    def create_yeasts(self):
        """
        Creates default range yests
        """
        return self.__create_default_value(reposity.range_key,range_model.create("дрожжи","Дрожжи сухие",self.create_gramm(),self.create_ingredients()))


    #@staticmethod
    def create_mozarella_cheese(self):
        """
        Creates default range mozarella cheese
        """
        return self.__create_default_value(reposity.range_key,range_model.create("моцарелла сыр","Сыр моцарелла",self.create_gramm(),self.create_ingredients()))

    
    #@staticmethod
    def create_adugey_cheese(self):
        """
        Creates default range adugey cheese
        """
        return self.__create_default_value(reposity.range_key,range_model.create("адыгейский сыр","Адыгейский сыр",self.create_gramm(),self.create_ingredients()))



    #@staticmethod
    def create_wafels_receipt(self):
        """
        Function that creates default receipt of wafels
        """
        proportions=[]
        proportions.append(proportion(self.create_flour(),100.0))
        proportions.append(proportion(self.create_sugar(),80.0))
        proportions.append(proportion(self.create_butter(),70.0))
        proportions.append(proportion(self.create_egg(),1.0))
        proportions.append(proportion(self.create_vanilin(),5.0))
        steps=[]
        steps.append(step("Как испечь вафли хрустящие в вафельнице? Подготовьте необходимые продукты. Из данного количества у меня получилось 8 штук диаметром около 10 см."))
        steps.append(step("Масло положите в сотейник с толстым дном. Растопите его на маленьком огне на плите, на водяной бане либо в микроволновке."))
        steps.append(step("Добавьте в теплое масло сахар. Перемешайте венчиком до полного растворения сахара. От тепла сахар довольно быстро растает."))
        steps.append(step("Добавьте в масло яйцо. Предварительно все-таки проверьте масло, не горячее ли оно, иначе яйцо может свариться. Перемешайте яйцо с маслом до однородности."))
        steps.append(step("Всыпьте муку, добавьте ванилин."))
        steps.append(step("Перемешайте массу венчиком до состояния гладкого однородного теста."))
        steps.append(step("Разогрейте вафельницу по инструкции к ней. У меня очень старая, еще советских времен электровафельница. Она может и не очень красивая, но печет замечательно!" \
                          " Я не смазываю вафельницу маслом, в тесте достаточно жира, да и к ней уже давно ничего не прилипает. Но вы смотрите по своей модели. Выкладывайте тесто по столовой ложке." \
                          " Можно класть немного меньше теста, тогда вафли будут меньше и их получится больше."))
        steps.append(step("Пеките вафли несколько минут до золотистого цвета. Осторожно откройте вафельницу, она очень горячая! Снимите вафлю лопаткой. Горячая она очень мягкая, как блинчик."))
        
        item=self.__create_default_value(reposity.receipt_key,receipt_model.create("Вафли Хрустящие",proportions,steps,20.0))
        return item

    #@staticmethod
    def create_hachapuri(self):
        """
        Function that creates default receipt of hachapuri
        """
        proportions=[]
        proportions.append(proportion(self.create_flour(),400.0))
        proportions.append(proportion(self.create_sugar(),15.0))
        proportions.append(proportion(self.create_butter(),100.0))
        proportions.append(proportion(self.create_egg(),5.0))
        proportions.append(proportion(self.create_milk(),125.0))
        proportions.append(proportion(self.create_yeasts(),7.0))
        proportions.append(proportion(self.create_water(),125.0))
        proportions.append(proportion(self.create_oil(),10.0))
        proportions.append(proportion(self.create_adugey_cheese(),250.0))
        proportions.append(proportion(self.create_mozarella_cheese(),200.0))
        steps=[]
        steps.append(step("Подготовить продукты для теста: просеять муку, подогреть молоко и воду"))
        steps.append(step("Смешать в чаше теплую воду и молоко, добавить сахар, дрожжи и пару ложек муки для опары"))
        steps.append(step("Убрать опару в теплое место на 10 минут до появления пенной шапки"))
        steps.append(step("Добавить в опару яйцо, растительное масло и соль, перемешать"))
        steps.append(step("Постепенно ввести всю муку, замешивать тесто 10 минут до эластичного состояния"))
        steps.append(step("Накрыть тесто и убрать в теплое место на 50-60 минут для подъема"))
        steps.append(step("Обмять подошедшее тесто и убрать подходить еще на 1 час"))
        steps.append(step("Натереть сыр на крупной терке, смешать с мягким сливочным маслом"))
        steps.append(step("Разделить тесто на 5 равных частей (примерно по 138 г), сформировать шарики"))
        steps.append(step("Раскатать каждый шарик в круглую лепешку толщиной 3-4 мм"))
        steps.append(step("Смазать противоположные края лепешки сырной начинкой (по ½ ст. ложки)"))
        steps.append(step("Завернуть края с начинкой к центру, защипнуть края для формирования лодочки"))
        steps.append(step("Перенести лодочки на противень, смазать яйцом, выложить начинку в середину"))
        steps.append(step("Разогреть духовку до 220°C, выпекать до золотистой корочки"))
        steps.append(step("Достать хачапури за 5 минут до готовности, сделать углубление в начинке и влить яйцо"))
        steps.append(step("Вернуть в духовку на несколько минут до схватывания белка"))
        item=self.__create_default_value(reposity.receipt_key,receipt_model.create("Хачапури по Адыгейски",proportions,steps,60.0))
        return item


    def start(self):
        """
        Function that start service and create default data
        """
        self.default_create_unit()
        self.default_create_range()
        self.default_create_range_group()
        self.default_create_receipt()
    

