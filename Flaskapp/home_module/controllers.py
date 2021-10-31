# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
                  
# Import the database object from the main app module
#from Flaskapp import db

# Define the blueprint: 'home_module', set its url prefix: app.url/
home_module = Blueprint('home_module', __name__, url_prefix='/')