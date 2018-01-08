# SmartCar-API
Restful API for SmartCar which makes HTTP requests to the GM API and returns the information into a cleaner format.

## Initial Setup
* Make sure you have python 3 or a higher version installed.
* Now we install pip as it makes it easier to download the latest version of Django globally. Execute the following command.
```
$ sudo apt-get install python3-pip
```
* Now we install Django using pip3. To do this execute the following command execute the following command.
```
$ sudo pip3 install django 
```
* We also need to install django rest framework. To do this execute the following command.
```
$ sudo pip3 install djangorestframework
```
* Last step in the setup is cloning this repository.
```
$ git clone <remote-url>
$ cd SmartCar-API
```

## Running the server
* We need to go in the smartcar directory and run the manage.py file. 
* Make migrations before running the server.
```
$ cd smartcar/
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```
* Your server must now be up and running without any errors.

## Calling the SmartCar API
If all the previous steps have been completed successfully your server must be up and running. Now we need to make requests to the SmartCar API and check the responses. <br /> <br />
Open any internet browser and type in the following URL.
```
http://127.0.0.1:8000
```
If you see the word **Localhost** in the browser you have the server up and running.

## Making requests to the API
Now you can make the following requests to the API and check the responses.
```
$ curl http://127.0.0.1:8000/vehicles/1234
$ curl http://127.0.0.1:8000/vehicles/1234/doors
$ curl http://127.0.0.1:8000/vehicles/1234/fuel
$ curl http://127.0.0.1:8000/vehicles/1234/battery
```
You could also run these URLs in the browser and see the responses. <br /> <br />
For the post request you could type in the command
```
$ curl http://127.0.0.1:8000/vehicles/1ntent-Type: application/json' -d '{"action": "START|STOP"}'
```
