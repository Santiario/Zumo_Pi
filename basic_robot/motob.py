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
        action : Holder of the action whose settings will be determined by the motob.
        duration : Holder of the most recent duration the of the action.
        """
        self.m = Motors()
        self.action = None
        self.duration = None

    def update(self, recommendation):
        """Update object.

        Receive a new motor recommendation.
        Load it into the .
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
        if self.action == 'F':
            self.m.set_value(duration)
        elif self.action == 'T':
            self.m.set_value((1, -1), 1)
        elif self.action == 'L':
            self.m.left(dur=duration)
        elif self.action == 'R':
            self.m.right(dur=duration)
        elif self.action == 'S':
            self.m.stop()
        elif self.action == 'B':
            self.m.backward(dur=duration)
