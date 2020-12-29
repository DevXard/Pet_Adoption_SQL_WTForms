from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class PetForm(FlaskForm):
    name = StringField('Pet Name', validators=[InputRequired(message="Name canot be blanck")])
    speacies = SelectField('Species', choices=['Cat', 'Dog', 'Porcupine'])
    photo = StringField('Photo', validators=[URL()])
    age = FloatField("Age", validators=[NumberRange(min=0, max=30, message="Age canot be Over 30 or negative")])
    notes = StringField("Notes")