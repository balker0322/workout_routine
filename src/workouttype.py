from abc import ABC, abstractmethod
from .movementtype import MovementType


class WortoutType(ABC):

    @abstractmethod
    def process_workout(self, movement_type_list:list[MovementType]) -> None:
        '''process workout'''


class RoundTypeWorkout(WortoutType):
    
    def __init__(self, number_of_rounds:int):
        self.number_of_rounds = number_of_rounds

    def process_workout(self, movement_type_list:list[MovementType]):
        print('TODO: process_workout method of RoundTypeWorkout class on workouttype.py')

        for movement in movement_type_list:
            print(f"TEST: {movement.name} {movement.work_to_rest_ratio} {movement.relative_effort}")

        movement_type_count = len(movement_type_list)
        number_of_sets = 3
        number_of_rounds_per_set = 2
        number_of_movement_per_round = round(float(movement_type_count)*0.5)


class RunningInterval(WortoutType):
    pass


