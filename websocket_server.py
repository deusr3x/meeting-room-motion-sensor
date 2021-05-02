import asyncio
import websockets
from motion_sensor import MoSensor
import random


sensor = MoSensor()
sensor.start()
async def room_status(websocket, path):
#    sensor.start()
    while True:
        status = sensor.get_state()
        await websocket.send(status)
        await asyncio.sleep(random.random()*3)

start_server = websockets.serve(room_status, "0.0.0.0", 5000)

try:
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt:
    pass
finally:
    sensor.stop()
