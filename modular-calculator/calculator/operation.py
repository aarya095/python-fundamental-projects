from abc import ABC, abstractmethod

class Operation(ABC):
    """Abstract class"""
    @abstractmethod
    def execute(self):
        pass