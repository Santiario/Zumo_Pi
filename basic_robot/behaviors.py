from abc import abstractmethod


class Behavior:
    """Behaviors the robot can do."""
    def __init__(self, sensob, priority=0.5, ):
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
        weight : The product of the priority and match_degree, which the arbitrator uses as the basis for selecting
        the winning timestep.
        """
        self.sensob = sensob
        self.motor_recommendation = ('F', 2)
        self.priority = priority
        self.match_degree = 0
        self.weight = 0
        self.update()

    def get_weight(self):
        print('Priority:', self.priority, 'Match degree:', self.match_degree)
        return self.priority * self.match_degree

    @abstractmethod
    def set_match_degree(self):
        """Generate match according to environment."""

    @abstractmethod
    def set_motor_recommendation(self):
        """Generate motor recommendation for this behavior."""

    def update(self):
        """Interface between bbcon and behavior."""
        print("Updating behavior.")
        self.sense_and_act()
        self.weight = self.get_weight()

    def sense_and_act(self):
        """Computes behavior and sensob readings to produce motor recommendations and halt requests."""
        self.set_match_degree()
        self.motor_recommendation = self.set_motor_recommendation()


class SonicBehavior(Behavior):
    def set_match_degree(self):
        """Generate match according to environment."""
        if self.sensob.value < 5:
            self.match_degree = 1.0
        elif self.sensob.value < 10:
            self.match_degree = 0.9
        else:
            self.match_degree = 0.6


    def set_motor_recommendation(self):
        """Generate motor recommendation for this behavior."""
        if self.sensob.value < 20:
            self.motor_recommendation = ('T', 1)  # TODO: Change the number to match a 180 degree turn
        else:
            self.motor_recommendation = ('F', 2)  # Drive forward for two more seconds


class CameraBehavior(Behavior):

    def set_match_degree(self):
        """Generate match according to environment."""
        if self.sensob.value == 1.0:
            self.match_degree = 1.0
        else:
            self.match_degree = 0.0

    def set_motor_recommendation(self):
        """Generate motor recommendation for this behavior."""
        if self.sensob.value == 1.0:
            self.motor_recommendation = ('B', 7)  # Drives backwards for 7 seconds
        else:
            self.motor_recommendation = ('F', 2)  # Continue forward for 2 seconds



