# import modules here

__author__ = 'estensen'


class Behavior:
    """Behaviors the robot can do."""
    def __init__(self):
        """Initialize behavior.

        Parameters
        ----------
        bbcon : Pointer to the controller that this behavior uses.
        sensobs : List of the sensobs this behavior uses.
        motor_recommendations : List of recommendations, one per motob, that this behavior provides to the arbitrator.
            Assume that all motobs are used by all behaviors.
        active_flag : Boolean indicating if behavior is active or inactive.
        halt_request : Some behaviors can request the robot to halt all activity.
        priority : Static predefined value indicating the importance of this behavior.
        match_degree : Real number in the range [0, 1] indicating the degree to which the current conditions warrant the
            performance of this behavior.
        weight : The product of the priority and match_degree, which the arbitrator uses as the basis for selecting the
            winning timestep.
        """
        self.bbcon = bbcon()
        self.sensobs = []