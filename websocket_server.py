import asyncio
import websockets
from motion_sensor import MoSensor
import random
import json

ROOM_NAME = 'JET'
sensor = MoSensor()
sensor.start()
status = 'no movement'
async def room_status(websocket, path):
#    sensor.start()
    status = 'no movement'
    while True:
        past_status = status
        status = sensor.get_history()
        if status != past_status:
            await websocket.send(json.dumps({'room': ROOM_NAME, 'status': status}))
        await asyncio.sleep(1)

start_server = websockets.serve(room_status, "0.0.0.0", 8080)

try:
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt:
    pass
finally:
    sensor.stop()
