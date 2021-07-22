# AI_numbers

Tested with Windows 10 (host).
AI_numbers is simple program which utilizes AI to recognize numbers which are sent as input.

# Environment

This is just a suggestion. You can of course whatever approach you prefer (i.e. VM).

## Requirements (host machine)

virtualenv==20.0.21 (tested with, probably works with other versions too)

So install virtualenv to your host machine (depending on your approach)

```bash
pip install virtualenv
```

## Create and activate virtual environment

```bash
py -m venv venv # create
venv\Scripts\activate.bat # activate
```

## Installation of requirements (inside of virtual envionment)

```bash
pip install -r requirements.txt
```

# App

Pull/clone app with git.

## Run project

```bash
cd ai_numbers_project
python manage.py runserver
```
