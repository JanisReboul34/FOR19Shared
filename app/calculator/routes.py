from flask import render_template, Blueprint, request, redirect, url_for, flash, jsonify
from app.models import Transport
from app import db
from datetime import timedelta, datetime
from flask_login import login_required, current_user
from app.calculator.forms import Form

calculator=Blueprint('calculator',__name__)

#Emissions factor per transport in kg per passemger km
#Data from: http://efdb.apps.eea.europa.eu/?source=%7B%22query%22%3A%7B%22match_all%22%3A%7B%7D%7D%2C%22display_type%22%3A%22tabular%22%7D
efco2={'Bus':{'Diesel':0.10231,'CNG':0.08,'Petrol':0.10231,'No Fossil Fuel':0},
    'Car':{'Petrol':0.18592,'Diesel':0.16453,'No Fossil Fuel':0},
    'Plane':{'Petrol':0.24298},
    'Ferry':{'Diesel':0.11131, 'CNG':0.1131, 'No Fossil Fuel':0},
    'Motorbike':{'Petrol':0.09816,'No Fossil Fuel':0},
    'Scooter':{'No Fossil Fuel':0},
    'Bicycle':{'No Fossil Fuel':0},
    'Walk':{'No Fossil Fuel':0}}
efch4={'Bus':{'Diesel':2e-5,'CNG':2.5e-3,'Petrol':2e-5,'No Fossil Fuel':0},
    'Car':{'Petrol':3.1e-4,'Diesel':3e-6,'No Fossil Fuel':0},
    'Plane':{'Petrol':1.1e-4},
    'Ferry':{'Diesel':3e-5, 'CNG':3e-5,'No Fossil Fuel':0},
    'Motorbike':{'Petrol':2.1e-3,'No Fossil Fuel':0},
    'Scooter':{'No Fossil Fuel':0},
    'Bicycle':{'No Fossil Fuel':0},
    'Walk':{'No Fossil Fuel':0}}

#Calculator, main page
@calculator.route('/calculator', methods=['GET','POST'])
@login_required
def page():
    form = Form()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = form.method.data
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('calculator.your_data'))
    return render_template('calculator/calculator.html', title='New entry', form=form)

@calculator.route('/get-items')
def get_items():
    method = request.args.get('method')
    items_dict = {
        'Bus': ['Diesel', 'CNG', 'Petrol', 'No Fossil Fuel'],
        'Car': ['Petrol', 'Diesel', 'No Fossil Fuel'],
        'Plane': ['Petrol'],
        'Ferry': ['Diesel', 'CNG', 'No Fossil Fuel'],
        'Motorbike': ['Petrol', 'No Fossil Fuel'],
        'Scooter': ['Petrol', 'No Fossil Fuel'],
        'Bicycle': ['No Fossil Fuel'],
        'Walk': ['No Fossil Fuel']
    }
    items = items_dict.get(method, [])
    return jsonify({'items': items})


#Your data
@calculator.route('/calculator/your_data')
@login_required
def your_data():
    #Table
    entries = Transport.query.filter_by(author=current_user). \
        filter(Transport.date> (datetime.now() - timedelta(days=5))).\
        order_by(Transport.date.desc()).order_by(Transport.transport.asc()).all()
    return render_template('calculator/your_data.html', title='your_data', entries=entries)

#Delete emission
@calculator.route('/calculator/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = Transport.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('calculator.your_data'))
    
  