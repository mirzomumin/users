# User CRUD
A Django application that provides all operations to interact with user table.
The following operations are available: creating, reading, editing, removing and
also signing in user.
## Setup

1. The first thing to do is to clone the repository and move to the directory "users" in your terminal:

```sh
$ git clone https://github.com/mirzomumin/users.git
$ cd users
```

## Log Files

2. If it is necessary to track bugs while running web application, add logging mechanism to this app,
otherwise just skip this step and move next. To add log files, comment out the whole "LOGGING"
variable content which is located in ./config/settings.py and in the root directory make folder named "logs" with three files 
(warning.log, error.log, critical.log) in it like the diagram showed below.

```sh
   users
     |------apps
     |------config
     |------logs
             |----warning.log
             |----error.log
             |----critical.log
```

## Project Launch

3. To launch the project with docker run the following command:

```sh
$ docker-compose up --build
```

4. The project is running now and to check it,
in your browser go to the address showed bellow:

```sh
$ http://127.0.0.1:8000/swagger/
```

## Tests

To run the tests, `cd` into the directory where `manage.py` is and run the command below:
```sh
$ docker exec user_web python manage.py test
```
