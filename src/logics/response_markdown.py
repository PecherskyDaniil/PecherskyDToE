from .abstract_response import abstract_response
from ..core.common import common
from ..models.abstract_reference import abstract_reference

class response_markdown(abstract_response):
    """
    Class for response markdown formatter
    """
    # Сформировать markdown
    def create(self, data: list):
        """
        Function that convert data to markdown format
        """
        text = super().create(data)
        dict_obj=self.build_object_dict(data)
        item = dict_obj[0]
        fields = item.keys()
        # Шапка
        text+=f"|{'|'.join(fields)}|"+"\n"
        text+="|---"*len(fields)+"\n"
        # Данные
        for item in dict_obj:
            table_line=[]
            for field in fields:
                attr=item[field]
                if isinstance(attr,str):
                    table_line.append(f"\"{attr}\"")
                else:
                    table_line.append(f"{attr}")
            text+=f"|{'|'.join(table_line)}|"+"\n"
        return text   