
from .basic_converter import basic_converter
from .datetime_converter import datetime_converter
from .reference_converter import reference_converter
from ..models.abstract_reference import abstract_reference
from ..models.proportion import proportion
from ..dto.abstract_dto import abstract_dto
from ..models.step import step
from ..core.common import common
from ..models.abstract_reference import argument_exception
import datetime
class convert_factory:
    """
    Class for universal converting objects to dict
    """    

    __converters={
        str:basic_converter,
        int:basic_converter,
        float:basic_converter,
        datetime.datetime:datetime_converter,
        datetime.date:datetime_converter,
        abstract_reference:reference_converter,
        proportion:reference_converter,
        step:reference_converter,
        abstract_dto:basic_converter,
        object:basic_converter
    }
    
    def convert(self,obj:any):
        """
        Function to converting any object to dict
        """
        if type(obj) in [str,int,float,datetime.datetime,datetime.date] or obj is None:
            return self.__converters[type(obj).__bases__[0]].convert(obj)
        elif isinstance(obj,list):
            sub_list=[]
            for item in obj:
                sub_list.append(self.convert(item))
            return sub_list
        elif isinstance(obj,dict):
            sub_dict={}
            for dict_key in obj.keys():
                sub_dict[dict_key]=self.convert(obj[dict_key])
            return sub_dict
        try:
            convert_obj=self.__converters[type(obj).__bases__[0]].convert(obj)
            fields=common.get_fields(convert_obj)
            data={}
            for key in fields:
                attr=getattr(convert_obj, key) 
                data[key]=self.convert(attr)
            return data
        except Exception as e:
            raise e
            raise argument_exception("There is not converter for this type")