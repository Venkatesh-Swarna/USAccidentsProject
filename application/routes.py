from application import app
from flask import render_template, request, json, jsonify,Flask
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
import requests
import numpy
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
import joblib

#decorator to access the app
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

#decorator to access the service
@app.route("/severityclassify", methods=['GET', 'POST'])
def severityclassify():
    if request.method == 'POST':
        #extract form inputs
        distance = request.form.get("distance")
        pressure = request.form.get("pressure")
        humidity = request.form.get("humidity")
        windChill = request.form.get("windChill")
        temperature = request.form.get("temperature")
        windSpeed = request.form.get("windSpeed")
        amenity = int(request.form.get("amenity"))
        bump = int(request.form.get("bump"))
        crossing = int(request.form.get("crossing"))
        junction = int(request.form.get("junction"))
        railway = int(request.form.get("railway"))
        stop = int(request.form.get("stop"))
        trafficSignal = int(request.form.get("trafficSignal"))
        sunriseSunset = int(request.form.get("sunriseSunset"))

        model = joblib.load('accidentsModel.pkl')
        #model = pickle.load(open('accidentsModel.pkl','rb'))
        data = pd.read_csv("cleaned_dataset.csv")

        prediction = model.predict([[distance,pressure,humidity,windChill,temperature,windSpeed,amenity, 
                                     bump, crossing,junction,railway,stop,trafficSignal, sunriseSunset]])
        results = prediction[0]
        print(results)

        print(type(amenity),sunriseSunset)
        return render_template("index.html", distance =distance,pressure=pressure,humidity=humidity,windChill=windChill,temperature=temperature,windSpeed=windSpeed, 
                               amenity = 'True' if amenity == 1 else 'False', bump = 'True' if bump == 1 else 'False', crossing = 'True' if crossing == 1 else 'False', 
                                junction = 'True' if junction == 1 else 'False', railway = 'True' if railway == 1 else 'False', 
                              stop = 'True' if stop == 1 else 'False',
                                trafficSignal = 'True' if trafficSignal == 1 else 'False', sunriseSunset = 'Day' if sunriseSunset == 1 else 'Night', results=results)
    else:
        return render_template("index.html")

