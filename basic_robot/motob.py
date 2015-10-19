# import modules here

__author__ = 'estensen'


class Motob:
    """Interface between a behavior and one or more motors."""
    def __init__(self, motors, value):
        """Initialize Motob object.

        Parameters
        ----------
        motors : A list of the motors whose settings will be determined by the motob.
        value : A holder of the most recent motor recommendation sent to the motob.
        """
        self.motors = motors
        self.value = value

    def update(self):
        """Update object.

        Receive a new motor recommendation.
        Load it into a value slot.
        Operationalize it.
        """
        motor_recommendation = (self.motors, self.value)
        self.operationalize(motor_recommendation)

    def operationalize(self, motor_recommendation):
        """Convert motor recommendation into motor setting and send to corresponding motor(s)."""
        # Motors.set_value()