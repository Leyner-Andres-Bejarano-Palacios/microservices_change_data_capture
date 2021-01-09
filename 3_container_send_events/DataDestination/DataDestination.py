from abc import ABC, abstractmethod

class DataDestination(ABC):

    @abstractmethod
    def send(self, records):
    """Return none"""