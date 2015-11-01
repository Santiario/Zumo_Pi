__author__ = 'estensen'


class Arbitrator:
    def __init__(self):
        pass

    def choose_action(self, active_behaviors):
        for behavior in active_behaviors:
            print(behavior)
        """Choose winning behavior.

        Returns
        -------
        motor_recommendation : On the format (action, duration).
        """
        winning_behavior = active_behaviors[0]
        for behavior in active_behaviors:
            if behavior.weight > winning_behavior.weight:
                winning_behavior = behavior
        print("Winning behavior is " + str(winning_behavior.motor_recommendation))
        return winning_behavior.motor_recommendation
