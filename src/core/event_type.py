"""
Типы событий
"""
class event_type:

    
    
    """
    Событие - сформирован Json
    """
    @staticmethod
    def convert_to_json() -> str:
        return "convert_to_json"


    """
    Событие - добавление нового объекта
    """
    @staticmethod
    def add_new_object() -> str:
        return "add_new_object"

    """
    Событие - объект добавлен
    """
    @staticmethod
    def added_new_object() -> str:
        return "added_new_object"


    """
    Событие - не удалось добавить объект
    """
    @staticmethod
    def cant_add_object() -> str:
        return "cant_add_object"
    """
    Событие - измненение существующего объекта
    """
    @staticmethod
    def change_object() -> str:
        return "change_object"
    
    """
    Событие - удаление существующего объекта объекта
    """
    @staticmethod
    def start_deletion_object() -> str:
        return "start_deletion_object"

    """
    Событие - объект удален
    """
    @staticmethod
    def object_deleted() -> str:
        return "object_deleted"

    """
    Событие - не удалось удалить объект
    """
    @staticmethod
    def cant_delete_object() -> str:
        return "cant_delete_object"

    """
    Событие - не удалось удалить объект
    """
    @staticmethod
    def cant_delete_object() -> str:
        return "cant_delete_object"


    """
    Событие - смена даты блокировки
    """
    @staticmethod
    def changed_block_datetime() -> str:
        return "changed_block_datetime"
    
    """
    Событие - ответ на запрос
    """
    @staticmethod
    def response_to_request() -> str:
        return "response_to_request"

    """
    Событие - ошибка ответа на запрос
    """
    @staticmethod
    def cant_response_to_request() -> str:
        return "cant_response_to_request"

    """
    Событие - внутренняя ошибка
    """
    @staticmethod
    def inner_error() -> str:
        return "inner_error"

    """
    Получить список всех событий
    """
    @staticmethod
    def events() -> list:
        result = []
        methods = [method for method in dir(event_type) if
                    callable(getattr(event_type, method)) and not method.startswith('__') and method != "events"]
        for method in methods:
            key = getattr(event_type, method)()
            result.append(key)

        return result