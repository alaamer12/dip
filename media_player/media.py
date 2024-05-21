from abc import ABC, abstractmethod

class Media(ABC):
    @abstractmethod
    def play(self):
        pass
