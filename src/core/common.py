from ..models.abstract_reference import *

class common:
    """
    Class for common operations with models
    """

    @staticmethod
    def get_models() -> list:
        """
        Function that gets all models names
        """
        result = []
        for  inheritor in abstract_reference.__subclasses__():
            result.append(inheritor.__name__)

        return result    


    
    @staticmethod
    def get_fields(source:any, is_common: bool = False) -> list:
        """
        Function that gets all filead of any model
        source:any - source model for fields
        is_common:bool - exception for lists and dicts
        """
        if source is None:
            raise argument_exception("Некорректно переданы аргументы!")

        items = list(filter(lambda x: not x.startswith("_") , dir(source))) 
        result = []

        for item in items:
            attribute = getattr(source.__class__, item)
            if isinstance(attribute, property):
                value = getattr(source, item)

                # is_common check
                if is_common == True and (isinstance(value, dict) or isinstance(value, list) ):
                    continue

                result.append(item)

        return result

