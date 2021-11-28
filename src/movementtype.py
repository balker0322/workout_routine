from abc import ABC, abstractmethod
from .pacetype import PaceType



class MovementType(ABC):
    pass


class RepsWorkout(MovementType):

    def __init__(self,
        name:str,
        pace:PaceType,
        work_to_rest_ratio:float,
        relative_effort:float,
    ):
        self.name = name
        self.pace = pace
        self.work_to_rest_ratio = work_to_rest_ratio
        self.relative_effort = relative_effort