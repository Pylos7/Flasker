from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Create an instance of Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey' # for CSRF protection

# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

# FORM FIELDS
# BooleanField
# DateField
# DateTimeField
# DecimalField
# FileField
# HiddenField
# MultipleFileField
# FieldList
# FloatField
# FormField
# IntegerField
# PasswordField
# RadioField
# SelectField
# SelectMultipleField
# StringField
# SubmitField
# TextAreaField

# FILTERS
# safe
# capitalize
# lower
# upper
# title
# trim
# striptags

# Create a route decorator
@app.route('/')
def index():
    first_name = "Nestor"
    stuff = "This is bold text."

    favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
    return render_template('index.html', first_name=first_name, stuff=stuff, favorite_pizza=favorite_pizza)


#localhost:5000/user/Nestor
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)

# Create custom error pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

# Create name page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successfully!")
        
    return render_template('name.html', name = name, form=form)
