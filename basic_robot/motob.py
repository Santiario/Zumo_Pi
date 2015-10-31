# import modules here
from .motors import Motors

__author__ = 'estensen'


class Motob:
    """Interface between a behavior and one or more motors."""
    # TODO: Rewrite class to use actions instead of motors?
    # F --> Forward
    # L --> Left
    # int --> duration
    def __init__(self):
        """Initialize Motob object.

        Parameters
        ----------
        motors : A list of the motors whose settings will be determined by the motob.
        value : A holder of the most recent motor recommendation sent to the motob.
        """
        self.m = Motors()
        self.motors = []  # MR only one motor at a time?
        self.value = None

    def update(self, recommendation):
        """Update object.

        Receive a new motor recommendation.
        Load it into a value slot.
        Operationalize it.

        Example
        -------
        recommendation = ('L', 45)
        """
        self.motors[0]
        self.value = recommendation[1]
        self.operationalize()

    def operationalize(self):
        """Convert motor recommendation into motor setting and send to corresponding motor(s).

        Parameters
        ----------
        val : Vector that sets speed and direction of the left and right motors.
        dur : Duration of the operation.

        Example
        -------
        val = [1, 1]  Full speed forward
        val = [-1, -1] Full speed backward
        val = [0.5, 0] Turn right on the spot
        val = 0.5, 0.2] Turn right while driving forward
        """
        if self.value == 0:
            m.stop()
        else:
            val = []
            duration =
            m.set_value(val, dur=duration)  # The duration of the turning has to be tuned

        # Val should be a 2-element vector with values for the left and right motor speeds, both in the range [-1, 1].
