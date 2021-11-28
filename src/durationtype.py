from abc import ABC, abstractmethod

class DurationType(ABC):
    pass


class DistanceKm(DurationType):
    pass


class TimeSec(DurationType):
    pass


class Repetition(DurationType):
    
    def __init__(self, repetition:float):
        self.repetition = repetition
