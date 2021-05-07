import socketio
from motion_sensor import MoSensor
import json
import time


ROOM_NAME = ''
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
    sensor.stop()
except Exception:
    try:
        sio.connect()
    except:
        pass
finally:
    sio.disconnect()
