from flask import render_template, Blueprint, request, redirect, url_for, flash, jsonify
from app.models import Transport
from app import db
from datetime import timedelta, datetime
from flask_login import login_required, current_user
from app.calculator.forms import Form
import json

calculator=Blueprint('calculator',__name__)

#Emissions factor per transport in kg per passemger km
#Data from: http://efdb.apps.eea.europa.eu/?source=%7B%22query%22%3A%7B%22match_all%22%3A%7B%7D%7D%2C%22display_type%22%3A%22tabular%22%7D
efco2={'Bus':{'Diesel':0.03,'CNG':0.0285, 'No Fossil Fuel':0.013},
    'Car':{'Petrol':0.180,'Diesel':0.160, 'Hybrid (gasoline)': 0.100, 'CNG': 0.130, 'No Fossil Fuel':0.026},
    'Train': {'Diesel': 0.027, 'Biodiesel': 0.014, 'No Fossil Fuel': 0.013}, ##ADD BIODIESEL
    'Plane':{'Petrol':0.300},
    'Ferry':{'Diesel':0.019, 'CNG': 0.01425},
    'Motorbike':{'Petrol':0.200},
    'Scooter':{'Petrol': 0.100,'No Fossil Fuel':0},
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
        passengers = form.passengers.data
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * (efco2[transport][fuel]/passengers)

        co2 = float("{:.2f}".format(co2))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('calculator.your_data'))
    return render_template('calculator/calculator.html', title='New entry', form=form)

