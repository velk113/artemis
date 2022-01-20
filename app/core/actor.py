from .whip import Manager
from .monitor import CoordGrabber, Camera, Detector, Monitor
from utils import calculateDistance
import numpy as np
import math
import autoit
import time
import asyncio


def check_state(func):
    def wrapper(*args, **kwargs):
        if Manager.state == False:
            while True:
                if Manager.state == True:
                    return func(*args, **kwargs)
                time.sleep(0.5)
        else:
            return func(*args, **kwargs)
    return wrapper


class Actor():
    
    def __init__(self) -> None:
        self.position = Position()
        self.camera = Camera()
        self.detector = Detector()

    async def check_coord(self, x, y):
        distance = 1000
        autoit.send('{=}')
        while True:
            self.position.update_position()
            distance = calculateDistance(x1=self.position.x, y1=self.position.y, x2=x, y2=y)
            if distance < 2:
                autoit.send('{=}') 
                return
            await asyncio.sleep(0.2)

    async def rotate(self, x, y):
        while True:
            degree = self.position.get_target_orientation(np.array([x, y]))
            diff_angle = self.position.diff_angle(degree)
            self.camera.rotate(speed=2, deg=diff_angle)
            await asyncio.sleep(0.8)

    async def _goto(self, x, y):
        task1 = asyncio.create_task(self.check_coord(x,y))
        task2 = asyncio.create_task(self.rotate(x,y))

        await task1

    @check_state
    def goto(self, x, y):
        asyncio.run(self._goto(x,y))
        time.sleep(0.3)

    @check_state
    def mine(self, duration=5):
        time.sleep(1)
        if self.detector.detect_action_button():
            autoit.send('{e}')
            print("Добываю...")
            time.sleep(duration)
            return True
        return False

    @check_state
    def drop_to_storage(self):
        autoit.send('{e}') 

        time.sleep(1)
        autoit.mouse_move(Monitor.mon['left'] + 5, 0)
        
        for i in range(136):
            coord = autoit.mouse_get_pos()
            autoit.mouse_move(coord[0]+3, coord[1]+1, 0)
            time.sleep(0.01)

        for i in range(88):
            coord = autoit.mouse_get_pos()
            autoit.mouse_move(coord[0]+3, coord[1], 0)
            time.sleep(0.01)
    
        for i in range(8):
            autoit.mouse_click(button="left")
            time.sleep(0.3)

        for i in range(68):
            coord = autoit.mouse_get_pos()
            autoit.mouse_move(coord[0]+3, coord[1], 0)
            time.sleep(0.01)

        for i in range(14):
            autoit.mouse_click(button="left")
            time.sleep(0.3)

        autoit.send('{TAB}')


class Position():

    def __init__(self):
        self.monitor = CoordGrabber()
        self.x = None
        self.y = None
        self.prev_x = None
        self.prev_y = None
        self.update_position()

    def update_position(self):
        new_x, new_y, time = self.monitor.grab_coord()

        if self.x != new_x or self.y != new_y:
            self.prev_x, self.prev_y = self.x, self.y
    
        self.x, self.y = new_x, new_y
    
    def diff_angle(self, new_angle) -> float:
        angle = new_angle - self.get_self_orientation()
        return angle

    def get_target_orientation(self, target) -> float:
        x, y = target - np.array([self.x, self.y])
        return round(math.degrees(math.atan2(y, x)), 10) % 360.0

    def get_self_orientation(self) -> float:
        x, y = np.array([self.x, self.y]) - np.array([self.prev_x, self.prev_y])
        return round(math.degrees(math.atan2(y, x)), 10) % 360.0

    def position_valide(self, x, y):
        if self.prev_y != None:
            if calculateDistance(x, y, self.x, self.y) > 300:
                print("Не удалось распознать координаты.")
                return False
        return True
        