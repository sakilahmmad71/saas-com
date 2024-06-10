# Python Django Project Setup and Set by Step Guideline

### Set up and installing the django project

- Create a repo in github
- clone the repo
- create virtual environment using `python -m venv venv`
- activate the venv using `source venv/bin/activate`
- create requirements.txt
- Added Django>=5.0,<5.1 to the requirements.txt
- pip install -r requirements.txt
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

-
