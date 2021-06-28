import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt

#################################################
# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

# Close session
session.close()

# Flask Setup
app = Flask(__name__)

#################################################
# Flask Routes

@app.route("/")
def home_page():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitaion<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br>"
        f"/api/v1.0/&lt;start&gt;&lt;end&gt;<br>"
    )

@app.route("/api/v1.0/precipitaion")
def precipitaion():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query - all dates and prcp values
    prcp = session.query(Measurement.date, Measurement.prcp).order_by(Measurement.date).all()
    session.close()

    # To create a dictionary  
    all_precipitation_list = []
    for date, prcp in prcp:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        all_precipitation_list.append(precipitation_dict)

    return jsonify(all_precipitation_list)
    
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    station_no = session.query(Station.station, Station.name).all()
    session.close()

    # To create a dictionary  
    all_stations_list = []
    for station, name in station_no:
        station_dict = {}
        station_dict["station"] = station
        station_dict["name"] = name
        all_stations_list.append(station_dict)
    
    return jsonify(all_stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    # Query Max Date in Measurement table 8/23/2017
    query_last_date = dt.date(2017, 8, 23)
    # Query Start Date 08/24/2016#
    query_start_date = dt.date(2017, 8, 23) - dt.timedelta(days=365-1)
    # Station with the largest number of observations
    max_station = 'USC00519281'

    # Query station USC00519281 with corresponding dates (08/24/2016 through 08/23/2017) and tobs
    tobs_scores = session.query(Measurement.station, Measurement.date, Measurement.tobs).filter(Measurement.date >= query_start_date).\
        filter(Measurement.date <= query_last_date).filter(Measurement.station == max_station).all()
    
    # Close session
    session.close()

    # To create a dictionary
    tobs_list = []
    for station, date, tobs in tobs_scores:
        tobs_dict = {}
        tobs_dict["station"] = station
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        tobs_list.append(tobs_dict)

    return jsonify(tobs_list)

@app.route("/api/v1.0/<start_date>")
def start_range(start_date):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    start_date_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_date).all()

    # Close session
    session.close()

    start_list=[]
    for min, avg, max in start_date_results:
        start_dict = {}
        start_dict["TMIN"] = min
        start_dict["TAVG"] = avg
        start_dict["TMAX"] = max
        start_list.append(start_dict)
        
    return jsonify(start_list)
        
if __name__ == '__main__':
    app.run(debug=True)
    