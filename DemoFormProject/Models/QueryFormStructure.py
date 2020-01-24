
### ----------------------------------------------------------- ###
### --- include all software packages and libraries needed ---- ###
### ----------------------------------------------------------- ###
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import Form, BooleanField, PasswordField
from wtforms import TextField, TextAreaField, SelectField, DateField
from wtforms import validators, ValidationError

from wtforms.validators import DataRequired
### ----------------------------------------------------------- ###




## This class have the fields that are part of the Country-Capital demonstration
## You can see two fields:
##   the 'name' field - will be used to get the country name
##   the 'submit' button - the button the user will press to have the 
##                         form be "posted" (sent to the server for process)
class QueryFormStructure(FlaskForm):
    """This class is the list of the fields that will participate in our form"""
    name   = StringField('Country Name?)' , validators = [DataRequired()])
    submit = SubmitField('Submit')