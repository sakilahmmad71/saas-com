# Python Django Project Setup and Set by Step Guideline

### Set up and installing the django project

- Create a repo in github
- clone the repo
- create virtual environment using `python -m venv venv`
- activate the venv using `source venv/bin/activate`
- create requirements.txt
- Added Django>=5.0,<5.1 to the requirements.txt
- `pip install -r requirements.txt`
- pip install pip --upgrade
- pip freeze to see all the libraries has been installed
- `cd src`
- `django-admin startproject cfehome .`

### Creating views

- create a file named views.py
- add some function which will return texts, html
- import the HttpResponse
- Return the text or html using the HttpResponse object

### Creating templates

- make folder called pages
- go through the `main` and update the `settings.py`
- update the `DIRS` list with the templates we have created
- import the html files from the views and start using the template
- inside templates can be use inheritance
- blocks and other things as needed

### Create a app

- `python manage.py startapp YOUR_APP_NAME`
- go through the `main` and update the `settings.py`
- list the installed apps inside the `INSTALLED_APPS` lists
- start working on the app

### Create a model

- every app contains model
- create model including all the columns you needed
- `python manage.py makemigrations`
- `python manage.py migrate`
- the model now can be use anywhere needed
- model contains the objects and other methods
- see the documentation for other use cases
