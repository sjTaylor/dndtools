dndtools
==========

An open source Django-based wiki-like web application for DnD.

Status
------
This github repository is currently a clone of a private repository. It contains ONLY source codes of the application, not its data.

Also, this readme file is just an early preview to be updated as soon as someone have the time.

If you find anything wrong, just start an issue.

Installation
------------
We will install the project in a virtual environment.
Virtualenvs allow to easily isolate the project dependencies from your system install.

The following instruction were tested on Linux, but should work on OSX and Windows as well.
The only requirements are Python 3 and Virtualenv.

To install DnDTools, run the following commands:

```sh
# Clone the repository 
`clone repository here`

# change dir into source folder
cd dndtools/

# Create a Python Virtual environment in env/ and enables it
virtualenv --python=python3 env

# activate environment
source env/bin/activate

# Then install all the requirements from the PyPI
pip install -r requirements.txt

# Copy the default settings for development
cd dndtools/
cp dndproject/local.py.sample dndproject/local.py


TODO: check correctness of the below steps

# Sync the database. You will be asked to create a user.
# The "--all" means that even tables based on migrations will be synced.
python manage.py syncdb --all

# Marks all database migrations as done.
python manage.py migrate --fake

# Finally, run the development server.
python manage.py runserver

# Your own version of DnDTools is now available at http://127.0.0.1:8000
```
