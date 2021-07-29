# AI_numbers

Tested with Windows 10 (host). With Linux there may be slight differences with the commands (i.e. you may need to use pip3 instead pip and python3 instead python)
AI_numbers is simple program which utilizes AI/ML to recognize digits which are sent as input (28x28 and png).

- Django 3.2 (python)
- REST
- AI/Machine learning
- Virtual environment

# Environment

This is just a suggestion. You can of course use whatever approach you prefer (i.e. VM).

## Requirements (host machine)

virtualenv==20.0.21 (tested with, probably works with other modern versions too)

So install virtualenv to your host machine (depending on your approach)

```bash
pip install virtualenv # if you already have virtualenv installed, you can skip this most likely
```

## Create and activate virtual environment

```bash
py -m venv venv # create virtual environment called venv / needs only to be done once
venv\Scripts\activate.bat # activate virtual environment
```

# App

Pull/clone app with git or simply just download it.
Set secret key (random numbers: https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-SECRET_KEY) in ai_numbers_project/settings.py.
Note that this project tries to import secret_key from ai_numbers/environment.py but that file is not included in git so either delete import or make your own environment file which includes the secret key (secret_key="insert_random_letters").

## Installation of requirements (inside of virtual environment)

```bash
pip install -r requirements.txt # needs only to be done once, make sure you have activated your virtual environment and are inside of it
```

## Run project

```bash
cd ai_numbers_project
python manage.py makemigrations # needs only to be done once or if you do modifications to the db models
python manage.py migrate # needs only to be done once or if you do modifications to the db models
python manage.py runserver
```

## Train model

Project should already include trained model (digits.model), however if it does not or you want to re-train model then simply do:

```bash
python manage.py train_model # you probably do not need to run this command
```

## Use model

Send .png file (28x28) of your digit to path/api/recognize/digit/ (i.e: http://localhost:8000/api/recognize/digit/). App includes example_digits which should be detected correctly but you can of course create your own digits too with paint. Key which you should use with the image is "image".
