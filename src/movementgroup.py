from abc import ABC, abstractmethod
from .movementtype import MovementType
from .durationtype import DurationType


class IMovementGroup(ABC):

    @abstractmethod
    def set_target(self, target:DurationType):
        '''set target'''

    @abstractmethod
    def add_movement(self, movement_type:MovementType):
        '''add movement'''

    @abstractmethod
    def get_all_movement_types(self) -> list[MovementType]:
        '''get all movement types'''


class MovementGroup:
    
    def __init__(self):
        self.movement_type_list = []

    def set_target(self, target:DurationType):
        self.target = target
 
    def add_movement(self, movement_type:MovementType):
        self.movement_type_list.append(movement_type)
    
    def get_all_movement_types(self) -> list[MovementType]:
        return self.movement_type_list

    