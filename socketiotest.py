import socketio
import time
import datetime

sio = socketio.Client()
sio.connect("http://0.0.0.0:8000") # change to server address
print('my sid is', sio.sid)
message = {'room': '', 'status': 'open'}
#sio.emit('meeting_room_update', message)

try:
    while True:
        a = datetime.datetime.now()
        message = {'room': '', 'status': f'{a}'}
        sio.emit('meeting_room_update', message)
        time.sleep(10)
except KeyboardInterrupt:
    pass
finally:
    sio.disconnect()
