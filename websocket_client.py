import socketio
from motion_sensor import MoSensor
import json
import time


ROOM_NAME = 'c_188c9bc7tbb1shu3ngtt936nq9dos4g8e9nmmt1ecdnmq@resource.calendar.google.com'
SERVER_ADDR = 'http://0.0.0.0:8000' # change to server address

sensor = MoSensor()
sensor.start()

sio = socketio.Client()
sio.connect(SERVER_ADDR)

def run_loop():
    status = 'unoccupied'
    while True:
        past_status = status
        status = sensor.get_history()
        if status != past_status:
            sio.emit('meeting_room_update', {'room': ROOM_NAME, 'status': status})
            print(status)
        time.sleep(1)

try:
    run_loop()
except KeyboardInterrupt:
    pass
finally:
    sensor.stop()
    sio.disconnect()
