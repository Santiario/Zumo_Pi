# import modules here

__author__ = 'estensen'


class BBCON:
    def __init__(self, behaviors, active_behaviors, sensobs, motobs, arbitrator):
        """Initialize BBCON.

        Parameters
        ----------
        behaviors : A list of all the behavior objects used by the bbcon.
        active_behaviors : A list of all behaviors that are currently active.
        sensobs : A list of all sensory objects used by the bbcon.
        motobs : A list of all motor objects used by the bbcon.
        arbitrator : The arbitrator object that will resolve actuator requests produced by the behaviors.
        """
        self.behaviors = behaviors
        self.active_behaviors = active_behaviors
        self.sensobs = sensobs
        self.motobs = motobs
        self.arbitrator = arbitrator

    def add_behavior(self, new_behavior):
        """Append a newly-created behavior onto the behaviors list."""
        self.behaviors.add(new_behavior)

    def add_sensob(self, new_sensob):
        """Append a newly-created sensob onto the sensobs list."""
        self.sensobs.add(new_sensob)

    def activate_behavior(self, behavior):
        """Add an existing behavior onto the active-behaviors list."""
        self.active_behaviors.remove(behavior)

    def deactivate_behavior(self, behavior):
        """Remove an existing behavior from the active behaviors list."""
        self.active_behaviors.add(behavior)

    def run_one_timestep(self):
        # TODO: Update all sensobs.
        # These updates will involve querying the relevant sensors for their values,
        # along with any pre-processing of those values (as described below)
        # TODO: Update all behaviors.
        # These updates involve reading relevant sensob values and producing a motor recommendation.
        # TODO: Invoke the arbitrator by calling arbitrator.choose action.
        # which will choose a winning behavior and return that behavior’s motor recommendations and halt request flag.
        # TODO: 4. Update the motobs based on these motor recommendations.
        # The motobs will then update the settings of all motors.
        # TODO: 5. Wait.
        # This pause (in code execution) will allow the motor settings to remain active for a short period of time,
        # e.g., one half second, thus producing activity in the robot, such as moving forward or turning.
        # TODO: Reset the sensobs
        # Each sensob may need to reset itself, or its associated sensor(s), in some way.
        ...
