# User CRUD
A Django application that provides all operations to interact with user table.
The following operations are available: creating, reading, editing, removing and
also signing in user.
## Setup

1. The first thing to do is to clone the repository and move to the directory:

```sh
$ git clone https://github.com/mirzomumin/user.git
$ cd library
```

2. Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv venv
$ source env/bin/activate
```

3. Then install the dependencies from the requirements.txt file:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

4. Once `pip` has finished downloading the dependencies run the following command
to create database/database structure of the project:

```sh
(env)$ python manage.py migrate
```
the primary database settings of django are configured for sqlite3 but
you can set any database you wish

5. After follow the command to run app on local server:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/swagger/`.


## Tests

To run the tests, `cd` into the directory where `manage.py` is and run the command below:
```sh
(env)$ python manage.py test
```
