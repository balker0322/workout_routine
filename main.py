from src.durationtype import Repetition
from src.workouttype import RoundTypeWorkout
from src.workout import Workout
from src.movementgroup import MovementGroup
from src.movementlists import *


def main():

    push = MovementGroup()
    push.set_target(Repetition(200.0))
    push.add_movement(push_up)
    push.add_movement(dips)
    
    pull = MovementGroup()
    pull.set_target(Repetition(150.0))
    pull.add_movement(pull_up)

    workout = Workout(
        workout_type = RoundTypeWorkout(number_of_rounds = 8),
        workout_groups=[push, pull],
    )
    workout.generate_workout()

def try_func():
    '''
    Input data: list of movement object
    Each object has a total target
    Function should set the ff.:
        - rounds (12 / sets)
        - sets (1,2,3,4,6)
        - routine (1 to len(movement))

    divide 
    '''
    pass

if __name__=="__main__":
    main()
    # try_func()