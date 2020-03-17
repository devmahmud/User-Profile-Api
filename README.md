# Profiles API

A Django Rest Framework project to demonstrate custom user model implementation with login, register, status update and some custom permissions. In this project i have replaced username field to email for authentication by extending AbstractBaseUser and BaseUserManager.

# Requirements
```
open requirements.txt file to see requirements

To install requirements type

pip install -r requirements.txt
```

# Installing
```
open terminal and type

git clone https://github.com/devmahmud/User-Profile-Api.git
```
or simply download using the url below
```
https://github.com/devmahmud/User-Profile-Api.git
```
# To migrate the database open terminal in project directory and type
```
python manage.py makemigrations
python manage.py migrate
```

# Creating Superuser
```
To create superuser open terminal and type
python manage.py createsuperuser
```

# To run the program in local server use the following command

```
python manage.py runserver
```
Then go to http://127.0.0.1:8000 in your browser to see available endpoints

## Author
<blockquote>
Mahmudul alam
Email: expelmahmud@gmail.com
</blockquote>

========Thank You !!!=========


