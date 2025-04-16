from flask_wtf import FlaskForm
from wtforms import  SubmitField,  SelectField,  FloatField, IntegerField
from wtforms.validators import InputRequired

class Form(FlaskForm):
  method = SelectField("Method of Transport", [InputRequired()],
                       choices=[("Car", "Car"), ("Bus", "Bus"), ('Train', 'Train'), ("Plane", "Plane"), ("Ferry", "Ferry"), ("Motorbike", "Motorbike"), ("Scooter", "Scooter"), ("Bicycle", "Bicycle"), ("Walk", "Walk")])
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel'), ('CNG', 'CNG'), ('Petrol', 'Petrol'), ('Biodiesel', 'Biodiesel'), ('Hybrid (gasoline)', 'Hybrid (gasoline)'), ('No Fossil Fuel', 'No Fossil Fuel')])
  passengers = IntegerField("Number of Passengers", default=1)
  submit = SubmitField('Submit')