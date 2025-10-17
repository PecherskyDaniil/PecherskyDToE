from .abstract_dto import abstract_dto


class step_dto(abstract_dto):
    """
    Class for step dto
    """
    __step_description:str = ""

    @property
    def step_description(self) -> str:
        """
        Property step description
        """
        return self.__step_description   
    
    @step_description.setter
    def step_description(self, value):
        """
        Setter fo property step description
        """
        self.__step_description = value