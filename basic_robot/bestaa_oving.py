from sensors import *
from sensobs import *
from behaviors import *
from arbitrator import Arbitrator
from motob import Motob
from BBCON import Bbcon


def main():

    ultrasonic_sensor = Ultrasonic()
    print('Made ultrasonic sensor')
    # reflectance_sensor = ReflectanceSensors()
    # camera_sensor = Camera()

    ultrasonic_sensob = Sensob(ultrasonic_sensor)
    print('Made ultrasonic sensob')

    ultrasonic_behavior = SonicBehavior(ultrasonic_sensob)
    print('Made ultrasonic behavior')

    arbitrator = Arbitrator()
    print('Made arbitrator')

    motob = Motob()
    print('Made motob')

    bbcon = Bbcon([ultrasonic_behavior], [ultrasonic_behavior], [ultrasonic_sensob], motob,arbitrator)

    print('Made motob')

    print('Running bbcon')
    bbcon.run_one_timestep()








if __name__ == '__main__':
    main()
