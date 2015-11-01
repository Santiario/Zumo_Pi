from .bbcon import Bbcon
from abc import abstractmethod

__author__ = 'estensen'


class Behavior:
    """Behaviors the robot can do."""
    def __init__(self):
        """Initialize behavior.

        Parameters
        ----------
        bbcon : Pointer to the controller that this behavior uses.
        sensobs : List of the sensobs this behavior uses.
        motor_recommendations : Motor recommendation for this behavior. Provides this to the arbitrator.
            Assume that all motobs are used by all behaviors.
        halt_request : Boolean indicating if the behavior will request the robot to halt all activity.
        priority : Static predefined value indicating the importance of this behavior.
        match_degree : Real number in the range [0, 1] indicating the degree to which the current conditions warrant the
            performance of this behavior.
        weight : The product of the priority and match_degree, which the arbitrator uses as the basis for selecting the
            winning timestep.
        """
        self.bbcon = Bbcon()
        self.sensobs = []
        self.motor_recommendations = None
        self.halt_request = False
        self.priority = 0
        self.match_degree = 0
        self.weight = 0

    def get_weight(self):
        return self.priority * self.match_degree

    @abstractmethod
    def set_match_degree(self):
        """Generate match according to environment."""

    @abstractmethod
    def set_motor_recommendations(self):
        """Generate motor recommendation for this behavior."""

    def update(self):
        """Interface between bbcon and behavior."""
        print("Updating behavior.")
        self.sense_and_act()
        self.weight = self.get_weight()

    def sense_and_act(self):
        """Computes behavior and sensob readings to produce motor recommendations and halt requests."""
        self.match_degree = self.set_match_degree()
        self.motor_recommendations = self.set_motor_recommendations()
