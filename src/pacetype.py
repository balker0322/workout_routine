from abc import ABC, abstractmethod


class PaceType(ABC):
    pass


class RepsPerSec(PaceType):
    
    def __init__(self, reps_per_sec:int):
        self.reps_per_sec = reps_per_sec