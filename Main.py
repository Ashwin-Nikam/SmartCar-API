import SmartCar as sc


# POST /vehicles/1234/engine Content-Type: application/json { "action": "START" }

request_url = input()
sc.api_call(request_url)
