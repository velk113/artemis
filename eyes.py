import mss
import cv2
import numpy
from time import sleep


class Eyes():

    def __init__(self) -> None:
        self.x = None
        self.y = None
        self.sct = mss.mss()
        self.monitor_number = 2 
        self.mon = self.sct.monitors[2]
        self.monitor = {
            'top': self.mon['top'] + 0,
            'left': self.mon['left'] + 0,
            'width': 1080,
            'height': 400,
            'mon': self.monitor_number
        }

    def shot(self):
        scene = numpy.array(self.sct.grab(self.monitor))
        scene = scene[:,:,:3]

        cv2.imshow('Screen Shot', scene)
        cv2.waitKey()
        sleep(.10)