@calculator.route('/get-items')
def get_items():
    method = request.args.get('method')
    items_dict = {
        'Bus': ['Diesel', 'CNG', 'No Fossil Fuel'],
        'Car': ['Petrol', 'Diesel', 'Hybrid (gasoline)', 'CNG', 'No Fossil Fuel'],
        'Train': ['Diesel', 'Biodiesel', 'No Fossil Fuel'],
        'Plane': ['Petrol'],
        'Ferry': ['Diesel', 'CNG'],
        'Motorbike': ['Petrol'],
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
        filter(Transport.date> (datetime.now() - timedelta(days=30))).\
        order_by(Transport.date.desc()).order_by(Transport.transport.asc()).all()

#Emissions by category
    emissions_by_transport = db.session.query(db.func.sum(Transport.co2), Transport.transport). \
        filter(Transport.date > (datetime.now() - timedelta(days=30))).filter_by(author=current_user). \
        group_by(Transport.transport).order_by(Transport.transport.asc()).all()
    emission_transport = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    first_tuple_elements = []
    second_tuple_elements = []
    for a_tuple in emissions_by_transport:
        first_tuple_elements.append(a_tuple[0])
        second_tuple_elements.append(a_tuple[1])

    if 'Bus' in second_tuple_elements:
        index_bus = second_tuple_elements.index('Bus')
        emission_transport[1]=first_tuple_elements[index_bus]
    else:
        emission_transport[1]

    if 'Car' in second_tuple_elements:
        index_car = second_tuple_elements.index('Car')
        emission_transport[2]=first_tuple_elements[index_car]
    else:
        emission_transport[2]

    if 'Ferry' in second_tuple_elements:
        index_ferry = second_tuple_elements.index('Ferry')
        emission_transport[3]=first_tuple_elements[index_ferry]
    else:
        emission_transport[3]

    if 'Motorbike' in second_tuple_elements:
        index_motorbike = second_tuple_elements.index('Motorbike')
        emission_transport[4]=first_tuple_elements[index_motorbike]
    else:
        emission_transport[4]

    if 'Plane' in second_tuple_elements:
        index_plane = second_tuple_elements.index('Plane')
        emission_transport[5]=first_tuple_elements[index_plane]
    else:
        emission_transport[5]
    
    if 'Scooter' in second_tuple_elements:
        index_scooter = second_tuple_elements.index('Scooter')
        emission_transport[6]=first_tuple_elements[index_scooter]
    else:
        emission_transport[6]

    if 'Train' in second_tuple_elements:
        index_train = second_tuple_elements.index('Train')
        emission_transport[7]=first_tuple_elements[index_train]
    else:
        emission_transport[7]

    #Kilometers by category
    kms_by_transport = db.session.query(db.func.sum(Transport.kms), Transport.transport). \
        filter(Transport.date > (datetime.now() - timedelta(days=30))).filter_by(author=current_user). \
        group_by(Transport.transport).order_by(Transport.transport.asc()).all()
    kms_transport = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    first_tuple_elements = []
    second_tuple_elements = []
    for a_tuple in kms_by_transport:
        first_tuple_elements.append(a_tuple[0])
        second_tuple_elements.append(a_tuple[1])

    if 'Bicycle' in second_tuple_elements:
        index_bicycle = second_tuple_elements.index('Bicycle')
        kms_transport[0]=first_tuple_elements[index_bicycle]
    else:
        kms_transport[0] 

    if 'Bus' in second_tuple_elements:
        index_bus = second_tuple_elements.index('Bus')
        kms_transport[1]=first_tuple_elements[index_bus]
    else:
        kms_transport[1]

    if 'Car' in second_tuple_elements:
        index_car = second_tuple_elements.index('Car')
        kms_transport[2]=first_tuple_elements[index_car]
    else:
        kms_transport[2]

    if 'Ferry' in second_tuple_elements:
        index_ferry = second_tuple_elements.index('Ferry')
        kms_transport[3]=first_tuple_elements[index_ferry]
    else:
        kms_transport[3]

    if 'Motorbike' in second_tuple_elements:
        index_motorbike = second_tuple_elements.index('Motorbike')
        kms_transport[4]=first_tuple_elements[index_motorbike]
    else:
        kms_transport[4]

    if 'Plane' in second_tuple_elements:
        index_plane = second_tuple_elements.index('Plane')
        kms_transport[5]=first_tuple_elements[index_plane]
    else:
        kms_transport[5]

    if 'Scooter' in second_tuple_elements:
        index_scooter = second_tuple_elements.index('Scooter')
        kms_transport[6]=first_tuple_elements[index_scooter]
    else:
        kms_transport[6]   

    if 'Train' in second_tuple_elements:
        index_train = second_tuple_elements.index('Train')
        kms_transport[7]=first_tuple_elements[index_train]
    else:
        kms_transport[7]   

    if 'Walk' in second_tuple_elements:
        index_walk = second_tuple_elements.index('Walk')
        kms_transport[8]=first_tuple_elements[index_walk]
    else:
        kms_transport[8]    

    #Emissions by date (individual)
    emissions_by_date = db.session.query(db.func.sum(Transport.co2), Transport.date). \
        filter(Transport.date > (datetime.now() - timedelta(days=30))).filter_by(author=current_user). \
        group_by(Transport.date).order_by(Transport.date.asc()).all()
    over_time_emissions = []
    dates_label = []
    for total, date in emissions_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_emissions.append(total)    

    #Kms by date (individual)
    kms_by_date = db.session.query(db.func.sum(Transport.kms), Transport.date). \
        filter(Transport.date > (datetime.now() - timedelta(days=30))).filter_by(author=current_user). \
        group_by(Transport.date).order_by(Transport.date.asc()).all()
    over_time_kms = []
    dates_label = []
    for total, date in kms_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_kms.append(total)      


    return render_template('calculator/your_data.html', title='Your Data', entries=entries,
        emissions_by_transport_python_dic=emissions_by_transport,     
        emission_transport_python_list=emission_transport,             
        emissions_by_transport=json.dumps(emission_transport),
        kms_by_transport=json.dumps(kms_transport),
        over_time_emissions=json.dumps(over_time_emissions),
        over_time_kms=json.dumps(over_time_kms),
        dates_label=json.dumps(dates_label))
    

#Delete emission
@calculator.route('/calculator/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = Transport.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('calculator.your_data'))
    
  