from .abstract_response import abstract_response
from ..core.common import common
from ..core.abstract_reference import abstract_reference

class response_csv(abstract_response):
    """
    Class for response csv formatter
    """
    # Сформировать CSV
    @staticmethod
    def response_type():
        """
        Type of API response
        """
        return "text/plain"
    
    def create(self, data: list):
        """
        Function that convert data to csv format
        """
        text = super().create(data)
        dict_obj=self.build_object_dict(data)
        item = dict_obj[0]
        fields = item.keys()
        # Шапка
        text=";".join(fields)
        text+="\n"
        # Данные
        for item in dict_obj:
            table_line=[]
            for field in fields:
                attr=item[field]
                if isinstance(attr,str):
                    table_line.append(f"\"{attr}\"")
                else:
                    table_line.append(f"{attr}")
            text+=";".join(table_line)+"\n"
        return text   
    
    