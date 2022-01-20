from pynput import keyboard
import time
import threading

class Manager():
    
    state = False

    def _on_press(self, key):
        if key == keyboard.Key.f9:
            if Manager.state == False:
                print("PLAY")
                Manager.state = True
            elif Manager.state == True:
                print("STOP")
                Manager.state = False 

    def start_keyboard_listener(self):
        listener = keyboard.Listener(on_press=self._on_press)
        listener.start()



