# AI_numbers
Tested with Windows 10 (host). 
AI_numbers is simple program which utilizes AI to recognize numbers which are sent as input.

# Environment
## Requirements (host machine)
virtualenv==20.0.21 (tested with, probably works with other versions too)

## Install and use virtual environment
```bash
py -m venv venv
ai_numbers\Scripts\activate.bat
```

## Installation of requirements (inside of virtual envionment)
```bash
venv\Scripts\activate.bat
pip install -r requirements.txt
```
# App
Pull/clone app with git.

## Run project
```bash
cd ai_numbers_project
python manage.py runserver
```