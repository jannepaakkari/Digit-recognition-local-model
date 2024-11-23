# AI_numbers

AI_numbers is a digit recognition application originally developed in 2021 using Django 3 and updated to Django 5.1 in 2024. The application utilizes AI/ML to recognize handwritten digits from 28x28 pixel PNG images. Though a relatively simple project, it demonstrates the integration of several technologies.

Technologies:
- Django 3.2 (Python) and Django 5.1 (updated)
- REST API
- Django commands
- AI/ML for digit recognition with a locally trained model (digits.keras)
- Virtual environment

# Environment

This is a suggested environment setup, but you're free to use any approach you prefer. The project has been designed to be flexible and not overly opinionated about the environment. As long as you have installed the required dependencies, you should be able to run the project without issues.

Note: You may want to unfreeze the requirements (currently frozen as of 23.11.2024) if you'd like to update to the latest versions of the dependencies.

# App

You can clone or download the app using Git.
After setting up the project, make sure to define a secret key in settings.py. The project currently tries to import it from environment import secret_key, but the secret_key is not included with the project. Without setting a secret key, the project will not start.

## Host Machine

Go to the project

```bash
pip install virtualenv # if you already have virtualenv installed, you can skip this most likely
py -m venv venv # create virtual environment called venv / needs only to be done once
venv\Scripts\activate.bat # activate virtual environment
```

## Installation of requirements & run project (inside of virtual environment)

```bash
pip install -r requirements.txt # needs only to be done once, make sure you have activated your virtual environment and are inside of it.
cd ai_numbers_project
python manage.py makemigrations # needs only to be done once or if you do modifications to the db models
python manage.py migrate # needs only to be done once or if you do modifications to the db models
python manage.py runserver
```


## Use/test model

POST .png file (28x28) of your digit to path/api/recognize/digit/ (i.e: http://localhost:8000/api/recognize/digit/). You can of course copy digit(s) from /example_digits folder if you do not wish to make your own digits, but you want to test that setup works as intended. "Key" which you should use with the digit is "image".

Alternatively you can replace digits in /example_digits folder with your own digits (make sure they are .png, 28x28, and image name is same than in image which you replace) and then run:

```bash
python manage.py test # Runs unit tests in tests.py Run from /ai_numbers_project
```

Result should be "ok".


# Train model

The project should already include a pre-trained model (digits.keras), so you typically don't need to retrain it. However, if you want to re-train the model for any reason, you can use the following command:

```bash
python manage.py train_model # you probably do not need to run this command
```

