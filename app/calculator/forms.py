from flask_wtf import FlaskForm
from wtforms import  SubmitField,  SelectField,  FloatField
from wtforms.validators import InputRequired

class Form(FlaskForm):
  method = SelectField("Method of Transport", [InputRequired()],
                       choices=[("Bus", "Bus"), ("Car", "Car"), ("Plane", "Plane"), ("Ferry", "Ferry"), ("Motorbike", "Motorbike"), ("Scooter", "Scooter"), ("Bicycle", "Bicycle"), ("Walk", "Walk")])
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel'), ('CNG', 'CNG'), ('Petrol', 'Petrol'), ('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')