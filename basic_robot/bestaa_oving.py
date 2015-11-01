from sensors import *
from sensobs import *
from behaviors import *
from arbitrator import Arbitrator
from motob import Motob
from BBCON import Bbcon


def main():
    ultrasonic_sensor = Ultrasonic()
    # reflectance_sensor = ReflectanceSensors()
    # camera_sensor = Camera()

    ultrasonic_sensob = Sensob(ultrasonic_sensor)

    ultrasonic_behavior = SonicBehavior(ultrasonic_sensob)

    arbitrator = Arbitrator()

    motob = Motob()

    bbcon = Bbcon([ultrasonic_behavior], [ultrasonic_behavior], [ultrasonic_sensob], motob,arbitrator)

    bbcon.run_one_timestep()








if __name__ == '__main__':
    main()
