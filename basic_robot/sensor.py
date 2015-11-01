from abc import abstractmethod


class Sensor:

    @abstractmethod
    def update(self):
        pass
