from .abstract_reference import *
from .range_model import range_model
from .range_group_model import range_group_model
from .step import step
from.proportion import proportion

class receipt_model(abstract_reference):
    """
    Class that contains info about receipt
    ingridients:list[proportion] - all proportions of receipt
    steps:list[step] - all steps of instruction for receipts
    """
    __ingridients:list[proportion]
    __steps:list[step]
    __time:float
    def __init__(self,name:str=None,ingridients:list[proportion]=None,steps:list[step]=None,time=None):
        """
        Constructor of class
        name:str
        ingridients:list[proportion]
        steps:list[step]
        """
        super().__init__(name)
        self.ingridients=ingridients
        self.steps=steps
        self.time=time
    
    @property
    def ingridients(self):
        """
        Function that returns ingridients
        """
        return self.__ingridients
    
    @ingridients.setter
    def ingridients(self,value:list[proportion]):
        """
        Function that sets property ingridients
        value:list[proportion]
        """
        if value is None or self._prop_validator.check_type(value,list):
            if value is not None and all(self._prop_validator.check_type(prop,proportion) for prop in value):
                self.__ingridients=value
            elif value is None:
                self.__ingridients=value   
            else:
                raise argument_exception("ingridients should be list of proportions")
        else:
            raise argument_exception("ingridients should be list of proportions")

    @property
    def steps(self):
        """
        Function that returns steps
        """
        return self.__steps
    
    @steps.setter
    def steps(self,value:list[step]):
        """
        Function that sets property steps
        value:list[step]
        """
        if value is None or self._prop_validator.check_type(value,list):
            if value is not None and all(self._prop_validator.check_type(stp,step) for stp in value):
                self.__steps=value
            elif value is None:
                self.__steps=value 
            else:
                raise argument_exception("steps should be list of steps")
        else:
            raise argument_exception("steps should be list of steps")
    
    @property
    def time(self):
        """
        Function that returns time
        """
        return self.__time
    
    @time.setter
    def time(self,value:float):
        """
        Function that sets property time
        value:float
        """
        if value is None or self._prop_validator.check_type(value,float):
            self.__time=value   
        else:
            raise argument_exception("time should be float")

    @staticmethod
    @singleton_result
    def create_wafels_receipt():
        """
        Function that creates default receipt of wafels
        """
        proportions=[]
        proportions.append(proportion(range_model.create_flour(),100.0))
        proportions.append(proportion(range_model.create_sugar(),80.0))
        proportions.append(proportion(range_model.create_butter(),70.0))
        proportions.append(proportion(range_model.create_egg(),1.0))
        proportions.append(proportion(range_model.create_vanilin(),5.0))
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
        
        item=receipt_model.create("Вафли Хрустящие",proportions,steps,20.0)
        return item

    @staticmethod
    @singleton_result
    def create_hachapuri():
        """
        Function that creates default receipt of hachapuri
        """
        proportions=[]
        proportions.append(proportion(range_model.create_flour(),400.0))
        proportions.append(proportion(range_model.create_sugar(),15.0))
        proportions.append(proportion(range_model.create_butter(),100.0))
        proportions.append(proportion(range_model.create_egg(),5.0))
        proportions.append(proportion(range_model.create_milk(),125.0))
        proportions.append(proportion(range_model.create_yeasts(),7.0))
        proportions.append(proportion(range_model.create_water(),125.0))
        proportions.append(proportion(range_model.create_oil(),10.0))
        proportions.append(proportion(range_model.create_adugey_cheese(),250.0))
        proportions.append(proportion(range_model.create_mozarella_cheese(),200.0))
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
        item=receipt_model.create("Хачапури по Адыгейски",proportions,steps,60.0)
        return item

    @staticmethod
    def create(name:str,ingridients:list[proportion],steps:list[step],time:float):
        """
        Function that creates receipt
        """
        return receipt_model(name,ingridients,steps,time)