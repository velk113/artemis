from config import RESOURCES_PATH, MONITOR_NUMBER
import mss
import numpy as np
import cv2
import time
import autoit


class Monitor():

    sct = mss.mss()
    monitor_number = MONITOR_NUMBER 
    mon = sct.monitors[MONITOR_NUMBER]

    @classmethod  
    def grabPositionArea(cls):
        params = {
            'top': cls.mon['top'] + 19,
            'left': cls.mon['left'] + 1083,
            'width': 270, 
            'height': 16,
            'mon': cls.monitor_number
        }

        return Monitor.sct.grab(params)

    @classmethod
    def grabActionButtonArea(cls):
        params = {
            'top': cls.mon['top'] + 85,
            'left': cls.mon['left'] + 100,
            'width': 950, 
            'height': 500,
            'mon': cls.monitor_number
        }

        return Monitor.sct.grab(params)


class Camera():

    def __init__(self) -> None:
        #self.left_side = 1925
        #self.right_side = 3280
        self.left_side = Monitor.mon['left'] + 5
        self.right_side = Monitor.mon['left'] + 1360

    def rotate(self, speed=2, deg=360):
        loop = 0
        
        speed = int(speed / (deg / abs(deg)))
        deg = abs(deg)
        border = self.right_side if speed < 0 else self.left_side
        leaps = (20.80 / abs(speed)) * deg  #20.49
        big_leap = int(1000 / (speed / abs(speed)))

        while loop < leaps:
            coord = autoit.mouse_get_pos()

            if coord[0] == border:
                autoit.mouse_move(coord[0]+big_leap, coord[1], 0)
            else:
                autoit.mouse_move(coord[0]-speed, coord[1], 0)
                loop +=1


class Detector():

    def __init__(self):
        pass

    def detect_action_button(self):
        threshold = .70
        action_button_img = cv2.imread(RESOURCES_PATH + 'action_button.jpg')
        scene = np.array(Monitor.grabActionButtonArea())
        scene = scene[:,:,:3]

        result = cv2.matchTemplate(scene, action_button_img, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        
        if max_val >= threshold:
            return True
        else:
            return False

        

class CoordGrabber():

    def __init__(self):
        self.coord_map = [1,1,1,0,1,1,1,0,0,1,1,1,0,1,1,1,1,0,0,1,1,1,0,1,1,1,1]
        self.numbers = [
            cv2.imread(RESOURCES_PATH + 'position_img/number_0.jpg'),
            cv2.imread(RESOURCES_PATH + 'position_img/number_1.jpg'),
            cv2.imread(RESOURCES_PATH + 'position_img/number_2.jpg'),
            cv2.imread(RESOURCES_PATH + 'position_img/number_3.jpg'),
            cv2.imread(RESOURCES_PATH + 'position_img/number_4.jpg'),
            cv2.imread(RESOURCES_PATH + 'position_img/number_5.jpg'),
            cv2.imread(RESOURCES_PATH + 'position_img/number_6.jpg'),
            cv2.imread(RESOURCES_PATH + 'position_img/number_7.jpg'),
            cv2.imread(RESOURCES_PATH + 'position_img/number_8.jpg'),
            cv2.imread(RESOURCES_PATH + 'position_img/number_9.jpg'),
            #cv2.imread(RESOURCES_PATH + 'dot.jpg'),
            cv2.imread(RESOURCES_PATH + 'position_img/bkt.jpg')
        ]
        
    def set_coord_map(self, coord_map):
        self.coord_map = coord_map

    def unsharp_mask(self, image, kernel_size = (5, 5), sigma = 1.0, amount = 1.0,):
        image = np.array(image)
        blurred = cv2.GaussianBlur(image, kernel_size, sigma)
        sharpened = float(amount + 1) * image - float(amount) * blurred
        sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
        sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
        sharpened = sharpened.round().astype(np.uint8)
        return sharpened

    def grab_coord(self):
        raw_data = ''
        raw_scene = np.array(Monitor.grabPositionArea())
        scene = cv2.resize(raw_scene, (600,36), interpolation = cv2.INTER_NEAREST)
        
        scene = scene[:,:,:3]
        y,x,h,w = 2,579,33,20
        step = 20
        crop_digit = scene[y:y+h, x:x+w]
        xyz_swap = 0

        for digit_bias in self.coord_map:
            crop_digit = scene[y:y+h, x:x+w]

            crop_digit = self.unsharp_mask(crop_digit)
            max_threshold = 0
            result_digit = ' '
            
            if digit_bias != 0: 
                for j in range(len(self.numbers) -1):
                    result = cv2.matchTemplate(crop_digit, self.numbers[j], cv2.TM_CCOEFF_NORMED)
                    _, max_val, _, max_loc = cv2.minMaxLoc(result)   

                    if max_val > max_threshold:
                        max_threshold = max_val
                        result_digit = j
            else:
                result_digit = '.'    

            raw_data = str(result_digit) + raw_data
            x-=step

        raw_data = raw_data.split('..')   
           
        try:
            return (float(raw_data[0]), float(raw_data[1]), time.time())
        except IndexError:
            return None
        except ValueError:
            return raw_data