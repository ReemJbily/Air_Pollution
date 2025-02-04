from flask import Flask, request, jsonify,render_template, redirect, send_file, url_for, abort
import pickle
import numpy as np
import pandas as pd
import pickle
from utility import model_loader

app=Flask(__name__)
model=model_loader.load_model()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method=='POST':        
        return redirect(url_for('classification',**request.form))   
    return render_template('index.html')

@app.route('/classifier', methods=['POST'])
def classification():
   features = {
            'Temperature': float(request.form['Temperature']),
            'Humidity': float(request.form['Humidity']),
            'PM2.5': float(request.form['PM2.5']),
            'PM10': float(request.form['PM10']),
            'NO2': float(request.form['NO2']),
            'SO2': float(request.form['SO2']),
            'CO': float(request.form['CO']),
            'Proximity_to_Industrial_Areas': float(request.form['Proximity_to_Industrial_Areas']),
            'Population_Density': float(request.form['Population_Density'])}
   df = pd.DataFrame([features], columns=['Temperature', 'Humidity', 'PM2.5', 
                                          'PM10', 'NO2', 'SO2', 'CO', 
                                          'Proximity_to_Industrial_Areas', 'Population_Density'])        
   prediction = model.predict(df)[0]        
   categories = ['Good', 'Moderate', 'Poor', 'Hazardous']
   air_quality = categories[prediction]        
   return render_template("classifier.html",quality=air_quality)


if __name__ == '__main__':   
    app.run(debug=True)