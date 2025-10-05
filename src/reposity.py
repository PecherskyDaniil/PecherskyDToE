
class reposity:
    """
    Class that contains data of all system
    data:dict - dict of all data
    """
    __data:dict={}
    @property
    def data(self):
        """
        Function that returns data
        """
        return self.__data
    @data.setter
    def data(self,data:dict):
        """
        Function that sets property data
        value:dict
        """
        self.__data=data
    @property
    def unit_key():
        """
        Function that returns data key for units
        """
        return "unit_model"
    @property
    def range_group_key():
        """
        Function that returns data key for range_groups
        """
        return "range_group_model"
    @property
    def range_key():
        """
        Function that returns data key for ranges
        """
        return "range_model"
    @property
    def receipt_key():
        """
        Function that returns data key for receipts
        """
        return "receipt_model"