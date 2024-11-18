# Letting Agents CRM API

This project is a RESTful API designed to serve as the backend for a Customer Relationship Management (CRM) system specifically tailored for letting agents. The API will handle the management of property listings and tenant details.


## Table of Contents

- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Testing](#testing)

## Installation

To install the project and set up your environment, follow these steps:

1. Clone the repository:

   git clone https://github.com/carlozrodri/zero_deposit.git

2. Change to the project directory:

    cd zero_deposit

3. Create a virtual enviroment

    python3 -m venv env

4. Activate the virtual enviroment
    Mac/Linux
    source env/bin/activate

    Windows
    venv\Scripts\activate

5. Install the project dependencies
    
    pip install -r requirements.txt

## Setup

1.Set up the environment variables:
Create a .env file and add the necessary environment variables:

    SECRET_KEY=your_secret_key

2. Run migrations 

    python manage.py migrate


## Usage


    
Create a superuser for testing the api:

    python manage.py createsuperuser

To run the development server
    
    python manage.py runserver
    
To create regular users for testing:

    python manage.py shell
    
```
from users.models import User
    
user = User.objects.create_user(
    username='test',
    password='test12345'
)
```
To Retrieve a Valid Token:
```
curl -L 'http://127.0.0.1:8000/auth/login/' \
-H 'Content-Type: application/json' \
-d '{
    "username": "test",
    "password": "test12345"
}'

```
To Create a Property
```
curl -L 'http://127.0.0.1:8000/api/properties/' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer TOKEN' \
-d '{
    "address": "Av. Romulo Gallegos",
    "postcode": "8871",
    "city": "Caracas",
    "rooms": 23
}'
```
To Retrieve Properties
```
curl -L 'http://127.0.0.1:8000/api/properties/' \
-H 'Authorization: Bearer TOKEN' \
-d ''
```
To Update a Property
```
curl -L -X PATCH 'http://127.0.0.1:8000/api/properties/7/' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer TOKEN' \
-d '{

    "rooms": 10
}'
```


## Testing

To Run tests
 python manage.py test
