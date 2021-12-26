import mss
import pytesseract
import numpy as np
from main import RESOURCES_PATH

import cv2
from time import sleep
import time


class Monitor():

    def __init__(self) -> None:
        self.x = None
        self.y = None
        self.sct = mss.mss()
        self.monitor_number = 2 
        self.mon = self.sct.monitors[2]
        self.monitor = {
            'top': self.mon['top'] + 19,
            'left': self.mon['left'] + 996,
            'width': 270, 
            'height': 16,
            'mon': self.monitor_number
        }
        self.numbers = [
            cv2.imread(RESOURCES_PATH + 'number_0.jpg'),
            cv2.imread(RESOURCES_PATH + 'number_1.jpg'),
            cv2.imread(RESOURCES_PATH + 'number_2.jpg'),
            cv2.imread(RESOURCES_PATH + 'number_3.jpg'),
            cv2.imread(RESOURCES_PATH + 'number_4.jpg'),
            cv2.imread(RESOURCES_PATH + 'number_5.jpg'),
            cv2.imread(RESOURCES_PATH + 'number_6.jpg'),
            cv2.imread(RESOURCES_PATH + 'number_7.jpg'),
            cv2.imread(RESOURCES_PATH + 'number_8.jpg'),
            cv2.imread(RESOURCES_PATH + 'number_9.jpg'),
            cv2.imread(RESOURCES_PATH + 'dot.jpg'),
            cv2.imread(RESOURCES_PATH + 'bkt.jpg')
        ]

    def search_color(self, frame, lh, ls, lv, hh, hs, hv):
        lower_range = np.array([lh, ls, lv])
        upper_range = np.array([hh, hs, hv])

        mask = cv2.inRange(frame, lower_range, upper_range)

        return mask
            
    def grab_coord_tesseract(self):
        scene = np.array(self.sct.grab(self.monitor))
        hsv_scene = cv2.cvtColor(scene, cv2.COLOR_BGR2HSV)
                
        good = self.search_color(hsv_scene, 25, 10, 140, 51, 85, 255)
        goodColor = cv2.cvtColor(good, cv2.COLOR_BGR2RGB)

        coordData = pytesseract.image_to_string(goodColor, config='--psm 13 --oem 3 -c tessedit_char_whitelist=,0123456789')
        
        return coordData

    def grab_coord(self):
        raw_data = ''
        scene = np.array(self.sct.grab(self.monitor))
        scene = cv2.cvtColor(scene, cv2.COLOR_BGR2HSV)
        scene = self.search_color(scene, 25, 10, 140, 51, 85, 255)
        scene = cv2.cvtColor(scene, cv2.COLOR_BGR2RGB)
        scene = scene[:,:,:3]        
        y,x,h,w = 0,261,17,10
        crop_scene = scene[y:y+h, x:x+w]
        xyz_swap = 0

        for i in range(27):
            crop_scene = scene[y:y+h, x:x+w]
            max_threshold = 0
            good_number = ' '
            
            for j in range(len(self.numbers)):
                result = cv2.matchTemplate(crop_scene, self.numbers[j], cv2.TM_CCOEFF_NORMED)
                _, max_val, _, max_loc = cv2.minMaxLoc(result)

                if max_val > max_threshold:
                    max_threshold = max_val
                    good_number = j
                    if good_number == 11:
                        good_number = "["
            
            if good_number == 10: 
                good_number='.'
                xyz_swap +=1
                if xyz_swap % 2 == 0:
                    raw_data = raw_data[1:]
                    

            if good_number == '[' and xyz_swap == 5: break
            raw_data = str(good_number) + raw_data
            x-=9

            #if xyz_swap == 6: break
            # raw_data = raw_data.replace('one', '')

        raw_data = raw_data.split('.')
        try:
            return (float(raw_data[0]+'.'+raw_data[1]), float(raw_data[2]+'.'+raw_data[3]), time.time())
        except IndexError:
            return None
        except ValueError:
            cv2.imshow('Screen Shott', scene)
            cv2.waitKey()
            sleep(.10)
            return raw_data
            
        #cv2.imshow('Screen Shott', crop_scene)
        


#brightless: 6
#contrast: 9
#field of view