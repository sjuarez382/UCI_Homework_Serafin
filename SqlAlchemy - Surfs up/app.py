#app.py file 

#flask
app = Flask(__name__)

#route
@app.route("/")
def home():
    print("Here are all of the available routes")

#Convert the query results to a dictionary using date as the key and prcp as the value.
@app.route("/api/v1.0/precipitation")
def precipitation():

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