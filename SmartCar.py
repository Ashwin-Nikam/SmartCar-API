import GeneralMotors as gm

BASE_URL = 'http://gmapi.azurewebsites.net'
vehicle_info = "/getVehicleInfoService"
security = "/getSecurityStatusService"
energy_level = "/getEnergyService"
engine = "/actionEngineService"


def parse_vehicle_info():
    info = {}
    vehicle_info_json = gm.gm_api_post(vehicle_info)
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
