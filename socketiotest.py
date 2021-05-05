import socketio

sio = socketio.Client()
sio.connect("http://0.0.0.0:8000") # change to server address
print('my sid is', sio.sid)

sio.emit('test', {'test': 'message'})
sio.disconnect()
