from src.movementtype import RepsWorkout
from src.pacetype import RepsPerSec


exercise_1 = RepsWorkout(
    name = 'Exercise 1',
    pace = RepsPerSec(1),
    work_to_rest_ratio = 1.5/1.0,
    relative_effort = 1.0,
)

dips = RepsWorkout(
    name = 'Dips',
    pace = RepsPerSec(1),
    work_to_rest_ratio = 1.5/1.0,
    relative_effort = 1.0,
)

push_up = RepsWorkout(
    name = 'Push-up',
    pace = RepsPerSec(1),
    work_to_rest_ratio = 1.5/1.0,
    relative_effort = 1.0,
)

pull_up = RepsWorkout(
    name = 'Pull-up',
    pace = RepsPerSec(1),
    work_to_rest_ratio = 1.5/1.0,
    relative_effort = 1.0,
)