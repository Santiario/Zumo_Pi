from abc import abstractmethod
from imager2 import Imager

__author__ = 'estensen'


class Sensob:
    """Interface between sensors and bbcon"""
    def __init__(self, sensor):
        """Initialize Sensob object.

        Parameters
        ----------
        sensor : Name of the sensor.
        value : Sensor value.
        """
        self.sensor = sensor
        self.update()  # Gets initial value of sensor

    @abstractmethod
    def update(self):
        """Update sensory object.
        Force sensob to fetch relevant sensor value(s).
        Convert to pre-processed sensob value.
        Done once each timestep.
        """
        self.value = self.sensor.update()


class CameraSensob(Sensob):
    def __init__(self, sensor, color_treshold=1700):
        """Initialize bbcon.

        Parameters
        ----------
        sensors: sensor used. Here it's a camera
        color: which color to look for. 0 = red, 1 = green, 2 = blue
        color_treshhold: amount of a colour needed in order to register as that color.
        """
        self.color = 0
        self.sensor = sensor
        self.value = self.sensor.update()
        self.color_treshold = color_treshold

    def update(self):
        """Check if you see red
        Takes a picture, runs wta(winner takes all) on it, then counts the number of red pixels
        If there's enough red, motor"""
        self.sensor.update()
        taken_image = self.sensor.get_value()

        wta_image = Imager(image=taken_image).map_color_wta(thresh=0.5)  # colors each pixel the dominant color
        red_count = 0
        for i in range(20, 100):
            for j in range(20, 80):
                if wta_image.get_pixel(i, j)[0] > 100:
                    red_count += 1
        print('Red count is:', red_count)
        if red_count > self.color_treshold:
            self.value = 1.0
        else:
            self.value = 0.0


class ReflectanceSensob(Sensob):
    def __init__(self, sensor):
        """
        Parameters
        ----------
        sensor: senso used, here IR
        value: priority of this one
        """
        self.sensor = sensor
        self.value = self.sensor.update()

    def update(self):
        sensors = self.sensor.get_value()
        avg = sum(sensors) / 6
        self.value = avg
