from .abstract_dto import abstract_dto

class transaction_dto(abstract_dto):
    """
    Class for work with transactions dto. Inherited from abstract_dto
    """
    __datetime:str=None
    __range_id:str=None
    __storage_id:str=None
    __amount:float=None
    __unit_id:str=None
    __name:str = ""
    __uuid:str = ""

    @property
    def name(self) ->str:
        """
        Property name
        """
        return self.__name
    
    @name.setter
    def name(self, value):
        """
        Setter for property name
        """
        self.__name = value

    @property
    def uuid(self) -> str:
        """
        Property id
        """
        return self.__uuid

    @uuid.setter
    def uuid(self, value):
        """
        Setter for property id
        """
        self.__uuid = value  

    @property
    def datetime(self) -> str:
        """
        Function that returns property datetime
        """
        return self.__datetime

    @datetime.setter
    def datetime(self, value:datetime):
        """
        Function that sets property datetime
        value - datetime
        """
        self.__datetime = value


    @property
    def range_id(self) -> str:
        """
        Function that returns property range
        """
        return self.__range_id

    @range_id.setter
    def range_id(self, value:str):
        """
        Function that sets property range
        value - str
        """
        self.__range_id = value
    

    @property
    def storage_id(self) -> str:
        """
        Function that returns property storage_id
        """
        return self.__storage_id

    @storage_id.setter
    def storage_id(self, value:str):
        """
        Function that sets property storage_id
        value - str
        """
        self.__storage_id = value

    @property
    def amount(self) -> float:
        """
        Function that returns property amount
        """
        return self.__amount

    @amount.setter
    def amount(self, value:float):
        """
        Function that sets property amount
        value - amount
        """
        self.__amount = value

    @property
    def unit_id(self) -> str:
        """
        Function that returns property unit_id
        """
        return self.__unit_id

    @unit_id.setter
    def unit_id(self, value:str):
        """
        Function that sets property unit_id
        value - str
        """
        self.__unit_id = value
