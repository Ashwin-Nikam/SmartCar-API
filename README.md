# SmartCar-API
Restful API for SmartCar which makes HTTP requests to the GM(General Motors) API and returns the information in a cleaner format.

## Initial Setup
* Make sure you have python3 installed.
* Now we install pip as it makes it easier to download the latest version of Django globally. Execute the following command.
```
$ sudo apt-get install python3-pip
```
* Now we install Django using pip3. To do this execute the following command.
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
Now you can make the following requests to the API and check the responses. Execute the following commands in the terminal.
```
$ curl http://127.0.0.1:8000/vehicles/1234
$ curl http://127.0.0.1:8000/vehicles/1234/doors
$ curl http://127.0.0.1:8000/vehicles/1234/fuel
$ curl http://127.0.0.1:8000/vehicles/1234/battery
```
You could also run these URLs in the browser and see the responses. <br /> <br />
For the post request you could type in the following command in the terminal.
```
$ curl http://127.0.0.1:8000/vehicles/1234/engine -H 'Content-Type: application/json' -d '{"action": "START|STOP"}'
```

## Implementation Details
Following are some files and modules which form the core base of this Restful API implementation. <br />
* <b>utilities</b> - This folder is inside the smartcar/webapp directory. It contains two main utility files namely _GeneralMotors.py_ and _SmartCar.py_. Functionalities of each file have been explained in the file itself.
* <b>models.py</b> - Contains models for each type of request. Each models contains the variables necessary for creating a response using the serializer, according to the specifications.
* <b>serializers.py</b> - Contains serializers for each type of model. Each serializer creates a json response which contain the fields specified in the fields[] list.
* <b>views.py</b> - Contains views for each GET/POST request to the SmartCar API. Whenever the SmartCar API is called, one of the following views is triggered which calls the corresponding method in the utilities/SmartCar.py file. The returned dictionary is used to create an object of the model corresponding to the request. This object is passed to the serializer to get the json response which is then returned by the API.

## Testing
Tests have been provided to check the functioning of all modules. These are written in _tests.py_ file inside webapp/ directory. There are a total of 15 tests which have been written for testing the SmartCar API and are organized into 3 main classes.
* <b>GeneralMotorsUtilityTests</b> - Tests for checking whether the GM API responds correctly to requests
* <b>SmartCarUtilityTests</b> - Tests for checking functionality of all the methods in utilities/SmartCar.py
* <b>SmartCarApiTests</b> - Tests for checking whether the SmartCar API responds correctly to requests

### Directions for testing
* In order to run the tests first we make sure the server is running. If not, then execute the following command.
```
$ python3 manage.py runserver
```
* Now that we have our server running we can run the tests by executing the following command.
```
$ python3 manage.py test
```
* After running all the tests the following message should be displayed.
```
Ran 15 tests in 21.398s

OK
```
This indicates that all the test cases have been passed. <br />
Else, you'll get _FAILED_ message indicating some/all tests have failed.

## Tools and Technologies used
* [Django Rest Framework](http://www.django-rest-framework.org/)
* [Django](https://www.djangoproject.com)
* [Python](https://www.python.org/)

## Acknowledgments
* [SmartCar, Inc](https://smartcar.com/)

## References
* https://www.youtube.com/watch?v=ejJ-2oz4AgI&t=375s
* https://www.youtube.com/watch?v=qgGIqRFvFFk&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK
