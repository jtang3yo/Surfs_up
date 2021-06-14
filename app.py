
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify 
#set up the database engine for Flask application access the sqlite database 
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base() #reflect tables 
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)
#create flask application called "app"

app = Flask(__name__)

@app.route("/")
def welcome(): 
    return(
    ''' 
    Welcome to the CLimate Analysis API! 
    Available Routes: 
    /api/v1.0/precipitation
    api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
#create precipitation route 
@app.route("/api/v1.0/precipitation")
#create precipitation()function 
def precipitation(): 
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365) 
    #write a query to get the date and precipitation for the previous year. 
    precipitation = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date>=prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
#Jsonify() is a function that converts the dictionary to a JSON file.
#create route for stations 
@app.route("/api/v1.0/stations")
def stations(): 
    results=session.query(Station.station).all()
    #unraveling our results into a one-dimensional array with np.ravel() with results as parameter
    stations = list(np.ravel(results))
    return jsonify(stations=stations)
#create route for temperature observations 
@app.route('/api/v1.0/tobs')
def temp_monthly(): 
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #query primary station's temperature observations 
    results = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').\
                filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
#ast route will be to report on the minimum, average, and maximum temperatures
@app.route('/api/v1.0/temp/<start>')
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None): #set start and end parameters to NONE
    #create a list to hold select results 
    sel = [func.min(Measurement.tobs), func.max(Measurement.tobs),func.avg(Measurement.tobs)]
    #if not statement to determine starting and ending dates 
    if not end: 
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps=list(np.ravel(results))
        return jsonify(temps=temps)
    
#next query for statistic temperature data 
    results = session.query(*sel).\
        filter(Measurement.date >=start).\
        filter(Measurement.date<=end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)