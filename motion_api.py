import json
from flask import Flask, request, jsonify
from motion_sensor import MoSensor
import time

app = Flask(__name__)

sensor = MoSensor()

@app.route('/', methods=['GET'])
def query_room():
    name = request.args.get('name')
    print(name)
    return jsonify({'motion':sensor.get_state()})

if __name__ == '__main__':
    sensor.start()
    app.run(host='0.0.0.0', debug=True)
    sensor.stop()

