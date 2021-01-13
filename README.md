# SupChain

SupChain is a decentralized web application based on Ethereum blockchain. Application allows users to enter information about every stage of supply chain (in this case there are producer, wholesaler, shipper and detailer). User can also check entered information by product id.


# Table of context

  - [General info](#General-info)
  - [Setup](#Setup)
  - [Technologies](#Technologies)
  - [Development](#Development)


## General info
Why decentrailzation in supply chain management? Firstly, decentralized application provides transparency. Application connects to public blockchain network, so every action taken is recorded in the public registry. Besides that, checking information about products is much easier and faster. In the classic supply chain system, every link of chain has its own database that is almost certainly incompatible with the others. Blockchain gathers all details in one place and makes data structure more constistent.

## Setup
To run the app locally you need to follow these steps.


Clone this repository
```
git clone https://github.com/macieksitko/Django-blockchain.git
```

Create new virtual environment
- install **pipenv**
```
pip3 install pipenv
```
 - activate environment
```
pipenv shell
```

- install all packages
```
pip install -r requirements.txt
```

Create secret file, for example .env and generate secret key from https://miniwebtool.com/django-secret-key-generator/. Past the key into  the secret file.

```
export SECRET_KEY='<secret_key>'
```

Create a postgres db and add the credentials to settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'name',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

Migrate your added database from scratch
```
python manage.py makemigrations
```
and then
```
python manage.py migrate
```
Create new super user
```
python manage.py createsuperuser
```
Run the application
```
python manage.py runserver
```


## Technologies
Main technologies used in the application:
 - Django 3.1.4
 - Python 3.7.9
 - Truffle 
 - Web3 5.12.1

The complete list of used libraries is in the file **requirements.txt**
## Development
Application can be developed in many directions. Some ideas that I am thinking of now:
 - File attachment
 - Transactions history


