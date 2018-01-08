"""
The SmartCar API implementation
Each method receives an id as a parameter corresponding to the
Vehicle ID (eg: 1234, 1235 etc). Each method then calls post_request()
which is in GeneralMotors.py. The returned json from post_request()
is parsed and required components are inserted in a dictionary and returned.
"""

from webapp.utilities import GeneralMotors as gm

vehicle_info = "/getVehicleInfoService"
security = "/getSecurityStatusService"
energy_level = "/getEnergyService"
engine = "/actionEngineService"


def get_vehicle_info(id):
    info = {}
    vehicle_info_json = gm.post_request(vehicle_info, id, None, None)
    if vehicle_info_json['status'] != '200':
        return 'Status code other than 200 received!'
    data = vehicle_info_json['data']
    color = data['color']['value']
    info['color'] = color
    drive_train = data['driveTrain']['value']
    info['driveTrain'] = drive_train
    vin = data['vin']['value']
    info['vin'] = vin
    if data['fourDoorSedan']['value'] == 'True':
        door_count = 4
    elif data['twoDoorCoupe']['value'] == 'True':
        door_count = 2
    else:
        door_count = None
    info['doorCount'] = door_count
    return info


def get_security(id):
    info = []
    security_info_json = gm.post_request(security, id, None, None)
    if security_info_json['status'] != '200':
        return 'Status code other than 200 received!'
    doors = security_info_json['data']['doors']['values']
    for door in doors:
        if door['locked']['value'] == 'True':
            locked_door = {}
            location = door['location']['value']
            locked_door['location'] = location
            locked_door['locked'] = "true"
            info.append(locked_door)
    return info


def get_fuel(id):
    info = {}
    fuel_info_json = gm.post_request(energy_level, id, None, None)
    if fuel_info_json['status'] != '200':
        return 'Status code other than 200 received!'
    data = fuel_info_json['data']
    tank_level = data['tankLevel']['value']
    info['percent'] = tank_level
    return info


def get_battery(id):
    info = {}
    battery_info_json = gm.post_request(energy_level, id, None, None)
    if battery_info_json['status'] != '200':
        return 'Status code other than 200 received!'
    data = battery_info_json['data']
    battery_level = data['batteryLevel']['value']
    info['percent'] = battery_level
    return info


def get_engine(id, content_type, action):
    info = {}
    engine_info_json = gm.post_request(engine, id, content_type, action)
    if engine_info_json['status'] != '200':
        return 'Status code other than 200 received!'
    if engine_info_json == "Invalid input":
        print(engine_info_json)
        return
    status = engine_info_json['actionResult']['status']
    if status == "EXECUTED":
        info['status'] = "success"
    elif status == "FAILED":
        info['status'] = "error"
    return info
