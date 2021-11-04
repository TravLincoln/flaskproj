from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

from hw import hw_obj
from flask import render_template, flash, redirect


class CityForm(FlaskForm):
    cname= StringField('City Name', validators = [DataRequired()])
    rank = IntegerField('City Rank', validators = [DataRequired()])
    visited = BooleanField('Is visited')
    submit = SubmitField('Submit')

#class TopCities(FlaskForm):
   # name = StringField('City Name', validators = [DataRequired()])
    #rank = IntegerField('City Rank', validators = [DataRequired()])
    #visited = BooleanField('Is visited')
    #submit = SubmitField("Submit")
