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

5. Install the project dependencies
    
    pip install -r requirements.txt

## Setup

1.Set up the environment variables:
Create a .env file and add the necessary environment variables:

    SECRET_KEY=your_secret_key

2. Run migrations 

    python manage.py migrate


## Usage

To run the development server
    
    python manage.py runserver

## Testing

To Run tests
 python manage.py test
