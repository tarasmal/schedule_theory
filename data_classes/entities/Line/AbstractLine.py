from abc import ABC, abstractmethod
from data_classes.entities.Circle import Circle


class AbstractLine(ABC):
    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def check_intersection_with_circle(self, circle: Circle, r: float) -> bool:
        pass
