from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

from hw import hw_obj
from flask import render_template, flash, redirect


@hw_obj.route("/")
def hello():
    name = "Travis"
    title = "Top Cities"
    top_cities = ['London','Paris','Los Angeles','Tokyo']
    return render_template("home.html", name=name, title=title, cities= top_cities)

class TopCities(FlaskForm):
    name = StringField('City Name', validators = [DataRequired()])
    rank = IntegerField('City Rank', validators = [DataRequired()])
    visited = BooleanField('Is visited')
    submit = SubmitField("Submit")

