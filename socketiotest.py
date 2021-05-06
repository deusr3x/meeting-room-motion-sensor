import socketio
import time
import datetime

sio = socketio.Client()
sio.connect("http://0.0.0.0:8000") # change to server address
print('my sid is', sio.sid)
message = {'room': 'c_188c9bc7tbb1shu3ngtt936nq9dos4g8e9nmmt1ecdnmq@resource.calendar.google.com', 'status': 'open'}
#sio.emit('meeting_room_update', message)

try:
    while True:
        a = datetime.datetime.now()
        message = {'room': 'c_188c9bc7tbb1shu3ngtt936nq9dos4g8e9nmmt1ecdnmq@resource.calendar.google.com', 'status': f'{a}'}
        sio.emit('meeting_room_update', message)
        time.sleep(10)
except KeyboardInterrupt:
    pass
finally:
    sio.disconnect()
