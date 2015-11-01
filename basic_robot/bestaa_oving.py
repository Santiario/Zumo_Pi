from sensors import *
from sensobs import *
from behaviors import *


def main():
    ultrasonic_sensor = Ultrasonic()
    #reflectance_sensor = ReflectanceSensors()
    #camera_sensor = Camera()

    ultrasonic_sensob = Sensob(ultrasonic_sensor)

    ultrasonic_behavior = SonicBehavior(ultrasonic_sensob)

    








if __name__ == '__main__':
    main()
