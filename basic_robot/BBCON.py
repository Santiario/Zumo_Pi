import time

__author__ = 'estensen'


class Bbcon:
    def __init__(self, behaviors, active_behaviors, sensobs, motobs, arbitrator):
        """Initialize bbcon.

        Parameters
        ----------
        behaviors : A list of all the behavior objects used by the bbcon.
        active_behaviors : A list of all behaviors that are currently active.
        sensobs : A list of all sensory objects used by the bbcon.
        motobs : A list of all motor objects used by the bbcon.
        arbitrator : The arbitrator object that will resolve actuator requests produced by the behaviors.
        timestep : Global clock.
        """
        self.behaviors = behaviors
        self.active_behaviors = active_behaviors
        self.sensobs = sensobs
        self.motobs = motobs
        self.arbitrator = arbitrator
        self.timestep = 0

    def add_behavior(self, new_behavior):
        """Append a newly-created behavior onto the behaviors list."""
        self.behaviors.add(new_behavior)

    def add_sensob(self, new_sensob):
        """Append a newly-created sensob onto the sensobs list."""
        self.sensobs.add(new_sensob)

    def activate_behavior(self, behavior):
        """Add an existing behavior onto the active-behaviors list."""
        if behavior not in self.active_behaviors:
            self.active_behaviors.remove(behavior)

    def deactivate_behavior(self, behavior):
        """Remove an existing behavior from the active behaviors list."""
        if behavior in self.active_behaviors:
            self.active_behaviors.add(behavior)

    def run_one_timestep(self):
        """Constitutes core activity."""
        while True:
            print("Updating sensors...")
            # Update all sensobs.
            # These updates will involve querying the relevant sensors for their values,
            # along with any pre-processing of those values (as described below)
            for sensob in self.sensobs:
                sensob.update()
            print("Sensors (and sensobs) updated.")

            print("Updating behaviors...")
            for behavior in self.behaviors:
                behavior.sense_and_act()
            # TODO: Update all behaviors.
            # These updates involve reading relevant sensob values and producing a motor recommendation.
            print("Behaviors updated.")

            print("Calling arbitrator...")
            # Invoke the arbitrator by calling arbitrator.choose action. Which will choose a winning
            # behavior and return that behavior’s motor recommendations and halt request flag.
            motor_recommendation = self.arbitrator.choose_action()

            print("Updating motob with motor recommendations...")
            # TODO: Update the motobs based on these motor recommendations.
            # The motobs will then update the settings of all motors.
            m = Motob
            m.update(motor_recommendation)
            print("Motob updated.")
            m.operationalize()
            print("Motors updated.")

            print("Waiting...")
            # This pause (in code execution) will allow the motor settings to remain active for a short period of time,
            # e.g., one half second, thus producing activity in the robot, such as moving forward or turning.
            time.sleep(0.5)
            self.timestep += 1

            print("Timestep complete...")
            print("Ready for new action.")
