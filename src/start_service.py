import json
import os

from .reposity import reposity
from .converters.convert_factory import convert_factory
from .core.abstract_reference import *
from .models.unit_model import unit_model
from .models.range_group_model import range_group_model
from .models.range_model import range_model
from .models.receipt_model import receipt_model
from .models.proportion import proportion
from .models.step import step
from .dto.abstract_dto import abstract_dto
from .dto.storage_dto import storage_dto
from .dto.range_dto import range_dto
from .dto.range_group_dto import range_group_dto
from .dto.transaction_dto import transaction_dto
from .dto.filter_dto import filter_dto
from .dto.receipt_dto import receipt_dto
from .dto.unit_dto import unit_dto
from .models.storage_model import storage_model
from .models.transaction_model import transaction_model
from .core.reposity_keys import reposity_keys
from .models.remnant_model import remnant_model,remnant_dto
import datetime
from .logics.prototype_report import prototype_report
from .core.abstract_logic import abstract_logic
from .core.observe_service import observe_service
from .core.event_type import event_type
class start_service(abstract_logic):
    """
    Class that creates all default data and start work of all service
    reposity:reposity - where the data contains
    __cache:dict - where ids contains
    """
    __reposity: reposity = reposity()
    __instance = None
    __block_datetime:datetime.datetime=None
    __cache={}
    def __init__(self):
        """
        Constructor of class
        """
        super().__init__()

        # Подключение в наблюдение
        observe_service.add(self)
        self.__reposity.data[reposity_keys.unit_key()] = {}
        self.__reposity.data[reposity_keys.range_key()] = {}
        self.__reposity.data[reposity_keys.range_group_key()] = {}
        self.__reposity.data[reposity_keys.receipt_key()] = {}
        self.__reposity.data[reposity_keys.storage_key()]={}
        self.__reposity.data[reposity_keys.transaction_key()]={}
        self.__reposity.data[reposity_keys.remnant_key()]={}

    """
    Реализация Singleton
    """
    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super(start_service, cls).__new__(cls)
        return cls.__instance
    
    def handle(self, event:str, params):
        super().handle(event, params)  
        
        if event==event_type.added_new_object() or event==event_type.object_deleted() or event==event_type.change_object():
            model_validator.validate(params,abstract_reference)
            if isinstance(params,transaction_model) or isinstance(params,range_model) or isinstance(params,transaction_model):
                self.create_block_remnant()

    @property
    def block_datetime(self):
        """
        Getter for block_datetime
        """
        return self.__block_datetime
    
    @block_datetime.setter
    def block_datetime(self,value:datetime.datetime):
        """
        Setter for block_datetime
        """
        model_validator.validate(value,datetime.datetime)
        self.__block_datetime=value
        observe_service.create_event(event_type.changed_block_datetime(),value)


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
        if obj.name not in [x.name for x in self.reposity.data[key].values()]:
            self.reposity.data[key][obj.uuid]=obj
            return self.reposity.data[key][obj.uuid]
        else:
            for old_obj in self.reposity.data[key].values():
                if old_obj.name==obj.name:
                    return old_obj
        

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
        item=self.__create_default_value(reposity_keys.unit_key(),unit_model.create("килограмм",inner_gramm,1000.0))
        return item
    
    #@staticmethod
    def create_gramm(self):
        """
        Creates default unit gramm
        """
        item=self.__create_default_value(reposity_keys.unit_key(),unit_model.create("грамм",None,1.0))
        return item
    
    #@staticmethod
    def create_litr(self):
        """
        Creates default unit litr
        """
        item=self.__create_default_value(reposity_keys.unit_key(),unit_model.create("литр",None,1.0))
        return item

    #@staticmethod
    def create_millilitr(self):
        """
        Creates default unit millilitr
        """
        item=self.__create_default_value(reposity_keys.unit_key(),unit_model.create("миллилитр",self.create_litr(),0.001))
        return item
    
    #@staticmethod
    def create_item(self):
        """
        Creates default unit item
        """
        item=self.__create_default_value(reposity_keys.unit_key(),unit_model.create("штука",None,1.0))
        return item


    #@staticmethod
    def create_ingredients(self):
        """
        Function that creates deafult value ingridients
        """
        return self.__create_default_value(reposity_keys.range_group_key(),range_group_model.create("ингридиенты"))

    #@staticmethod
    def create_milk(self):
        """
        Creates default range milk
        """
        return self.__create_default_value(reposity_keys.range_key(),range_model.create("молоко","Молоко пастеризованное натуральное",self.create_litr(),self.create_ingredients()))

    #@staticmethod
    def create_salt(self):
        """
        Creates default range salt
        """
        return self.__create_default_value(reposity_keys.range_key(),range_model.create("соль","Соль пищевая кристализованная",self.create_killogramm(),self.create_ingredients()))


    #@staticmethod
    def create_sugar(self):
        """
        Creates default range sugar
        """
        return self.__create_default_value(reposity_keys.range_key(),range_model.create("сахар","Сахар песок",self.create_killogramm(),self.create_ingredients()))


    #@staticmethod
    def create_flour(self):
        """
        Creates default range flour
        """
        return self.__create_default_value(reposity_keys.range_key(),range_model.create("мука","Мука пшеничная 1 сорт",self.create_killogramm(),self.create_ingredients()))
    
    #@staticmethod
    def create_egg(self):
        """
        Creates default range egg
        """
        return self.__create_default_value(reposity_keys.range_key(),range_model.create("яйцо","Яйцо куринное",self.create_item(),self.create_ingredients()))

    
    #@staticmethod
    def create_butter(self):
        """
        Creates default range butter
        """
        return self.__create_default_value(reposity_keys.range_key(),range_model.create("масло сливочное","Масло сливочное натуральное",self.create_gramm(),self.create_ingredients()))

    
    #@staticmethod
    def create_vanilin(self):
        """
        Creates default range vanilin
        """
        return self.__create_default_value(reposity_keys.range_key(),range_model.create("ванилин","Ванилин пищевой ароматизатор",self.create_gramm(),self.create_ingredients()))



    #@staticmethod
    def create_water(self):
        """
        Creates default range water
        """
        return self.__create_default_value(reposity_keys.range_key(),range_model.create("вода","Вода питьевая негазированная",self.create_millilitr(),self.create_ingredients()))

    #@staticmethod
    def create_oil(self):
        """
        Creates default range oil
        """
        return self.__create_default_value(reposity_keys.range_key(),range_model.create("масло растительное","Масло растительное подсолнечное",self.create_millilitr(),self.create_ingredients()))


    #@staticmethod
    def create_yeasts(self):
        """
        Creates default range yests
        """
        return self.__create_default_value(reposity_keys.range_key(),range_model.create("дрожжи","Дрожжи сухие",self.create_gramm(),self.create_ingredients()))


    #@staticmethod
    def create_mozarella_cheese(self):
        """
        Creates default range mozarella cheese
        """
        return self.__create_default_value(reposity_keys.range_key(),range_model.create("моцарелла сыр","Сыр моцарелла",self.create_gramm(),self.create_ingredients()))

    
    #@staticmethod
    def create_adugey_cheese(self):
        """
        Creates default range adugey cheese
        """
        return self.__create_default_value(reposity_keys.range_key(),range_model.create("адыгейский сыр","Адыгейский сыр",self.create_gramm(),self.create_ingredients()))



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
        
        item=self.__create_default_value(reposity_keys.receipt_key(),receipt_model.create("Вафли Хрустящие",proportions,steps,20.0))
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
        item=self.__create_default_value(reposity_keys.receipt_key(),receipt_model.create("Хачапури по Адыгейски",proportions,steps,60.0))
        return item

    def create_storage_a(self):
        item=storage_model()
        item.name="Storage A"
        self.__create_default_value(reposity_keys.storage_key(),item)

    def create_storage_b(self):
        item=storage_model()
        item.name="Storage B"
        self.__create_default_value(reposity_keys.storage_key(),item)

    def default_create_storages(self):
        self.create_storage_a()
        self.create_storage_b()
    
    def default_create_transactions(self):
        start_date=datetime.datetime.strptime("2024-01-01T12:00:00","%Y-%m-%dT%H:%M:%S")
        storage=list(self.reposity.data[reposity_keys.storage_key()].values())[0]
        for day in range(0,365):
            for ind,range_obj in enumerate(self.reposity.data[reposity_keys.range_key()].values()):
                item=transaction_model()
                item.name=f"Transaction #{day}-{ind+1}"
                item.range=range_obj
                item.storage=storage
                if day%2==0:
                    item.amount=10.0
                else:
                    item.amount=-5.0
                item.unit=range_obj.unit
                item.datetime=start_date+datetime.timedelta(days=day)
                self.__create_default_value(reposity_keys.transaction_key(),item)

    def create_block_remnant(self):
        self.reposity.data[reposity_keys.remnant_key()]={}
        remnants=self.create_remnant(self.block_datetime)
        for remnant_obj in remnants:
            self.__create_default_value(reposity_keys.remnant_key(),remnant_obj)


    def create_remnant(self,target_datetime:datetime.datetime):
        """
        Create remnants before block_datetime
        """
        model_validator.validate(target_datetime,datetime.datetime)
        remnants={}
        datetime_filters=[filter_dto.create("datetime","lt",target_datetime)]
        base_remnants=None
        if self.reposity.data[reposity_keys.remnant_key()]!={} and target_datetime>=self.block_datetime:
            base_remnants=prototype_report(list(self.reposity.data[reposity_keys.remnant_key()].values()))
            datetime_filters.append(filter_dto.create("datetime","ge",self.block_datetime))
        transactions=list(self.reposity.data[reposity_keys.transaction_key()].values())
        base_prototype=prototype_report(transactions)
        datetime_filtered_prototype=base_prototype.filter(datetime_filters)
        for transaction_obj in datetime_filtered_prototype.data:
            if transaction_obj.storage.name not in remnants.keys():
                remnants[transaction_obj.storage.name]={}
            if transaction_obj.range.name not in remnants[transaction_obj.storage.name].keys():
                unit_uuid,coef=transaction_obj.unit.get_base()
                unit_obj=self.reposity.data[reposity_keys.unit_key()][unit_uuid]
                remnant_start_value=0.0
                if base_remnants is not None:
                    find_filter=filter_dto.create("name","eq",f"{transaction_obj.storage.name}-{transaction_obj.range.name}")
                    remnant_start_value=base_remnants.filter([find_filter]).data[0].remnant_value
                remnants[transaction_obj.storage.name][transaction_obj.range.name]=remnant_model.create(
                    transaction_obj.range,
                    transaction_obj.storage,
                    unit_obj,
                    remnant_start_value,
                    target_datetime
                    )
                remnants[transaction_obj.storage.name][transaction_obj.range.name].name=f"{transaction_obj.storage.name}-{transaction_obj.range.name}"
            base_unit_uuid,coef=transaction_obj.unit.get_base()
            remnants[transaction_obj.storage.name][transaction_obj.range.name].remnant_value+=transaction_obj.amount*coef
        result=[]
        for storage_remnants in remnants.values():
            result+=list(storage_remnants.values())
        return result
            

        #base_prototype=prototype_report(transactions)
        
        #for storage_obj in self.reposity.data[reposity_keys.storage_key()].values():
        #    storage_filters=[filter_dto.create("storage.uuid","eq",storage_obj.uuid)]   
        #    storage_filtered_prototype=base_prototype.filter(storage_filters)
        #    if self.reposity.data[reposity_keys.remnant_key()]!={} and target_datetime>=self.block_datetime:
        #        storage_filtered_remnants= base_remnants.filter(storage_filters)
        #    datetime_filtered_prototype=storage_filtered_prototype.filter(datetime_filters)
        #    for range_obj in list(self.reposity.data[reposity_keys.range_key()].values()):
        #        range_filters=[
        #            filter_dto.create("range","eq",range_obj)
        #        ]
        #        remnant_value=0.0
        #        if self.reposity.data[reposity_keys.remnant_key()]!={} and target_datetime>=self.block_datetime:
        #            range_filtered_remnant=storage_filtered_remnants.filter(range_filters).data[0]
        #            remnant_value=range_filtered_remnant.remnant_value
        #        unit_obj=range_obj.unit
        #        remnant_prototype=prototype_report.filter(datetime_filtered_prototype,range_filters)
        #        for transaction_obj in remnant_prototype.data:
        #            unit_name,coef=transaction_obj.unit.get_base()
        #            remnant_value+=transaction_obj.amount*coef
        #            unit_obj=self.reposity.data[reposity_keys.unit_key()][unit_name]
        #        remnant_obj=remnant_model.create(range_obj,storage_obj,unit_obj,remnant_value,target_datetime)
        #        remnant_obj.name=f"{storage_obj.name}-{range_obj.name}"
        #        remnants.append(remnant_obj)
        #return remnants
    def reposity_to_json(self):
        data={}
        data[reposity_keys.unit_json_key()]=convert_factory().convert(self.reposity.data[reposity_keys.unit_key()])
        data[reposity_keys.range_group_json_key()]=convert_factory().convert(self.reposity.data[reposity_keys.range_group_key()])
        data[reposity_keys.range_json_key()]=convert_factory().convert(self.reposity.data[reposity_keys.range_key()])
        data[reposity_keys.receipt_json_key()]=convert_factory().convert(self.reposity.data[reposity_keys.receipt_key()])
        data[reposity_keys.storage_json_key()]=convert_factory().convert(self.reposity.data[reposity_keys.storage_key()])
        data[reposity_keys.transcation_json_key()]=convert_factory().convert(self.reposity.data[reposity_keys.transaction_key()])
        data[reposity_keys.remnant_json_key()]=convert_factory().convert(self.reposity.data[reposity_keys.remnant_key()])
        return data

    def save_data_to_config(self,filename):
        """
        Function that saves all data values to config
        """
        data=self.reposity_to_json()
        data=json.dumps(data,indent=4)
        try:
            with open(filename,"w",encoding="UTF-8") as config:
                config.write(data)
                return True
        except Exception as e:
            return False
    
    def save_data(self,filename):
        """
        Function that saves all data in balance_sheet
        """
        data=self.reposity_to_json()
        data=json.dumps(data,indent=4)
        try:
            with open(filename,"w",encoding="UTF-8") as config:
                config.write(data)
                return True
        except Exception as e:
            return False


    def load(self,filename:str):
        """
        Function that load data from file
        """
        if filename == "":
            raise operation_exception("Не найден файл настроек!")
        try:
            with open(filename, 'r',encoding="UTF-8") as file_instance:
                data = json.load(file_instance)
                return self.convert(data)

            return False
        except Exception as e:
            #raise e
            return False
    
    def __save_item(self, key:str, dto:abstract_dto, item:abstract_reference):
        model_validator.validate(key, str)
        item.uuid = dto.uuid
        self.__cache.setdefault(dto.uuid, item)
        self.reposity.data[key][item.uuid]=item

    def __convert_units(self, data: dict) -> bool:
        model_validator.validate(data, dict)
        units = data['units'] if 'units' in data else []    
        if len(units) == 0:
            return False
         
        for unit in units.values():
            dto = unit_dto().create(unit)
            item = unit_model.from_dto(dto, self.reposity.data)
            self.__save_item( reposity_keys.unit_key(), dto, item )

        return True

    # Загрузить группы номенклатуры
    def __convert_groups(self, data: dict) -> bool:
        model_validator.validate(data, dict)
        range_groups =  data['range_groups'] if 'range_groups' in data else []    
        if len(range_groups) == 0:
            return False

        for range_group in range_groups.values():
            dto = range_group_dto().create(range_group)    
            item = range_group_model.from_dto(dto, self.reposity.data)
            self.__save_item(reposity_keys.range_group_key(), dto, item)

        return True

    # Загрузить номенклатуру
    def __convert_ranges(   self, data: dict) -> bool:
        model_validator.validate(data, dict)      
        ranges = data['ranges'] if 'ranges' in data else []   
        if len(ranges) == 0:
            return False
         
        for range in ranges.values():
            dto = range_dto().create(range)
            item = range_model.from_dto(dto, self.reposity.data)
            self.__save_item( reposity_keys.range_key(), dto, item )

        return True     
    
    def __convert_storages(self, data: dict) -> bool:
        model_validator.validate(data, dict)      
        storages = data['storages'] if 'storages' in data else []   
        if len(storages) == 0:
            return False
         
        for storage in storages.values():
            dto = storage_dto().create(storage)
            item = storage_model.from_dto(dto, self.reposity.data)
            self.__save_item( reposity_keys.storage_key(), dto, item )

        return True   

    def __convert_transactions(self, data: dict) -> bool:
        model_validator.validate(data, dict)      
        transactions = data['transactions'] if 'transactions' in data else []   
        if len(transactions) == 0:
            return False
         
        for transaction in transactions.values():
            dto = transaction_dto().create(transaction)
            item = transaction_model.from_dto(dto, self.reposity.data)
            self.__save_item( reposity_keys.transaction_key(), dto, item )

        return True   

    def __convert_receipt(self,data:dict)->bool:
        model_validator.validate(data, dict)
        receipts=data["receipts"] if "receipts" in data else []   
        if len(receipts)==0:
            return False
        for receipt in receipts.values():
            dto=receipt_dto().create(receipt)
            item=receipt_model.from_dto(dto,self.reposity.data)
            self.__save_item(reposity_keys.receipt_key(),dto,item)
        return True 
    
    def __convert_remnants(self,data:dict)->bool:
        model_validator.validate(data, dict)
        remnants=data["remnants"] if "remnants" in data else []   
        if len(remnants)==0:
            return False
        for remnant in remnants.values():
            dto=receipt_dto().create(remnant)
            item=receipt_model.from_dto(dto,self.reposity.data)
            self.__save_item(reposity_keys.remnant_key(),dto,item)
        return True 

    def convert(self, data: dict) -> bool:
        """
        Function that convert data from config
        """
        model_validator.validate(data, dict)
        self.__convert_units(data)    
        self.__convert_groups(data)  
        self.__convert_ranges(data)
        self.__convert_receipt(data)
        self.__convert_storages(data)
        self.__convert_transactions(data)
        self.__convert_remnants(data)
        return True

    def start(self,create_default:bool=True):
        """
        Function that start service and create default data
        """
        #if os.path.exists("default_data.json"):
        #    self.load("default_data.json")
        if create_default:
            self.default_create_unit()
            self.default_create_range()
            self.default_create_range_group()
            self.default_create_receipt()
            self.default_create_storages()
            self.default_create_transactions()
        else:
            self.load("default_data.json")
        
        if self.block_datetime:
            self.create_block_remnant()
    

    def create_balance_sheet(self,start_datetime_filters:list,main_datetime_filters:list,storage_filters:list,other_filters:list=[]):
        transactions=list(self.reposity.data[reposity_keys.transaction_key()].values())
        base_prototype=prototype_report(transactions)
        
        base_filtered_prototype=base_prototype.filter(other_filters)

        balance_sheet=[]
        storage_filtered_prototype=base_filtered_prototype.filter(storage_filters)
        
        start_balance_datetime_filtered_prototype=storage_filtered_prototype.filter(start_datetime_filters)
        
        main_datetime_filtered_prototype=storage_filtered_prototype.filter(main_datetime_filters)
        for range_obj in list(self.reposity.data[reposity_keys.range_key()].values()):
            range_filters=[
                filter_dto.create("range","eq",range_obj)
            ]
            balance_sheet_item={}
            balance_sheet_item["range"]=range_obj.name
            balance_sheet_item["unit"]=None
            balance_sheet_item["start_balance"]=0
            balance_sheet_item["end_balance"]=0
            balance_sheet_item["in"]=0
            balance_sheet_item["out"]=0
            start_balance_range_filtered_prototype=prototype_report.filter(start_balance_datetime_filtered_prototype,range_filters)
            for transaction_obj in start_balance_range_filtered_prototype.data:
                unit_name,coef=transaction_obj.unit.get_base()
                balance_sheet_item["unit"]=unit_name
                balance_sheet_item["start_balance"]+=transaction_obj.amount*coef
                balance_sheet_item["end_balance"]+=transaction_obj.amount*coef
            main_balance_range_filtered_prototype=prototype_report.filter(main_datetime_filtered_prototype,range_filters)
            for transaction_obj in main_balance_range_filtered_prototype.data:
                unit_name,coef=transaction_obj.unit.get_base()
                balance_sheet_item["unit"]=unit_name
                balance_sheet_item["end_balance"]+=transaction_obj.amount*coef    
                balance_sheet_item["in"]+=abs(transaction_obj.amount*coef) if transaction_obj.amount>0 else 0
                balance_sheet_item["out"]+=abs(transaction_obj.amount*coef) if transaction_obj.amount<0 else 0
            
            balance_sheet.append(balance_sheet_item)
        return balance_sheet
    
    def create_balance_sheet_with_remnants(self,start_datetime_filters:list,main_datetime_filters:list,storage_filters:list,other_filters:list=[]):
        transactions=list(self.reposity.data[reposity_keys.transaction_key()].values())
        base_prototype=prototype_report(transactions)
        
        base_filtered_prototype=base_prototype.filter(other_filters)

        balance_sheet=[]
        storage_filtered_prototype=base_filtered_prototype.filter(storage_filters)
        s_d_f=start_datetime_filters.copy()
        if self.block_datetime is not None:
            s_d_f.append(filter_dto.create("datetime","ge",self.block_datetime))
        
        remnants=list(self.reposity.data[reposity_keys.remnant_key()].values())
        remnant_prototype=prototype_report(remnants)
        storage_filtered_remnants=remnant_prototype.filter(storage_filters)

        start_balance_datetime_filtered_prototype=storage_filtered_prototype.filter(s_d_f)
        main_datetime_filtered_prototype=storage_filtered_prototype.filter(main_datetime_filters)
        for range_obj in list(self.reposity.data[reposity_keys.range_key()].values()):
            
            range_filters=[
                filter_dto.create("range","eq",range_obj)
            ]
            
            range_filtered_remnant_prototype=storage_filtered_remnants.filter(range_filters)
            remnant_obj=range_filtered_remnant_prototype.data[0]
            balance_sheet_item={}
            balance_sheet_item["range"]=range_obj.name
            balance_sheet_item["unit"]=remnant_obj.unit
            balance_sheet_item["start_balance"]=remnant_obj.remnant_value
            balance_sheet_item["end_balance"]=remnant_obj.remnant_value
            balance_sheet_item["in"]=0
            balance_sheet_item["out"]=0
            
            start_balance_range_filtered_prototype=prototype_report.filter(start_balance_datetime_filtered_prototype,range_filters)
            #breakpoint()
            for transaction_obj in start_balance_range_filtered_prototype.data:
                unit_name,coef=transaction_obj.unit.get_base()
                balance_sheet_item["unit"]=unit_name
                balance_sheet_item["start_balance"]+=transaction_obj.amount*coef
                balance_sheet_item["end_balance"]+=transaction_obj.amount*coef
            main_balance_range_filtered_prototype=prototype_report.filter(main_datetime_filtered_prototype,range_filters)
            for transaction_obj in main_balance_range_filtered_prototype.data:
                unit_name,coef=transaction_obj.unit.get_base()
                balance_sheet_item["unit"]=unit_name
                balance_sheet_item["end_balance"]+=transaction_obj.amount*coef    
                balance_sheet_item["in"]+=abs(transaction_obj.amount*coef) if transaction_obj.amount>0 else 0
                balance_sheet_item["out"]+=abs(transaction_obj.amount*coef) if transaction_obj.amount<0 else 0
            
            balance_sheet.append(balance_sheet_item)
        return balance_sheet