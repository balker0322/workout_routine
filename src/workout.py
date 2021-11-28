from abc import ABC, abstractmethod
from .workouttype import WortoutType
from .movementgroup import IMovementGroup
from .movementtype import MovementType


class IWorkout(ABC):
    
    @abstractmethod
    def generate_workout():
        '''display workout'''


class WorkoutBroadcaster(IWorkout):

    listeners = []

    def _broadcast_workout(self):
        print('TODO: _broadcast_workout method of WorkoutBroadcaster class on workout.py')

    def add_listener(self, listener):
        self.listeners.append(listener)


class Workout(WorkoutBroadcaster):
    
    def __init__(self,
        workout_type:WortoutType,
        workout_groups:list[IMovementGroup],
    ):
        self.workout_type = workout_type
        self.workout_groups = workout_groups
    
    def generate_workout(self):

        movement_type_list = self._get_all_movement_type_list()
        self.workout_type.process_workout(movement_type_list)
        self._broadcast_workout()
    
    def _get_all_movement_type_list(self) -> list[MovementType]:

        movement_type_list = []

        for workout_group in self.workout_groups:
            movement_type_list += workout_group.get_all_movement_types()
        
        return movement_type_list
