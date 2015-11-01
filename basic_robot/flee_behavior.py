__author__ = 'Jostein'
from .behavior import Behavior

class Flee_behavior(Behavior):

    def __init__(self):
        self.active_flag = False
        self.motor_recommendation = ('B')



