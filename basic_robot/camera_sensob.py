__author__ = 'Jostein'

from .sensob import Sensob
from .camera import Camera
from .imager2 import Imager
import PIL

class Camera_sensob(Sensob):


    def __init__(self):
        """Initialize bbcon.

        Parameters
        ----------
        sensobs: sensors used. Here only camera shoult be added
        active_flag: whether to use this behavior or not
        priority: how important this behavior is (very important)
        color: which color to look for. 0 = red, 1 = green, 2 = blue
        color_treshhold: amount of a colour needed in order to register as that color.
        """
        super.__init__(self)
        self.sensor = Camera()
        self.value = 0

    def update(self):
        """Check if you see red
        Takes a picture, runs wta(winner takes all) on it, then counts the number of red pixels
        If there's enough red, motor"""
        self.sensor.update()
        taken_image = self.sensor.get_value()
        wta_image = Imager(image=taken_image).map_color_wta() #colors each pixel the dominant color
        red_count = 0
        for i in range(20, 100):
            for j in range(20, 80):
                if(wta_image.get_pixel(0,0)[0] > 100):
                    red_count += 1
        if(red_count > self.color_treshhold):
            self.value = 100
        else:
            self.value = 0








