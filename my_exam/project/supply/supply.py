from abc import ABC, abstractmethod


class Supply(ABC):
    @abstractmethod
    def __init__(self, needs_increase):
        self._needs_increase = needs_increase

    @property
    def needs_increase(self):
        return self._needs_increase

    @needs_increase.setter
    def needs_increase(self, value):
        if value < 0:
            raise ValueError("Needs increase cannot be less than zero.")
        self._needs_increase = value

    def apply(self, survivor):
        survivor.needs += self._needs_increase