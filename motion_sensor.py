import RPi.GPIO as GPIO
import time
import threading
from collections import deque


class MoSensor(object):
    GPIO.setmode(GPIO.BOARD)
    def __init__(self):
        self.pir_sensor = 11
        self.current_state = 0
        self._running = False
        self._stop = threading.Event()
        GPIO.setup(self.pir_sensor, GPIO.IN)
        self.history = deque(maxlen=60)

    def start(self):
        print("Starting sensor")
        self._running = True
        if not self._stop.is_set():
            self.start_loop()

    def stop(self):
        self._running = False
        self._stop.set()

    def start_loop(self):
        self._stop.clear()
        t = threading.Thread(name="monitorloop", target=self.monitor)
        t.daemon = False
        t.start()

    def monitor(self):
        while self._running:
            time.sleep(1)
            self.current_state = GPIO.input(self.pir_sensor)
            self.history.append(self.current_state)
            if self._stop.is_set():
                print("stopping")
                break

    def get_state(self):
        if self.current_state == 1:
            return "movement detected"
        else:
            return "no movement"

    def get_history(self):
        if sum(self.history) == 0:
            return "no movement"
        else:
            return "movement detected"
