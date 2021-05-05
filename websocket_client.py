import socketio
from motion_sensor import MoSensor
import json
import time


ROOM_NAME = 'JET'
SERVER_ADDR = 'http://0.0.0.0:8000' # change to server address

sensor = MoSensor()
sensor.start()

sio = socketio.Client()
sio.connect(SERVER_ADDR)

def run_loop():
    status = 'no movement'
    while True:
        past_status = status
        status = sensor.get_history()
        if status != past_status:
            sio.emit('test', {'room': ROOM_NAME, 'status': status})
        time.sleep(1)

try:
    run_loop()
except KeyboardInterrupt:
    pass
finally:
    sensor.stop()
    sio.disconnect()
