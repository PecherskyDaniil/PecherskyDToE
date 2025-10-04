from .reposity import *
from .models.unit_model import unit_model
from .models.range_group_model import range_group_model
from .models.range_model import range_model
from .models.receipt_model import receipt_model
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
    
    def default_create_unit(self):
        """
        Function that creates all default units
        """
        self._add_unit_to_reposity(unit_model.create_killogramm())
        self._add_unit_to_reposity(unit_model.create_gramm())
        self._add_unit_to_reposity(unit_model.create_litr())
        self._add_unit_to_reposity(unit_model.create_millilitr())
        self._add_unit_to_reposity(unit_model.create_item())
    
    def default_create_range_group(self):
        """
        Function that creates all default range_groups
        """
        self._add_range_group_to_reposity(range_group_model.create_ingredients())
        
    def default_create_range(self):
        """
        Function that creates all default ranges
        """
        self._add_range_to_reposity(range_model.create_egg())
        self._add_range_to_reposity(range_model.create_flour())
        self._add_range_to_reposity(range_model.create_milk())
        self._add_range_to_reposity(range_model.create_salt())
        self._add_range_to_reposity(range_model.create_sugar())
        self._add_range_to_reposity(range_model.create_adugey_cheese())
        self._add_range_to_reposity(range_model.create_mozarella_cheese())
        self._add_range_to_reposity(range_model.create_vanilin())
        self._add_range_to_reposity(range_model.create_oil())
        self._add_range_to_reposity(range_model.create_butter())
        self._add_range_to_reposity(range_model.create_yeasts())
        self._add_range_to_reposity(range_model.create_water())

    def default_create_receipt(self):
        """
        Function that creates all default receipts
        """
        self._add_receipt_to_reposity(receipt_model.create_wafels_receipt())
        self._add_receipt_to_reposity(receipt_model.create_hachapuri())

    def _add_unit_to_reposity(self,unit:unit_model):
        """
        Function that add unit to reposity
        """
        self.__reposity.data[reposity.unit_key][unit.name]=unit
    
    def _add_range_group_to_reposity(self,range_group:range_group_model):
        """
        Function that add range_group to reposity
        """
        self.__reposity.data[reposity.range_group_key][range_group.name]=range_group

    def _add_range_to_reposity(self,range:range_model):
        """
        Function that add range to reposity
        """
        self.__reposity.data[reposity.range_key][range.name]=range

    def _add_receipt_to_reposity(self,receipt:receipt_model):
        """
        Function that add receipt to reposity
        """
        self.__reposity.data[reposity.receipt_key][receipt.name]=receipt

    def start(self):
        """
        Function that start service and create default data
        """
        self.default_create_unit()
        self.default_create_range()
        self.default_create_range_group()
        self.default_create_receipt()
    

