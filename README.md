# Django Views - Django Core

## About <a name = "about"></a>

this is a project based on the section "Django Views" of the course "Django Core"

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

> using virtualenv

```
pip install virtualenv
```

> creating a virtual environment

```
virtualenv venv
```


> activate the virtual environment

```
source venv/bin/activate
```

### Installing

A step by step series of examples that tell you how to get a development env running.

installing the pip packages

```
pip install -r requirements.txt
```


## Usage <a name = "usage"></a>

to start up, steps to follow:

```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```