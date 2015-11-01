# import modules here
from operator import attrgetter

__author__ = 'estensen'


class Arbitrator:
    def __init__(self, bbcon):
        self.bbcon = bbcon

    def choose_action(self):
        """Choose winning behavior.

        Returns
        -------
        motor_recommendation : On the format (action, duration).
        """
        winning_behavior = max(self.bbcon.active_behaviors, key=attrgetter('weight'))
        print("Winning behavior is " + str(winning_behavior))
        return winning_behavior.motor_recommendation
