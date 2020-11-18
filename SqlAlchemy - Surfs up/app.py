#app.py file 
from flask import Flask, jsonify
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from datetime import datetime, timedelta
from itertools import chain

#setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station 
#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return (f"Here are all of the available routes<br/>")
            f"/api/v1.0/precipitation: This list dates and Precipitation<br/>"
            f"/api/v1.0/stations : This list all stations from dataset<br/>"
            f"/api/v1.0/tobs : This list dates and temperature from a year from the last data point (2017-08-23)<br/>"
            f"/api/v1.0/startdate : This shows min, average and max temperature after specified start date<br/>"
            f"/api/v1.0/startdate/enddate : show min, average and max temperature between specified start and end date<br/><br/><br/>"
            f"Start and end date should be formatted as 'YYYY-MM-DD'")


#Convert the query results to a dictionary using date as the key and prcp as the value.
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine
    last_year_prcp = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= year_ago).all()
    dict_prcp = dict(last_year_prcp)
    session.close()
    return jsonify(last_year_prcp)
#Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():

#Query the dates and temperature observations of the most active station for the last year of data.
#Return a JSON list of temperature observations (TOBS) for the previous year.
@app.route("/api/v1.0/tobs")
def tobs():


#Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

#When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
@app.route("/api/v1.0/<start>")
def start():

#When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
@app.route("/api/v1.0/<start>/<end>")
def end():

















if __name__ == '__main__':
    app.run(debug=True)