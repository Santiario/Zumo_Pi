# import modules here

__author__ = 'estensen'


class BBCON:
    def __init__(self, behaviors, active_behaviors, sensobs, motobs, arbitrator):
        self.behaviors = behaviors  # A list of all the behavior objects used by the bbcon.
        self.active_behaviors = active_behaviors  # A list of all behaviors that are currently active.
        self.sensobs = sensobs  # A list of all sensory objects used by the bbcon.
        self.motobs = motobs  # A list of all motor objects used by the bbcon.
        self.arbitrator = arbitrator  # The arbitrator object that will resolve actuator requests produced by the behaviors.

    def add_behavior(self):
        """
        Append a newly-created behavior onto the behaviors list.
        """
        ...

    def add_sensob(self):
        """
        Append a newly-created sensob onto the sensobs list.
        """
        ...

    def activate_behavior(self):
        """
        Add an existing behavior onto the active-behaviors list.
        """
        ...

    def deactivate_behavior(self):
        """
        Remove an existing behavior from the active behaviors list.
        """
        ...

    def run_one_timestep(self):
        ...

