from abc import ABC, abstractmethod


class Medicine(ABC):
    @abstractmethod
    def __init__(self, health_increase):
        self._health_increase = health_increase

    @property
    def health_increase(self):
        return self._health_increase

    @health_increase.setter
    def health_increase(self, value):
        if value < 0:
            raise ValueError("Health increase cannot be less than zero.")

    def apply(self, survivor):
        survivor.health += self._health_increase