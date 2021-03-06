# Citation for run.py:
# Date: 05/18/2022
# Copied from: OSU cs340_starter_app
# Source URL: https://github.com/mlapresta/cs340_starter_app

#this file is used to run your flask-based-database-interacting-website persistently!

#change this line to run the app that you want to run
#from db_connector.sample import app
from starter_website.webapp import app
#for example, the above line tells to run the sample db connection app in db_connector/ directory

#then from the commandline run:
#./venv/bin/activate
#gunicorn run:app -b 0.0.0.0:SOME_NUMBER_BETWEEN_1025_and_65535
#eg. gunicorn run:app -b 0.0.0.0:8842
