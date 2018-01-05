import GeneralMotors as gm

BASE_URL = 'http://gmapi.azurewebsites.net'
vehicle_info = "/getVehicleInfoService"
security = "/getSecurityStatusService"
energy_level = "/getEnergyService"
engine = "/actionEngineService"


def parse_vehicle_info():
    info = {}
    vehicle_info_json = gm.post_request(vehicle_info)
    data = vehicle_info_json['data']
    color = data['color']['value']
    info["color"] = color
    drive_train = data['driveTrain']['value']
    info["driveTrain"] = drive_train
    vin = data['vin']['value']
    info["vin"] = vin
    if data['fourDoorSedan']['value'] == 'True':
        door_count = 4
    elif data['twoDoorCoupe']['value'] == 'True':
        door_count = 2
    else:
        door_count = None
    info["doorCount"] = door_count
    return info


def parse_security_info():
    info = []
    security_info_json = gm.post_request(security)
    doors = security_info_json['data']['doors']['values']
    for door in doors:
        if door['locked']['value'] == 'True':
            locked_door = {}
            location = door['location']['value']
            locked_door["location"] = location
            locked_door["locked"] = "true"
            info.append(locked_door)
    return info


def parse_fuel_info():
    info = {}
    fuel_info_json = gm.post_request(energy_level)
    data = fuel_info_json['data']
    tank_level = data['tankLevel']['value']
    info['percent'] = tank_level
    return info


def parse_battery_info():
    info = {}
    battery_info_json = gm.post_request(energy_level)
    data = battery_info_json['data']
    battery_level = data['batteryLevel']['value']
    info['percent'] = battery_level
    return info


def start_stop_engine():
    info = {}
    engine_info_json = gm.post_request(engine)
    if engine_info_json == "Invalid input":
        print(engine_info_json)
        return
    status = engine_info_json['actionResult']['status']
    if status == "EXECUTED":
        info['status'] = "success"
    elif status == "FAILED":
        info['status'] = "error"
    return info





def api_call(request_url):
    request = request_url.split()
    if request[0] == "GET":
        print("GET URL")
    elif request[0] == "POST":
        print("POST URL")
    else:
        print("Invalid API call")


# print(parse_vehicle_info())
# print(parse_security_info())
# print(parse_fuel_info())
# print(parse_battery_info())
# print(start_stop_engine())