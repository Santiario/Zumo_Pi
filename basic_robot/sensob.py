# import modules here

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

    def update(self):
        """Update sensory object.
        Force sensob to fetch relevant sensor value(s).
        Convert to pre-processed sensob value.
        Done once each timestep.
        """
        self.value = self.sensor.update()
