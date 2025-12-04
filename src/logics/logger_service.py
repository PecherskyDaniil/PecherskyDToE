
from ..core.event_type import event_type
from ..core.reposity_keys import reposity_keys
from ..core.abstract_logic import abstract_logic
from ..core.observe_service import observe_service
from ..core.abstract_reference import model_validator,operation_exception,abstract_reference
from ..core.abstract_reference import abstract_reference
from ..core.log_levels import log_levels
from ..converters.convert_factory import convert_factory
import datetime
import sys
class logger_service(abstract_logic):
    """
    Class for service object changes
    """
    __log_level:str=None
    __log_dir:str=None
    _info_events=[event_type.added_new_object(),event_type.change_object(),event_type.changed_block_datetime(),event_type.object_deleted()]
    _error_events=[event_type.cant_add_object(),event_type.cant_delete_object(),event_type.cant_response_to_request(),event_type.cant_response_to_request(),event_type.inner_error()]


    @property
    def log_dir(self):
        """
        Getter for log directory
        """
        return self.__log_dir
    
    @log_dir.setter
    def log_dir(self,value:str):
        """
        Setter for log directory
        """
        model_validator.validate(value,str)
        self.__log_dir=value


    @property
    def log_level(self):
        """
        Getter for log level
        """
        return self.__log_level
    
    @log_level.setter
    def log_level(self,value:str):
        """
        Setter for log level
        """
        model_validator.validate(value,str)
        self.__log_level=value
    def __init__(self,log_dir:str=None,log_level:str=log_levels.DEBUG()):
        """
        Constructor
        """
        super().__init__()
        self.log_dir=log_dir
        self.log_level=log_level
        # Подключение в наблюдение
        observe_service.add(self)
   
    """
    Обработка событий
    """
    def handle(self, event:str, params):
        log_row=""
        data=None
        current_log_level=log_levels.DEBUG()
        if event in self._info_events:
            current_log_level=log_levels.INFO()
        elif event in self._error_events:
            current_log_level=log_levels.ERROR()
        if log_levels.LEVELS_RANK()[current_log_level]>log_levels.LEVELS_RANK()[self.log_level]:
            return False
        if isinstance(params,list) and len(params)>1 and isinstance(params[1],abstract_reference):
            data=convert_factory().convert(params[1].to_dto())
        else:
            data=params
        log_row=self.compose_log_row(current_log_level,event,data)
        if self.log_dir:
            self.save_to_file(log_row)
        else:
            sys.stdin.write(log_row)   
             
    def compose_log_row(self,status:str,event:str,data:str):
        """
        Create row of log_file
        """
        return f"{datetime.datetime.now()} - {status} - {event} - {data}\n"
    
    def save_to_file(self,row:str):
        """
        Save row to log_file
        """
        filename=f"{datetime.datetime.now().strftime('%Y-%m-%d')}.log"

        with open(self.log_dir+"/"+filename,"a") as f:
            f.write(row)
    