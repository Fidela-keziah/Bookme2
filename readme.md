# BookMe Website
## Summary
This is  a website We'd developed as a project for a saloon,we include numerous features like including scheduling appointments, syncing with google calendar, notifying by text messages, receipts, logs, etc...

## Preview

Admin username: admin
Admin password: testtesttest

## Requirements
Python 3 (x64 version)

## Installation
### 1. Install virtualenv and create a virtual environment called scalp and activate it
```
pip install virtualenv
virtualenv --no-site-packages scalp
cd scalp
./scripts/activate
```
### 2. Copy the file requirements.txt from the scalp-beauty-salon-website folder into the scalp environment
### 3. Install the requirements using the following command
```
pip install -r requirements.txt
```
### 4. Copy the src folder into the scalp environment
### 5. Fix credentials in src/settings.py, appointment/views.py and credentials.json to fit your own
### 6. Run the following commands
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
### 7. Open this link in any web browser http://localhost:8000/


