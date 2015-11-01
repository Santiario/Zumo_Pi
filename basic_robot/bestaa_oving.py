from sensors import *
from sensobs import *
from behaviors import *
from arbitrator import Arbitrator
from motob import Motob
from BBCON import Bbcon


def main():

    ultrasonic_sensor = Ultrasonic()
    #reflectance_sensor = ReflectanceSensors()
    camera_sensor = Camera()
    print('Made sensors')

    ultrasonic_sensob = Sensob(ultrasonic_sensor)
    camera_sensob = CameraSensob(camera_sensor)
    print('Made sensobs')

    ultrasonic_behavior = SonicBehavior(ultrasonic_sensob)
    camera_behavior = CameraBehavior(camera_sensob)
    print('Made behaviors')

    arbitrator = Arbitrator()
    print('Made arbitrator')

    motob = Motob()
    print('Made motob')

    bbcon = Bbcon([ultrasonic_behavior, camera_behavior], [ultrasonic_sensob, camera_sensob], motob, arbitrator)
    print('Made BBCON')

    print('Running...')
    while True:
        bbcon.run_one_timestep()


if __name__ == '__main__':
    main()
